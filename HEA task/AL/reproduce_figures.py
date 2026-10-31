"""按原绘图脚本绘制图 8(a/b/c)。"""

import os
from pathlib import Path
import subprocess
import sys


def main():
    root = Path(__file__).resolve().parent
    env = dict(os.environ, MPLBACKEND="Agg", PYTHONUTF8="1")
    for script in ("plot_a.py", "plot_b.py", "plot_c.py"):
        subprocess.run(
            [sys.executable, "-B", str(root / script)],
            cwd=root, env=env, check=True,
        )
    print(f"三个子图已生成: {root / 'experinced plot'}")


if __name__ == "__main__":
    main()
