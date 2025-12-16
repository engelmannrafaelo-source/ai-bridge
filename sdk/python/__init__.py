"""AI-Bridge Client SDK - Smart URL Resolution with Optional Fallback."""

from .ai_bridge_client import (
    get_bridge_url,
    get_bridge_url_sync,
    get_bridge_url_or_default,
    initialize_bridge_url,
    is_initialized,
    create_client,
    health_check,
    HETZNER_URL,
    LOCAL_URL,
    AIBridgeConnectionError,
)

__all__ = [
    "get_bridge_url",
    "get_bridge_url_sync",
    "get_bridge_url_or_default",
    "initialize_bridge_url",
    "is_initialized",
    "create_client",
    "health_check",
    "HETZNER_URL",
    "LOCAL_URL",
    "AIBridgeConnectionError",
]

__version__ = "1.0.0"
