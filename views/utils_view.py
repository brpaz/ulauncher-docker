"""
Utils View
Displays some utility tools for Managing Docker
"""

from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.RunScriptAction import RunScriptAction


class UtilsView():
    """ Display some Utils functions """

    def __init__(self, extension):
        self.extension = extension

    def execute(self):
        """ Render view """
        items = []
        data = [{
            'name':
            'Clean',
            'description':
            'Cleanup unusued Docker containers and images',
            'action':
            RunScriptAction("x-terminal-emulator -e docker system prune -a",
                            [])
        }]

        for item in data:
            items.append(
                ExtensionResultItem(icon='images/icon.png',
                                    name=item['name'],
                                    highlightable=False,
                                    description=item['description'],
                                    on_enter=item['action']))

        return RenderResultListAction(items)
