import random
import sys
from vikingsClasses import not0fun
from vikingsClasses import Saxon
from vikingsClasses import Viking
from vikingsClasses import War



random.randint(0,1000)


first_names = [
    'Alice', 'Bob', 'Charlie', 'David', 'Emily', 'Frank', 'Grace', 'Henry', 'Isabella', 'Jack',
    'Katherine', 'Liam', 'Mia', 'Noah', 'Olivia', 'Penelope', 'Quinn', 'Robert', 'Sophia', 'Thomas',
    'Ulysses', 'Victoria', 'William', 'Xander', 'Yasmine', 'Zachary', 'Abigail', 'Benjamin', 'Chloe',
    'Daniel', 'Emma', 'Finn', 'Gabriella', 'Henry', 'Isabelle', 'James', 'Katherine', 'Liam', 'Madison',
    'Noah', 'Olivia', 'Parker', 'Quinn', 'Rebecca', 'Samuel', 'Taylor', 'Ulysses', 'Violet', 'William',
    'Xander', 'Yasmine', 'Zachary'
]

thewar=War()
for i in range(100):
    A_viking = Viking(first_names[random.randint(0,len(first_names)-1)], random.randint(0,1000), random.randint(0,1000))
    A_saxon = Saxon(random.randint(0,1000), random.randint(0,1000))

    thewar.addViking(A_viking)
    thewar.addSaxon(A_saxon)
    print(f'Saxon health: {thewar.saxonArmy[i].health}  Viking health: {thewar.vikingArmy[i].health}')


while (len(thewar.vikingArmy) != 0 and len(thewar.saxonArmy) != 0):
    thewar.vikingAttack()
    thewar.saxonAttack()
    print(f'          VIKINGS: {len(thewar.vikingArmy)} SAXONS: {len(thewar.saxonArmy)}')


         

y="stuff;thing;junk;"
z = y.split(";")
print(z)