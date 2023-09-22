## PatientEducation

PatientEducation is a free educational platform designed for the prevention <br>
and rehabilitation of patients after a stroke. <br> The application is created
using Django and Python.

## Objective of the project

The goal of the project is to provide an accessible and personalized educational experience  <br>
for stroke patients and their loved ones. I believe that education and social <br>
support have an important role in the rehabilitation process. PatientEducation offers a platform <br>
where people can find educational materials and interact with other patients and professionals.


## Features

- List of courses: users can view the general list of courses and select the ones they need by category
- Course Tracking: users can view the courses they are registered for
- Educational materials: users can view different types of content module-by-module
- Course Creation: users with instructors rights can create courses and<br>
add text/images/videos to educational materials
- Online chat: for each course you can go to an online chat where patients can get support and share <br>
their experiences
 
![Example](/media/Preview.png)


## Getting Started

1. First create empty directory.

2. Next clone the repository from GitHub and switch to the new directory:

    `$ git clone git@github.com/USERNAME/{{ project_name }}.git`
3. Extract and move all files from docker_configuration into the root directory of your project.
4. Rename the directory PatientEducation to mededucation
5. Install docker 
6. Create file ".env" in {project_name}/mededucation with enviroment variable $DJANGO_SECRET_KEY
7. Run the command in the root folder terminal
`docker compose --env-file ./mededucation/.env up`
