# crewai/__init__.py (stub replacement for real CrewAI package)

class Agent:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def run(self, *args, **kwargs):
        return {"message": "Stub CrewAI Agent executed."}

__all__ = ["Agent"]
