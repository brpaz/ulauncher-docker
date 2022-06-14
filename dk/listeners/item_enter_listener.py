import logging
from ulauncher.api.client.EventListener import EventListener
from dk.actions import ACTION_RESTART_CONTAINER, ACTION_STOP_CONTAINER, ACTION_START_CONTAINER, ACTION_DETAIL_CONTAINER

logger = logging.getLogger(__name__)


class ItemEnterEventListener(EventListener):
    """ Listener that handles the click on an item """

    # pylint: disable=unused-argument,no-self-use
    def on_event(self, event, extension):
        """ Handles the event """
        data = event.get_data()

        if data['action'] == ACTION_RESTART_CONTAINER:
            logger.info("Restarting container %s", data['id'])
            extension.restart_container(data['id'])

        if data['action'] == ACTION_STOP_CONTAINER:
            logger.info("Stopping container %s", data['id'])
            extension.stop_container(data['id'])

        if data['action'] == ACTION_START_CONTAINER:
            logger.info("Starting container %s", data['id'])
            extension.start_container(data['id'])

        if data['action'] == ACTION_DETAIL_CONTAINER:
            return extension.show_container_details(data['container_id'])
