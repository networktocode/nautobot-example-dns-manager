"""Plugin declaration for nautobot_example_dns_manager."""
# Metadata is inherited from Nautobot. If not including Nautobot in the environment, this should be added
try:
    from importlib import metadata
except ImportError:
    # Python version < 3.8
    import importlib_metadata as metadata

__version__ = metadata.version(__name__)

from nautobot.extras.plugins import PluginConfig


class NautobotExampleDNSManagerConfig(PluginConfig):
    """Plugin configuration for the nautobot_example_dns_manager plugin."""

    name = "nautobot_example_dns_manager"
    verbose_name = "Nautobot Example DNS Manager"
    version = __version__
    author = "Network to Code, LLC"
    description = "Nautobot Example DNS Manager."
    base_url = "example-dns-manager"
    required_settings = []
    min_version = "1.4.0"
    max_version = "1.9999"
    default_settings = {}
    caching_config = {}


config = NautobotExampleDNSManagerConfig  # pylint:disable=invalid-name
