""" List containers """

from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from dk.actions import ACTION_DETAIL_CONTAINER


class ListContainersView():
    """ List containers view """

    def __init__(self, extension):
        self.extension = extension

    def render(self, query, only_running=True):
        """ Lists the Containers """

        filters = {}

        if query:
            filters["name"] = query

        if only_running:
            filters["status"] = "running"

        containers = self.extension.docker_client.containers.list(
            filters=filters, limit=8)

        if not containers:
            return RenderResultListAction([
                ExtensionResultItem(
                    icon=self.extension.icon_path,
                    name='No containers found that match: {}'.format(query),
                    on_enter=HideWindowAction())
            ])

        items = []
        for container in containers:
            items.append(
                ExtensionResultItem(icon=self.extension.icon_path,
                                    name=container.name,
                                    description=container.status,
                                    on_enter=ExtensionCustomAction(
                                        {
                                            'action': ACTION_DETAIL_CONTAINER,
                                            'container_id': container.id
                                        },
                                        keep_app_open=True)))

        return RenderResultListAction(items)
