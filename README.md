# Backend for HawkPhish Extension

## Frontend Resources

Reference 2024 Frontend Extension: [SecurityWebScanner](https://github.com/IPRO497-HawkPhish/SecurityWebScanner/tree/main)

Reference 2023 Frontend Extension: [SecurityWebScanner (Legacy)](https://github.com/JohnDeifel/SecurityWebScanner)

## MR and workflow

***Do not work on main...*** That is bad practice and if you push changes that break something it can be hard to figure out. Make your own branch with:
```
git pull
git checkout -b <test_branch>
```
When ready with your changes and they work locally, commit and push changes:
```
git commit -am "message"
git push -u origin <test_branch>
```
Merge request (MR) to main:
```
git checkout main
git pull origin main
git merge <test_branch>`
```
There should be an approval request so wait, if not after resovling conflicts:
```
git push origin main
```

## Local Testing

You need to generate *your own* secret key for which you need to install django (search up how to do that for your OS) and generate your secret key:
```
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`
```
Now you need to create a file inside the root project dir:
```
touch .env
```
Install an environment library:
```
pip install python-dotenv
```
Add these two things inside the file `.env`:
```
DJANGO_SECRET_KEY='<your_secret_key'
DEBUG='True'
```
Lastly, to start the django server:
```
cd <project_dir>
python3 manage.py migrate
python3 manage.py runserver
```
This will open a local connection on port 8000, you might need to add firewall rules to allow this and you can work real-time (changes made live) on this as long as you dont close that connection.
