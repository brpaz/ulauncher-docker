"""
Ulauncher Docker Extension
Manage your Docker containers from Ulauncher
"""

import logging
import gi
import docker
import subprocess
from gi.repository import Notify
from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem

from dk.listeners.query_listener import KeywordQueryEventListener
from dk.listeners.item_enter_listener import ItemEnterEventListener
from dk.views.container_details import ContainerDetailsView
from dk.views.info import InfoView
from dk.views.list_containers import ListContainersView

gi.require_version('Notify', '0.7')

logger = logging.getLogger(__name__)


class DockerExtension(Extension):
    """ Extension entry point """

    def __init__(self):
        """ Initializes the extension """
        super(DockerExtension, self).__init__()
        self.docker_client = docker.from_env()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())

        self.icon_path = 'images/icon.png'
        self.list_containers_view = ListContainersView(self)
        self.container_details_view = ContainerDetailsView(self)
        self.info_view = InfoView(self)

        Notify.init("DockerExtension")

    def show_notification(self, text):
        """
        Shows a notification
        Args:
          text (str): The text to display on the notification
        """
        Notify.Notification.new("Docker", text).show()

    def show_docker_info(self):
        """ Shows Docker daemon information"""
        return self.info_view.render()

    def list_containers(self, query):
        """ Lists running containers"""
        return self.list_containers_view.render(query)

    def show_container_details(self, container_id):
        """ Show the details of the container with the specified id"""
        return self.container_details_view.render(container_id)

    def start_container(self, container_id):
        """
        Starts the container with the specified id
        Args:
          container_id (str): The container id
        """
        try:
            self.docker_client.containers.get(container_id).start()
            self.show_notification("Container %s started with success" %
                                   container_id)
        except Exception as e:
            logger.error("Failed to start container {}", e)
            self.show_notification("Failed to start container %s" %
                                   container_id)

    def stop_container(self, container_id):
        """
        Stops the container with the specified id
        Args:
          container_id (str): The container id
        """
        try:
            self.docker_client.containers.get(container_id).stop()
            self.show_notification("Container %s stopped with success" %
                                   container_id)
        except Exception as e:
            logger.error("Failed to stop container {}", e)
            self.show_notification("Failed to stop container %s" %
                                   container_id)

    def restart_container(self, container_id):
        """
        Restarts the container with the specified id
        Args:
          container_id (str): The container id
        """
        try:
            self.docker_client.containers.get(container_id).restart()
            self.show_notification("Container %s restarted with success" %
                                   container_id)
        except Exception as e:
            logger.error("Failed to restart container {}", e)
            self.show_notification("Failed to restart container %s" %
                                   container_id)

    def prune(self):
        """ Run docker system prune command"""
        try:
            output = subprocess.run(
                ["docker", "system", "prune", "-a", "-f"],
                check=True,
                capture_output=True,
                text=True,
            )
            self.show_notification("Prune completed successfully: %s" %
                                   output.stdout)
            return HideWindowAction()
        except Exception as e:
            self.show_notification("Prune command failed with error: %s" % e)

    def search_documentation(self, query):
        """ Searches on https://docs.docker.com """
        return RenderResultListAction([
            ExtensionResultItem(
                icon=self.icon_path,
                name="Press enter to search for %s" % query,
                highlightable=False,
                on_enter=OpenUrlAction("https://docs.docker.com/search/?q=%s" %
                                       str(query)))
        ])
