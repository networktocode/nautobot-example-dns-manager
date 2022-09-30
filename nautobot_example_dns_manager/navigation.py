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
                        buttons=(
                            NavMenuAddButton(
                                link="plugins:nautobot_example_dns_manager:dnszonemodel_add",
                                permissions=[],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="plugins:nautobot_example_dns_manager:arecordmodel_list",
                        name="A Records",
                        permissions=[],
                        buttons=(
                            NavMenuAddButton(
                                link="plugins:nautobot_example_dns_manager:arecordmodel_add",
                                permissions=[],
                            ),
                        ),
                    ),
                    NavMenuItem(
                        link="plugins:nautobot_example_dns_manager:cnamerecordmodel_list",
                        name="CNAME Records",
                        permissions=[],
                        buttons=(
                            NavMenuAddButton(
                                link="plugins:nautobot_example_dns_manager:cnamerecordmodel_add",
                                permissions=[],
                            ),
                        ),
                    ),
                ),
            ),
        ),
    ),
)
