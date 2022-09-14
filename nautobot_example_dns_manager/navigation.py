"""Nautobot Example DNS Manager Navigation."""

from nautobot.core.apps import NavMenuAddButton, NavMenuGroup, NavMenuItem, NavMenuImportButton, NavMenuTab

menu_items = (
    NavMenuTab(
        name="IPAM",
        groups=(
            NavMenuGroup(
                name="DNS",
                weight=150,
                items=(
                    NavMenuItem(
                        link="plugins:nautobot_example_dns_manager:dnszonemodel_list",
                        name="DNS Zones",
                        permissions=[],
                    ),
                    NavMenuItem(
                        link="plugins:nautobot_example_dns_manager:records",
                        name="DNS Records",
                        permissions=[],
                    ),
                ),
            ),
        ),
    ),
)