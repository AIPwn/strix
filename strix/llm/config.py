import os
from typing import Optional


class LLMConfig:
    def __init__(
        self,
        model_name: str | None = None,
        temperature: float = 0,
        enable_prompt_caching: bool = True,
        prompt_modules: list[str] | None = None,
        api_base: Optional[str] = None,
        api_key: Optional[str] = None,
    ):
        self.model_name = model_name or os.getenv("STRIX_LLM", "openai/gpt-5")

        if not self.model_name:
            raise ValueError("STRIX_LLM environment variable must be set and not empty")

        self.temperature = max(0.0, min(1.0, temperature))
        self.enable_prompt_caching = enable_prompt_caching
        self.prompt_modules = prompt_modules or []

        # Support custom API base URL
        self.api_base = api_base or os.getenv("STRIX_API_BASE")
        self.api_key = api_key or os.getenv("STRIX_API_KEY") or os.getenv("LLM_API_KEY")

        # Set model-specific defaults
        self._configure_model_defaults()

    def _configure_model_defaults(self):
        """Configure model-specific API settings."""
        if not self.model_name:
            return

        model_lower = self.model_name.lower()

        # DeepSeek models
        if "deepseek" in model_lower:
            if not self.api_base:
                self.api_base = "https://api.deepseek.com"
            if not self.api_key:
                self.api_key = os.getenv("DEEPSEEK_API_KEY")

        # GLM models (Zhipu AI)
        elif "glm" in model_lower or "zhipu" in model_lower:
            if not self.api_base:
                self.api_base = "https://open.bigmodel.cn/api/paas/v4"
            if not self.api_key:
                self.api_key = os.getenv("GLM_API_KEY") or os.getenv("ZHIPU_API_KEY")

        # Custom OpenAI-compatible API or any model with custom API base
        if self.api_base and not self.api_key:
            # For custom OpenAI-compatible APIs, fallback to common key variables
            self.api_key = os.getenv("OPENAI_API_KEY") or os.getenv("STRIX_API_KEY") or os.getenv("LLM_API_KEY")
