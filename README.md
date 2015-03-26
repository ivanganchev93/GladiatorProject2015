# Spartacus

Browser based RPG game, where you can fight on the arena <br/>
with other gladiators. You can equip your gladiator with <br/>
authentic ancient weapons, get stronger and become the best <br/>
among the gladiators.

The app can be found [Here] (http://spartacus.pythonanywhere.com)

### Features
- Items that can be equipped and unequipped
- Inventory for the items
- Market to buy and sell items
- Arena where you can fight with other gladiators
- Quests - another way for earning gold and stats.

### Installation instructions

- First: Clone the repository
    git clone https://github.com/2087690alexCh/GladiatorTeamProject.git
    
- Second: Create a virtual environment for the app and switch to it
    $ mkvirtualenv Spartacus
    $ workon Spartacus
    
- Third: Install the dependencies
    $ pip install -r requirements.txt
    
- Forth: Run the population script and launch the server
    $ python populate_spartacus
    $ python manage.py runserver
    
- Fifth: Login
    Type the following in your web browser: 127.0.0.1:8000/Spartacus
    Register or login with the test account - username: test password: test
  
- Finally: Have Fun!
    This part is mandatory

### Screenshots

#### Avatar view
<img src = "GladiatorTeamProject/static/images/screenshot1.jpg" width= 600 height= 400>

#### Quests
<img src = "GladiatorTeamProject/static/images/screenshot2.jpg" width= 600 height= 400>

#### Battle
<img src = "GladiatorTeamProject/static/images/screenshot3.jpg" width= 600 height= 400>
