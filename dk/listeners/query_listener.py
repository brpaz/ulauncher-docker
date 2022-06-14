from ulauncher.api.client.EventListener import EventListener


class KeywordQueryEventListener(EventListener):
    """ Listener that handles the user input """

    # pylint: disable=unused-argument,no-self-use
    def on_event(self, event, extension):
        """ Handles the event """

        query = event.get_argument() or ""
        kw = self.get_keyword_id(extension, event.get_keyword())

        if kw == "kw_info":
            return extension.show_docker_info()

        if kw == "kw_prune":
            return extension.prune()

        if kw == "kw_documentation":
            return extension.search_documentation(query)

        return extension.list_containers(query)

    def get_keyword_id(self, extension, keyword):
        """ Returns the keyword ID from the keyword name """
        kw_id = None
        for key, value in extension.preferences.items():
            if value == keyword:
                kw_id = key
                break

        return kw_id
