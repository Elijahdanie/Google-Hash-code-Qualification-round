#!/usr/bin/python3

"""
This module contains the class Contributor
with its attributes
"""


class Contributors:

    def __init__(self, name, skill):
        self.name = name
        self.skill = skill
        self.projects = {}

    def add_project(self, project):
        """
        Adds a project assigned to this
        Contributor
        """
        self.projects[project.name] = project
