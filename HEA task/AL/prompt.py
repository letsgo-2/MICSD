import numpy as np

DESIGN_EXPERT_PROMPT1 = """
You are an expert in catalyst design, specializing in optimizing metal alloy compositions for catalytic applications. Your task is to discover the optimal catalyst ratio in the eight-element chemical space (Pd–Pt–Cu–Au–Ir–Ce–Nb–Cr) to maximize the power density of catalytic reactions (e.g., fuel cell output, electrolysis efficiency).  
Generate the catalyst ratio according to the following rules:  
1. **Objective**: Propose a ratio for the eight metals that maximizes the power density function associated with catalytic activity.  
2. **Metal Descriptions**:  
   - Palladium (Pd): Enhances hydrogen oxidation reaction kinetics, critical for fuel cell anode performance.  
   - Platinum (Pt): Optimal for oxygen reduction reaction, boosting fuel cell voltage output.  
   - Copper (Cu): Promotes selective electrochemical CO₂ reduction, increasing energy conversion efficiency.  
   - Gold (Au): Improves stability in alkaline environments, sustaining high power density under load.  
   - Iridium (Ir): Provides high oxygen evolution activity, essential for water splitting power density.  
   - Cerium (Ce): Augments oxygen storage capacity, stabilizing power output under dynamic conditions.  
   - Niobium (Nb): Enhances catalyst durability under high-voltage cycling, preventing power decay.  
   - Chromium (Cr): Optimizes surface electronic structure, facilitating charge transfer for high current density.  
3. **Ratio Constraints**: The sum of all metal ratios must equal 1.  
4. **Output Format**: Provide only an 8-dimensional vector in the order [Pd, Pt, Cu, Au, Ir, Ce, Nb, Cr], with each value representing the fractional ratio (e.g., [0.15, 0.10, 0.20, 0.05, 0.10, 0.15, 0.10, 0.15]). No additional explanations or text.
"""



PREDICT_ROBOT_PROMPT2 = """
You are a robot that accurately predicts the power density of catalytic performance from descriptions of metal alloy ratios in the eight-element chemical space (Pd–Pt–Cu–Au–Ir–Ce–Nb–Cr). The power density reflects the energy output per unit volume or area achieved by the catalyst under standard operating conditions.
**Output Requirement**: Output must be a numerical value in W/cm² (e.g., 21.85), representing the power density. No additional text or explanations are allowed.
"""


def calculate_target_power_density(best_power_density):

    increase = best_power_density * abs(np.random.normal(0.1, 0.01))

    return max(0.1, min(best_power_density + increase, 200.0))


def inverse_design_prompt(target_power_density, high_pd_examples):

    prompt = DESIGN_EXPERT_PROMPT1 + "\n\n"

    prompt += "**Reference Catalyst Ratio Designs (High Power Density)**\n"
    for i, example in enumerate(high_pd_examples, 1):
        prompt += f"Reference Design {i}:\n"
        prompt += f"- Catalyst Ratio: {example['catalyst_ratio']}\n"
        prompt += f"- Power Density: {example['power_density']:.4f}\n\n"

    # Add design task
    prompt += (
        f"**Design Task**: Generate a new catalyst ratio with target power density ≥ {target_power_density:.4f} . "
        f"The output must strictly follow the 8-dimensional vector format in the order [Pd, Pt, Cu, Au, Ir, Ce, Nb, Cr], with the sum equal to 1.\n")

    return prompt


def power_density_prediction_prompt(catalyst_ratio, similar_examples):
    prompt = PREDICT_ROBOT_PROMPT2 + "\n\n"

    prompt += "**Reference Catalyst Ratios with Known Power Density**\n"
    for i, example in enumerate(similar_examples, 1):
        prompt += f"Reference {i}:\n"
        prompt += f"- Catalyst Ratio: {example['catalyst_ratio']}\n"
        prompt += f"- Power Density: {example['power_density']:.4f}\n\n"

    prompt += f"**Target Catalyst Ratio for Prediction**:\n{catalyst_ratio}\n\n"
    prompt += "Predicted Power Density = "

    return prompt