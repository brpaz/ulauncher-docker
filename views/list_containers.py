""" List containers """

from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.SetUserQueryAction import SetUserQueryAction


class ListContainersView():
    """ List containers view """

    def __init__(self, extension):
        self.extension = extension

    def execute(self, event, query, only_running=True):
        """ Lists the Containers """

        filters = {}

        if query:
            filters["name"] = query.lstrip('-a ')

        if only_running:
            filters["status"] = "running"

        containers = self.extension.docker_client.containers.list(
            filters=filters, limit=8)

        items = []
        for container in containers:
            items.append(
                ExtensionResultItem(
                    icon='images/icon.png',
                    name=container.name,
                    description=container.status,
                    on_enter=SetUserQueryAction(
                        "%s -c %s" %
                        (event.get_keyword(), container.short_id))))

        return RenderResultListAction(items)
