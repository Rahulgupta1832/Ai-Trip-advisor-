# crewai/__init__.py — minimal stubs to allow deployment (real CrewAI not required)

class Agent:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def run(self, *args, **kwargs):
        return {"status": "stub", "message": "CrewAI Agent not available (stub)."}


class LLM:
    """
    Minimal LLM stub. Provide the methods your code might call.
    Adjust returns if your code expects other shapes.
    """
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def generate(self, prompt, max_tokens=100, **kwargs):
        # Return a simple stubbed response that mimics an LLM output
        return {"text": "LLM stub response. Install real CrewAI or OpenAI for full functionality."}

    # Some code may call __call__ instead of generate
    def __call__(self, prompt, **kwargs):
        return self.generate(prompt, **kwargs)


# Export expected names
__all__ = ["Agent", "LLM"]
