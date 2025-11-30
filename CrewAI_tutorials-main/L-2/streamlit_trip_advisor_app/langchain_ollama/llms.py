# stub for langchain_ollama.llms.OllamaLLM

class OllamaLLM:
    """
    Minimal OllamaLLM stub to satisfy imports and basic usage.
    This returns safe placeholder responses. Replace with the real
    library when deploying on an environment that supports it.
    """
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def generate(self, prompt, max_tokens=100, **kwargs):
        # mimic a typical LLM return; adjust per your app if needed
        return {"text": "OllamaLLM stub response. Install real langchain_ollama for full functionality."}

    def __call__(self, prompt, **kwargs):
        return self.generate(prompt, **kwargs)

__all__ = ["OllamaLLM"]
