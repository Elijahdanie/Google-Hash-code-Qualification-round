#!/usr/bin/python3

class Contributors:

    def __init__(self, name, skill):
        self.name = name
        self.skill = skill
        self.projects = {}
    
    def add_project(self, project):
        self.projects[project.name] = project
