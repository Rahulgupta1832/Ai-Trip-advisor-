# crewai/__init__.py — expanded stubs including Crew.kickoff
# Safe placeholders so the app can import and run in the deployed environment.

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
        return {"text": "LLM stub response."}

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
    Minimal Crew stub with kickoff() and helpful helpers used by the app.
    """
    def __init__(self, members=None, *args, **kwargs):
        self.members = members or []
        self.args = args
        self.kwargs = kwargs
        self._last_result = None

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
        self._last_result = results
        return results

    def kickoff(self, *args, **kwargs):
        """
        Start the crew in a default way. Return a predictable stub result
        matching what the app expects (adjust if your app expects a specific shape).
        """
        # Try to run all members; if none, return a default message
        if not self.members:
            res = {"status": "stub", "message": "Crew kickoff run: no members (stub)."}
            self._last_result = res
            return res

        results = self.run_all(*args, **kwargs)
        self._last_result = {"status": "stub", "results": results}
        return self._last_result

    def last_result(self):
        return self._last_result


class Process:
    def __init__(self, name="process", mode=None, *args, **kwargs):
        self.name = name
        self.mode = mode
        self.running = False

    def start(self, *args, **kwargs):
        self.running = True
        return {"status": "started", "name": self.name}

    def stop(self, *args, **kwargs):
        self.running = False
        return {"status": "stopped", "name": self.name}

    def run(self, *args, **kwargs):
        return {"status": "stub", "name": self.name, "mode": self.mode, "output": "Process run in stub mode."}

    @classmethod
    def sequential(cls, *args, **kwargs):
        return cls(name="sequential", mode="sequential", *args, **kwargs)

    @classmethod
    def parallel(cls, *args, **kwargs):
        return cls(name="parallel", mode="parallel", *args, **kwargs)


# Export expected names
__all__ = ["Agent", "LLM", "Task", "Crew", "Process"]
