# Welcome to Erica Tubbs' final project for IS601.
#
# ----- INTRODUCTION -----
#
# This is a web application built with FastAPI, SQLAlchemy, and Tailwind
# that performs calculations, supports login registration, and
# calculation history. Built using Python.
#
# Features of this calculator include calculations, BREAD
# operations, user profiles, password change, authentication,
# and a dashboard.
#
# Technologies used in this project include Python/FastAPI,
# SQLAlchemy, Jinja Templates, Docker, pytest, Playwright,
# and more.
#
# ----- INSTRUCTIONS -----
#
# To use this application with Python, activate a venv and install
# the required dependencies with "pip install -r requirements.txt". 
# Then run "uvicorn app.main:app --reload" and visit
# http://127.0.0.1:8000 in your browser.
#
# To use this application with Docker, build the container
# using "docker compose up --build" and visit 
# http://127.0.0.1:8000 in your browser.
#
# ----- ADDED FEATURE -----
#
# For this project, I decided to add "Change Password" as
# the new feature. You can view the navigation for this feature 
# near the "Logout" button in the applications's UI.
#
# ----- REFLECTION -----
# This project taught me that it is not a simple process to add
# a seemingly simple feature to a web application. There are 
# many elements involved, such as developing the logic, building 
# the backend, building the front-end, integrating the two, 
# writing testing, routing the paths, validating input for the
# database, and more. There is a reason company websites are run
# by teams of people - it's a lot of layered elements to manage.
#
# I found it difficult not only to determine what code needed to
# be added where, but simply to just keep track of what stage 
# of developing the feature I was in, what stage came next, and 
# what still was yet to be done. I found myself constantly referring
# to and maintaining a list of all the elements involved in adding
# the password change feature. It felt overwhelming, especially
# coming in with little to none programming experience.
#
# The next time I tackle a project like this, I would create a separate
# changelog of everything I was working on in detail. This would make
# stepping away from the project and returning much easier, as I would
# be less likely to lose track of where I was, what I was doing, and
# what the next steps were. A detailed changelog would also help
# me in troubleshooting. If I added code that broke another part of the 
# application, I could visit the changelog to quickly discover
# what to change or undo. Though pytest and git are helpful for this as
# well, I think a changelog would make it much clearler for me.
#
# Implementing a new feature into this program really forced me to
# learn how to read and understand code, understand the structure
# of a complex program, and engage with new concepts like routing,
# database management, and integration testing. 
#
# If I had to choose two things as my big takeaways from this course,
# it would be this:
# 1. There are numerous amounts of tools out there already created
# to help you program more efficiently, to add new features to your 
# application, or to streamline your code. It can feel overwhelming
# to have so many options, but it's important to persevere. I don't need
# to fully understand a library and all of its capabilities to use it.
# 2. Part of being a programmer is largely debugging and troubleshooting
# errors. Code will rarely work on the "first try", so being able to use
# testing, read error codes (or pytest failures!), and have patience 
# are invaluable skills.
#
# Thank you for everything, Professor!
#
# ----- DISCLAIMER -----
#
# This application is a school project and not meant for public/
# commercial use. 