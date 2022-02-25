#!/usr/bin/python3

from contributors import Contributors
from project import Project


def load_Data(contributors, projects, filecontents=[]):
    """
    This reads the files and initialize them into
    their seperate classes
    """
    parsedata = {}
    cont = []
    projobj = []
    iterator = 0
    total = len(filecontents)
    track_cont = 0
    track_proj = 0
    while(iterator < total):
        if track_cont < contributors and track_proj == 0:
            line = filecontents[iterator]
            name, skillcount = line.split(' ')
            skillcount = int(skillcount)
            skills = {}
            for i in range(skillcount):
                skillname, level = filecontents[iterator + i + 1].split()
                skills[skillname] = int(level)
            iterator = iterator + skillcount
            track_cont = track_cont + 1
            con = Contributors(name, skills)
            cont.append(con)
        elif track_proj < projects and track_cont == contributors:
            line = filecontents[iterator]
            name, duration, score, best_before, skill_needed = line.split()
            skills = []
            skill_needed = int(skill_needed)
            for i in range(skill_needed):
                skills.append(filecontents[iterator + i + 1])
            iterator = iterator + skill_needed
            pro = Project(name, skills, duration, best_before, score)
            projobj.append(pro)
            track_proj = track_proj + 1
        iterator = iterator+1
    parsedata = {'contributors': cont, 'projects': projobj}
    return parsedata
