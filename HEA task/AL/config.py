"""通过环境变量设置 API；本文件不保存密钥。"""

import os

API_KEY = os.environ.get("OPENAI_API_KEY", "")
API_BASE_URL = os.environ.get("OPENAI_BASE_URL", "https://api.zhizengzeng.com/v1")
LLM_MODEL = os.environ.get("OPENAI_MODEL", "gpt-4o")
