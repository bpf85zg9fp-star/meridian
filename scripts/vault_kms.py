import os
import base64
import hashlib
from dataclasses import dataclass


@dataclass
class VaultKey:
    key_id: str
    key_material: bytes


class VaultKMS:
    """Minimal Vault/KMS abstraction layer.

    This is a structural interface intended to be replaced by:
    - HashiCorp Vault
    - AWS KMS
    - GCP KMS

    Current implementation is local-only and deterministic.
    """

    ENV_PRIMARY_KEY = "MERIDIAN_VAULT_KEY"

    def __init__(self):
        self._cache = {}

    def get_primary_key(self) -> VaultKey:
        raw = os.getenv(self.ENV_PRIMARY_KEY)
        if not raw:
            raise RuntimeError("Missing MERIDIAN_VAULT_KEY environment variable")

        key_bytes = base64.b64decode(raw.encode("utf-8")) if self._is_base64(raw) else raw.encode("utf-8")

        return VaultKey(
            key_id="primary",
            key_material=key_bytes
        )

    def derive_key(self, salt: str) -> bytes:
        base = self.get_primary_key().key_material
        return hashlib.pbkdf2_hmac(
            "sha256",
            base,
            salt.encode("utf-8"),
            200000
        )

    def _is_base64(self, value: str) -> bool:
        try:
            base64.b64decode(value.encode("utf-8"))
            return True
        except Exception:
            return False

    def rotate_notice(self) -> str:
        return "Key rotation must be performed via external KMS/Vault system."
