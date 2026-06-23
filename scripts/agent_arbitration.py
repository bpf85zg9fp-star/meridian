import json
import os
from datetime import datetime, timezone

QUEUE_PATH = os.path.join("agents", "queue.jsonl")

os.makedirs("agents", exist_ok=True)

class AgentArbitration:
    def __init__(self):
        self.queue_path = QUEUE_PATH

    def enqueue(self, agent_id, target_path, operation, priority=0):
        entry = {
            "agent_id": agent_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "target_path": target_path,
            "operation": operation,
            "priority": priority,
            "status": "queued"
        }

        with open(self.queue_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")

        return entry

    def load_queue(self):
        if not os.path.exists(self.queue_path):
            return []

        items = []
        with open(self.queue_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    items.append(json.loads(line))
        return items

    def resolve(self):
        """Simple deterministic resolution: highest priority first, FIFO tie-break."""
        queue = self.load_queue()
        queue.sort(key=lambda x: (-x["priority"], x["timestamp"]))

        resolved = []
        locked_paths = set()

        for item in queue:
            if item["target_path"] in locked_paths:
                item["status"] = "rejected"
            else:
                item["status"] = "granted"
                locked_paths.add(item["target_path"])
                resolved.append(item)

        return resolved
