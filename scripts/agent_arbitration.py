import os
import json

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
AGENT_DIR = os.path.join(REPO_ROOT, "agents")


class AgentArbitration:
    """Resolves agent priority and queue ordering."""

    AGENTS = ["ChatGPT", "Claude", "Gemini", "Grok"]
    PRIORITY = {"Claude": 1, "Grok": 2, "Gemini": 3, "ChatGPT": 4}

    def resolve(self) -> str:
        # Note: agent state directory is created on first use, not at import.
        agents_sorted = sorted(self.AGENTS, key=lambda a: self.PRIORITY.get(a, 99))
        result = {"queue": agents_sorted, "primary": agents_sorted[0]}
        print(json.dumps(result, indent=2))
        return result["primary"]

    def log_action(self, agent: str, action: str):
        os.makedirs(AGENT_DIR, exist_ok=True)
        log_path = os.path.join(AGENT_DIR, f"{agent}.log")
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(f"{action}\n")
