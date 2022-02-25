#!/usr/bin/python3

from contributors import Contributors

class Roles:

    def __init__(self, skillname, level):
        self.name_of_skill = skillname
        self.level = int(level)
        self.contributor = None

    def assign(self, contributor:Contributors):
        checkskill = self.name_of_skill in contributor.skill.keys()
        checklevel = checkskill and contributor.skill[self.name_of_skill] >= (self.level - 1)
        isassigned = self.contributor is None
        if checkskill and checklevel and isassigned:
            self.contributor = contributor
            return True
        return False
