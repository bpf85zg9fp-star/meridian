import os


class KeyManager:
    """Single source of truth for the HMAC signing key.

    The key is read from the MERIDIAN_KEY environment variable.
    In GitHub Actions, set this as a repository secret:
      Settings > Secrets and variables > Actions > New repository secret
      Name: MERIDIAN_KEY
      Value: <random 256-bit hex string, e.g. output of: openssl rand -hex 32>

    For production deployments, replace this class with VaultKMS (vault_kms.py)
    which delegates to AWS KMS, GCP KMS, or HashiCorp Vault.
    """

    ENV_KEY = "MERIDIAN_KEY"

    def get_key(self) -> str:
        key = os.getenv(self.ENV_KEY)
        if not key:
            raise RuntimeError(
                f"Missing required environment variable: {self.ENV_KEY}. "
                "Set it as a GitHub Actions repository secret."
            )
        return key

    def rotate_hint(self) -> str:
        return (
            f"To rotate: update the {self.ENV_KEY} GitHub Actions secret, "
            "then re-sign any existing event stores with the new key."
        )
