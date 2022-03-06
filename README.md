# Google-Hash-code-Qualification-round

## Introduction
Picture with four laptops and letters T E A M illustrating teamwork
Work is so much more fun when we are part of a team! By combining our different skills, we can be more creative, efficient and productive. And more importantly, when working together we share... not only pizzas, but also knowledge. We can learn from each other, improve our own skills and gain experience.

Teamwork is one of the main ingredients of Hash Code, especially in this challenge!

So, are you up for the challenge?

## Summary
You are given a list of contributors, who have already mastered various skills, and a list of projects with different skill requirements. Contributors can improve their skills by completing projects and can mentor each other to work is roles in which they couldn't succeed on their own. Your task is to assign contributors to project roles that fit their qualifications and maximize the score for completed projects.

## Problem description
### Contributors
There are N contributors. Each contributor has a name and one or more skills at a specific level (0,1,2,...). Not possessing a skill is equivalent to possessing a skill at level 0.

For example, three contributors could have the following skills:

Anna: Python level 3
Bob: C++ level 3
Maria: HTML level 4, CSS level 6
Three contributors and their skills, as described in the example above.
Projects
There are M projects. Each project is described by:

its name
the duration of the project in days (how long it takes to complete a project once it is started)
the score awarded for completing the project
the “best before” time in days – if the project last day of work is strictly before the indicated day, it earns the full score. If it’s late (that is, the project is still worked on during or after its "best before day"), it gets one point less for each day it is late, but no less than zero points. See also the example in the "Assignments" section below.
a list of roles for contributors working on the project
Each project has one or more roles that need to be filled by contributors. Each role requires one skill at a specific level, and can be filled by a single contributor. Each contributor can fill at most one role on a single project.

For example, a project called "WebServer" could have the following roles:

Role 0 requiring Python level 3
Role 1 requiring HTML level 1
Role 2 requiring CSS level 5
The 3 roles that need to be filled for project WebServer, as described in the example above.
Filling roles and mentorship
A contributor can be assigned to a project for a specific role (at most one role in a single project), if they either:

have the skill at the required level or higher; or
have the skill at exactly one level below the required level, only if another contributor on the same project (assigned to another role), has this skill at the required level or higher. In this case, the contributor will be mentored by their colleague :)
One contributor can mentor multiple people at once, including for the same skill. A contributor can mentor and be mentored by other contributors at the same time.

Not possessing a skill is equivalent to possessing a skill at level 0. So a contributor can work on a project and be assigned to a role with requirement C++ level 1 if they don’t know any C++, provided that somebody else on the team knows C++ at level 1 or higher.

[more info](https://codingcompetitions.withgoogle.com/hashcode/round/00000000008caae7/000000000098afc8)
