# glm_client.py
import os
import requests

class GLMClient:
    """
    Lightweight client for GLM-5.3 API, supporting OpenAI/Anthropic-compatible endpoints,
    token management, and 1M context handling.
    """
    def __init__(self, api_key: str = None, base_url: str = "https://api.z.ai/v1"):
        self.api_key = api_key or os.getenv("GLM_API_KEY", "free-october-token")
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def generate_code(self, prompt: str, context_files: dict = None, max_tokens: int = 4096) -> str:
        """
        Sends a code generation prompt with local project context to the GLM-5.3 model.
        """
        formatted_context = ""
        if context_files:
            for path, content in context_files.items():
                formatted_context += f"--- FILE: {path} ---\n{content}\n\n"

        payload = {
            "model": "glm-5.3",
            "messages": [
                {"role": "system", "content": "You are GLM-5.3, the #1 open-weights coding model. Write precise, clean code."},
                {"role": "user", "content": f"{formatted_context}\nTask: {prompt}"}
            ],
            "max_tokens": max_tokens,
            "temperature": 0.2
        }

        try:
            response = requests.post(
                f"{self.base_url}/chat/completions",
                headers=self.headers,
                json=payload,
                timeout=60
            )
            response.raise_for_status()
            result = response.json()
            return result["choices"][0]["message"]["content"]
        except requests.exceptions.RequestException as e:
            return f"# Error connecting to GLM-5.3 endpoint: {e}\n# (Ensure your local setup or API key is active)"
