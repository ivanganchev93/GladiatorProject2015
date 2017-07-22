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

- First: Clone the repository<br/>
    git clone https://github.com/ivanganchev93/GladiatorTeamProject.git<br/>
    
- Second: Go to ./GladiatorTeamProject, create a virtual environment for the app and switch to it<br/>
    cd GladiatorTeamProject<br/>
    mkvirtualenv Spartacus<br/>
    workon Spartacus<br/>
    
- Third: Install the dependencies<br/>
    pip install -r requirements.txt<br/>
    
- Forth: Make the migrations, migrate, run the population script and launch the server<br/>
    cd GladiatorTeamProject<br/>
    python manage.py makemigrations Spartacus<br/>
    python manage.py migrate<br/>
    python populate_spartacus.py<br/>
    python manage.py runserver<br/>
    
- Fifth: Login<br/>
    Type the following in your web browser: 127.0.0.1:8000/Spartacus<br/>
    Register or login with the test account - username: test password: test<br/>
  
- Finally: Have Fun!<br/>
    This part is mandatory<br/>

### Screenshots

#### Avatar view
<img src = "GladiatorTeamProject/static/images/screenshot1.jpg" width= 600 height= 400>

#### Quests
<img src = "GladiatorTeamProject/static/images/screenshot2.jpg" width= 600 height= 400>

#### Battle
<img src = "GladiatorTeamProject/static/images/screenshot3.jpg" width= 600 height= 400>
