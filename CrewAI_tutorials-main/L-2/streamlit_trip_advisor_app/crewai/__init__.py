# crewai/__init__.py — combined minimal stubs for deployment
# These are placeholders so the app can import and run. Replace with real CrewAI package for full functionality.

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
        return {"text": "LLM stub response. Install real CrewAI or OpenAI for full functionality."}

    def __call__(self, prompt, **kwargs):
        return self.generate(prompt, **kwargs)


class Task:
    """
    Minimal Task stub to satisfy 'from crewai import Task'.
    Implement methods your app expects. This basic stub stores task args
    and provides a run/execute method returning a safe placeholder.
    """
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def run(self, *args, **kwargs):
        return {"status": "stub", "result": "Task executed in stub mode."}

    # Some code may call execute or __call__
    def execute(self, *args, **kwargs):
        return self.run(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        return self.run(*args, **kwargs)


# Export names expected by the app
__all__ = ["Agent", "LLM", "Task"]
