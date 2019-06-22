"""
Docker client
"""


class Client:
    """ Class that interacts with Docker API """

    def __init__(self, docker_client):
        """ Constructor method """
        self.docker_client = docker_client
