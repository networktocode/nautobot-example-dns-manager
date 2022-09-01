"""Plugin declaration for nautobot_dns_manager."""
# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
try:
    from importlib import metadata
except ImportError:
    # Python version < 3.8
    import importlib_metadata as metadata

__version__ = metadata.version(__name__)

from nautobot.extras.plugins import PluginConfig


class NautobotDNSManagerConfig(PluginConfig):
    """Plugin configuration for the nautobot_dns_manager plugin."""

    name = "nautobot_dns_manager"
    verbose_name = "Nautobot DNS Manager"
    version = __version__
    author = "Network to Code, LLC"
    description = "Nautobot DNS Manager."
    base_url = "dns-manager"
    required_settings = []
    min_version = "1.2.0"
    max_version = "1.9999"
    default_settings = {}
    caching_config = {}


config = NautobotDNSManagerConfig  # pylint:disable=invalid-name
