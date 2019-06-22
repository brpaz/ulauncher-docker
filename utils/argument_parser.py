""" Argument Parser """
import argparse


class ArgumentError(Exception):
    """ Exception with the argument parser fails """


class ArgumentParser(argparse.ArgumentParser):
    """ Override the Argument Parser to silently ignore errors """

    def error(self, message):
        raise ArgumentError(message)
