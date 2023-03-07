# Test Game Rock Paper Scissors for Anaconda

## How to run

1) Install requirements `pip3 install -r requirements.txt`
2) Run migrations `python3 manage.py migrate`
3) Run the application `python3 manage.py runserver`
4) Go to `http://<your_host>/8000` and play :)

## Developer notes

The game was implemented using `Django` framework, with django templating system.
Firstly I was thinking about creating a single page application with using modern
front-end frameworks such as Reach or Angular and started to implement backend with an
API first approach, but when I have seen that I am in a hurry and don't have enough time
I decided to go with django templating system and basic ajax.

Due to lack of time:
- The project didn't contain any tests
- Typing wasn't set
- It's not implemented as a SPA with modern front-end frameworks
- The API wasn't properly tested for corner cases and vulnerabilities
- Secrets wasn't moved to environment variables and left in git
- There is no authentication/validation and user management system
- Multiplayer wasn't implemented
- Not implemented game against CPU
- No pagination on some list objects
- Not used production database like PostgreSQL or others. Used sqlite for testing purposes