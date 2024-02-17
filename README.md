# Backend for HawkPhish Extension

## Frontend Resources

**Reference 2024 Frontend Extension:** [SecurityWebScanner](https://github.com/IPRO497-HawkPhish/SecurityWebScanner/tree/main)

**Reference 2023 Frontend Extension:** [SecurityWebScanner (Legacy)](https://github.com/JohnDeifel/SecurityWebScanner)

## General Steps and Rules

*Do not work on main...* That is bad practice and if you push changes that break something it can be hard to figure out. Make your own branch with:

`git switch -c <branch_name>`

You need to generate *your own* secret key for which you need to install django (search up how to do that for your OS) and generate your secret key:

`python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`

Now you need to create a file inside the root project dir:

`touch .env`

install an environment library:

`pip install python-dotenv`

and add these two things inside the file:

`DJANGO_SECRET_KEY='<your_secret_key'
DEBUG='True'`

To start the django server:

`cd <project_dir>
python3 manage.py migrate
python3 manage.py runserver`

This will open a local connection on port 8000, you might need to add firewall rules to allow this and you can work real-time (changes made live) on this as long as you dont close that connection.

Once you are certain your changes are good and work as intended you can commit your changes on a test branch, push test branch changes so they're live on github, and then follow these general steps to make a merge request:

`git checkout main
git pull
git merge <test_branch>`

resolve conflicts if any and then:

`git commit -am "Merge changes from <test_branch> into main"
git push origin main`
