#!/usr/bin/python3

"""
This module contains the class Project
that has all the attributes for a Project
"""


from contributors import Contributors
from roles import Roles


class Project:

    def __init__(self, name, roles, duration, best_before, score):
        self.name = name
        self.roles = []
        self.skillmap = {}
        for i in roles:
            skillname, level = i.split()
            r = Roles(skillname, level)
            self.roles.append(r)
        self.duration = duration
        self.best_before = best_before
        self.score = score

    def Assign(self, contributor: Contributors = []):
        """
        Assigns Contributors to the project
        """
        for c in contributor:
            for r in self.roles:
                result = r.assign(c)
                if result  == c:
                    c.add_project(self)

    

    def render(self):
        """
        Prints out a copy
        of the Project Overview
        as pointed out in the submission file
        """
        submission = self.name + '\n'
        for r in self.roles:
            if r.contributor is not None:
                submission = submission + r.contributor.name
                submission = submission + ' '
        return submission
