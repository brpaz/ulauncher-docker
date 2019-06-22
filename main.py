
"""
Ulauncher Docker Extension
Manage your Docker containers from Ulauncher
"""

import logging
import gi
import docker

from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.client.Extension import Extension
from gi.repository import Notify

from views import ListContainersView, ContainerDetailsView, InfoView, UtilsView
from utils import ArgumentParser
from utils.constants import *  # pylint: disable=wildcard-import

gi.require_version('Notify', '0.7')


LOGGING = logging.getLogger(__name__)


class DockerExtension(Extension):
    """ Extension entry point """

    def __init__(self):
        """ Initializes the extension """
        super(DockerExtension, self).__init__()
        self.docker_client = docker.from_env()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())

        parser = ArgumentParser()
        parser.add_argument('-c', '--c', action='store', dest='container_id')
        parser.add_argument('-a',
                            '--a',
                            action='store_true',
                            default=False,
                            dest='all_containers')
        parser.add_argument('-i',
                            '--i',
                            action='store_true',
                            default=False,
                            dest='info')

        self.arg_parser = parser

        self.list_containers_view = ListContainersView(self)
        self.container_details_view = ContainerDetailsView(self)
        self.info_view = InfoView(self)
        self.utils_view = UtilsView(self)

        Notify.init("DockerExtension")

    def show_notification(self, text):
        """
        Shows a notification
        Args:
          text (str): The text to display on the notification
        """
        Notify.Notification.new("Docker", text).show()

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
        except:  # pylint: disable=bare-except
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
        except:  # pylint: disable=bare-except
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
        except:  # pylint: disable=bare-except
            self.show_notification("Failed to restart container %s" %
                                   container_id)


class KeywordQueryEventListener(EventListener):
    """ Listener that handles the user input """

    # pylint: disable=unused-argument,no-self-use
    def on_event(self, event, extension):
        """ Handles the event """

        query = event.get_argument() or ""

        args, _ = extension.arg_parser.parse_known_args(query.split())

        if query.strip() == "utils":
            return extension.utils_view.execute()

        if args.info or query.strip() == "info":
            return extension.info_view.execute()

        if args.container_id is not None:
            return extension.container_details_view.execute(
                args.container_id)

        return extension.list_containers_view.execute(
            event, query, not args.all_containers)


class ItemEnterEventListener(EventListener):
    """ Listener that handles the click on an item """

    # pylint: disable=unused-argument,no-self-use
    def on_event(self, event, extension):
        """ Handles the event """
        data = event.get_data()

        if data['action'] == ACTION_RESTART_CONTAINER:
            LOGGING.info("Restarting container %s", data['id'])
            extension.restart_container(data['id'])

        if data['action'] == ACTION_STOP_CONTAINER:
            LOGGING.info("Stopping container %s", data['id'])
            extension.stop_container(data['id'])

        if data['action'] == ACTION_START_CONTAINER:
            LOGGING.info("Starting container %s", data['id'])
            extension.start_container(data['id'])


if __name__ == '__main__':
    DockerExtension().run()
