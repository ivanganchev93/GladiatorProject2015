from Spartacus.models import User, Avatar, AvatarItem, Item
from random import randint

def fight(you, opponent):
    fightData={}
    rounds=[]
    try:
        # items that are equiped
        yourItems = AvatarItem.objects.filter(avatar = you, equiped = True)
        opponentItems = AvatarItem.objects.filter(avatar = opponent, equiped = True)


        youAttack = you.attack
        youDeffence = you.deffence
        opponentAttack = opponent.attack
        opponentDeffence = opponent.deffence

        # update attack and defence
        for item in yourItems:
            youAttack += item.item.attack
            youDeffence += item.item.deffence
        for item in opponentItems:
            opponentAttack += item.item.attack
            opponentDeffence += item.item.deffence

        # both gladiators start the fight with 100 health
        youHealth = you.strength*25
        opponentHealth = you.strength*25

        # the hit chance depends on the intelligence
        hitRatio = (you.intelligence + opponent.intelligence) * 1.0
        youHitChance = (you.intelligence / hitRatio) * 100 # in percentages
        opponentHitChance = (opponent.intelligence / hitRatio) * 100  # in percentages

        # chance of double hit depends on the agility and the initial hit chance
        doubleHitRatio = (you.agility + opponent.agility) * 1.0
        youDoubleHitChance = (youHitChance * (you.agility / doubleHitRatio))
        opponentDoubleHitChance = (opponentHitChance * (opponent.agility / doubleHitRatio))

        # damage
        if(youAttack > opponentDeffence):
            youDamageFactor = youAttack - opponentDeffence
        else:
            youDamageFactor = 5

        if(opponentAttack > youDeffence):
            opponentDamageFactor = opponentAttack - youDeffence
        else:
            opponentDamageFactor = 5

        round = 1
        while youHealth > 0 and opponentHealth > 0 and round <= 20:
            youDamage = 0
            youCritical = 0
            opponentDamage = 0
            opponentCritical = 0

            if randint(0,100) <= int(youHitChance):
                youDamage = youDamageFactor * ((randint(85,125))/100.0)
                opponentHealth -= youDamage

            if randint(0,100) <= int(youDoubleHitChance):
                youCritical = (youDamageFactor * ((randint(85,125))/100.0)) * 2
                opponentHealth -= youCritical

            if randint(0,100) <= int(opponentHitChance):
                opponentDamage = opponentDamageFactor * ((randint(85,125))/100.0)
                youHealth -= opponentDamage

            if randint(0,100) <= int(opponentDoubleHitChance):
                opponentCritical = (opponentDamageFactor * ((randint(85,125))/100.0)) * 2
                youHealth -=  opponentCritical

            rounds.append({'youDamage': youDamage, 'opponentHealth': opponentHealth, 'youCritical': youCritical,
                           'youHealth': youHealth, 'opponentDamage': opponentDamage,
                           'opponentCritical': opponentCritical, 'roundN': round})
            round+=1

        fightData["rounds"]=rounds
        fightData["stats"]={}

        #victory
        if youHealth - opponentHealth > 50:
            you.points += 50
            you.victories += 1

            cashWon = opponent.cash / 10.0  # 10% of the opponent's cash
            you.cash += cashWon + 30  #30 cash extra for a victory
            opponent.cash -= cashWon
            opponent.points += 20

            #updating stats
            you.attack += 2
            you.deffence += 2
            you.strength += 2
            you.agility += 2
            you.intelligence += 1
            fightData["stats"]["attack"]=2
            fightData["stats"]["deffence"]=2
            fightData["stats"]["strength"]=2
            fightData["stats"]["agility"]=2
            fightData["stats"]["intelligence"]=1

            you.save()
            opponent.save()
            fightData['result']=1

            return fightData

        #defeat
        elif youHealth - opponentHealth < -50:
            #updating stats
            you.attack += 1
            you.deffence += 1
            you.points += 20
            you.save()
            opponent.victories += 1
            opponent.points += 50
            opponent.save()

            fightData["stats"]['result']=-1
            fightData["stats"]["attack"]=1
            fightData["stats"]["deffence"]=1
            fightData["stats"]["points"]=20
            fightData['result']=-1
            return fightData
        
        #tie
        else:
            #updating stats
            you.attack += 1
            you.deffence += 1
            you.strength += 1
            you.agility += 1
            you.points += 30
            opponent.points += 30
            opponent.save()
            you.save()

            fightData["stats"]["attack"]=1
            fightData["stats"]["deffence"]=1
            fightData["stats"]["strength"]=1
            fightData["stats"]["agility"]=1
            fightData["stats"]["points"]=30
            fightData['result']=0

            return fightData
    except:
        print "Query fail battle"
