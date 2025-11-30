# crewai/__init__.py — expanded minimal stubs for deployment
# These are safe placeholders so the app can import and run.
# They return simple stub responses; replace with the real CrewAI package later.

class Agent:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def run(self, *args, **kwargs):
        return {"status": "stub", "message": "CrewAI Agent not available (stub)."}


class LLM:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def generate(self, prompt, max_tokens=100, **kwargs):
        return {"text": "LLM stub response. Install real CrewAI or OpenAI for full functionality."}

    def __call__(self, prompt, **kwargs):
        return self.generate(prompt, **kwargs)


class Task:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def run(self, *args, **kwargs):
        return {"status": "stub", "result": "Task executed in stub mode."}

    def execute(self, *args, **kwargs):
        return self.run(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        return self.run(*args, **kwargs)


class Crew:
    """
    Minimal Crew stub: a collection/manager of Task/Agent objects.
    Provide only simple behavior so imports and basic usage work.
    """
    def __init__(self, members=None, *args, **kwargs):
        self.members = members or []
        self.args = args
        self.kwargs = kwargs

    def add(self, member):
        self.members.append(member)

    def run_all(self, *args, **kwargs):
        results = []
        for m in self.members:
            try:
                res = m.run(*args, **kwargs)
            except Exception:
                try:
                    res = m(*args, **kwargs)
                except Exception:
                    res = {"status": "stub", "result": None}
            results.append(res)
        return results


class Process:
    """
    Minimal Process stub: represents a runnable process/workflow.
    """
    def __init__(self, name="process", *args, **kwargs):
        self.name = name
        self.args = args
        self.kwargs = kwargs
        self.running = False

    def start(self, *args, **kwargs):
        self.running = True
        return {"status": "started", "name": self.name}

    def stop(self, *args, **kwargs):
        self.running = False
        return {"status": "stopped", "name": self.name}

    def run(self, *args, **kwargs):
        return {"status": "stub", "name": self.name, "output": "Process run in stub mode."}


# Export expected names
__all__ = ["Agent", "LLM", "Task", "Crew", "Process"]
