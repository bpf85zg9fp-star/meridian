import os


class KeyManager:
    """Simple environment-based key manager."""

    ENV_KEY = "MERIDIAN_KEY"

    def get_key(self) -> str:
        key = os.getenv(self.ENV_KEY)
        if not key:
            raise RuntimeError("Missing MERIDIAN_KEY environment variable")
        return key

    def rotate_hint(self) -> str:
        return "Rotate externally (recommended: secret manager)."
