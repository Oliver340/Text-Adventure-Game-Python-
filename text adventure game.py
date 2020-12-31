#BY BOB and OLIVER
import time, random
def fight(enemy):
    global hp
    while enemies[enemy] > 0:
        print('\nEnemy HP: '+str(enemies[enemy]))
        print('Your HP: '+str(hp) + '\n')
        if inv['Chicken'] == 0 and inv['Cooked Chicken'] == 0 and inv['Cake'] == 0:
          choice = input('A: Attack\nB: You have no food.\n')
        elif inv['Chicken'] == 1:
          choice = input('A: Attack\nB: Heal 60 HP with your chicken.\n')
        elif inv['Cooked Chicken'] == 1:
          choice = input('A: Attack\nB: Heal 80 HP with your cooked chicken.\n')
        elif inv['Cake'] == 1:
          choice = input('A: Attack\nB: Heal 70 HP with your cake.\n')
          
        if str.lower(choice)=='inventory':
          inventory(inv)
          continue
        if str.lower(choice) == 'a' and inv['Sword']>=2:
            dmg = random.randint(45,55)
            print('You attack with both of your swords, dealing ' + str(dmg) + ' points of damage.')
            enemies[enemy] -= dmg  
        elif str.lower(choice) == 'a' and inv['Sword']==1:
            dmg = random.randint(20,30)
            print('You attack with your sword, dealing ' + str(dmg) + ' points of damage.')
            enemies[enemy] -= dmg
        elif str.lower(choice) == 'a':
            dmg = random.randint(10,20)
            print('You attack with your fists, dealing ' + str(dmg) + ' points of damage.')
            enemies[enemy] -= dmg
        elif str.lower(choice) == 'b' and inv['Chicken']:
            print('You eat your Chicken and replenish 60 HP')
            inv['Chicken'] -= 1
            hp += 60
            if hp>100:
                hp=100
        elif str.lower(choice) == 'b' and inv['Cooked Chicken']:
            print('You eat your Cooked Chicken and replenish 80 HP')
            inv['Cooked Chicken'] -= 1
            hp += 80
            if hp>100:
                hp=100
        elif str.lower(choice) == 'b' and inv['Cake']:
            print('You eat your Cake and replenish 70 HP')
            inv['Cake'] -= 1
            hp += 70
            if hp>100:
                hp=100
        elif str.lower(choice) == 'b':
          continue
        if enemies[enemy] <= 0:
          print('You defeated '+ str(enemy) + '\n')
          time.sleep(2)
          break
        if enemies[enemy] > 0 and str(enemy)=='Guard':
          dmg = random.randint(20,30)
          print(str(enemy)+' hit you for ' + str(dmg) + ' points of damage')
          hp -= dmg
        if enemies[enemy] > 0 and str(enemy)=='Bear':
          dmg = random.randint(45,55)
          print(str(enemy)+' hit you for ' + str(dmg) + ' points of damage')
          hp -= dmg
        if enemies[enemy] > 0 and str(enemy)=='Bear Cub':
          dmg = random.randint(25,35)
          print(str(enemy)+' hit you for ' + str(dmg) + ' points of damage')
          hp -= dmg
        if hp <= 0:
          break

def africanamericansmith():
    global hp,annoyed
    print('You are in the blacksmith\'s quarters.\nYou see a blacksmith with a key looped around his belt. You notice he is hard at work smithing at incredible speeds. He most likely won\'t see you reach for it.\n')
    time.sleep(3)
    while True:
        choice=input('A:Grab the key\nB:Talk to him\nC:Leave\n')

        if str.lower(choice)=='inventory':
          inventory(inv)
          continue

        if str.lower(choice) == 'a':
            chance=random.randint(1,2)
            if inv['Key']>= 1:
                print('You already have the key.\n')
            elif chance==2:
                print('He notices that you were reaching for his key and is insulted. He swats your hand away.\n')
                annoyed = True
            elif chance==1:
                print(r""" .--.
/.-. '----------.
\'-' .--"--""-"-'
 '--'""")
                print('You successfully take the key.\n')
                inv['Key'] += 1
        elif str.lower(choice) == 'b' and annoyed == False:
            dialogue('Andre: Hi I\'m Andre, what can I help you with?\n\n')
            choice=input('A: Buy a sword(5 Gold)\nB: Ask for his key\n')

            if str.lower(choice)=='inventory':
              inventory(inv)
              continue

            if str.lower(choice) == 'a' and inv['Gold']>=5:
                if inv['Sword'] == 0:
                  print(r'''         />_________________________________
[########[]_________________________________>
         \>''')
                elif inv['Sword'] == 1:
                  print(r'''/\                    /\
\ \                  / /
 \ \                / /
  \.\              /./
   \.\            /./
    \.\          /./
     \\\        ///
      \.\      /./
       \.\    /./
        \.\__/./
       _/)))(((\_
       \|)\##/(|/
       _|)/##\(|_
       \|)))(((|/
        /o/  \o\
       /o/    \o\
      /_/      \_\ ''')
                print('YOU OBTAINED A SWORD\n')
                inv['Gold'] -= 5
                inv['Sword'] += 1
            elif str.lower(choice) == 'b' and inv['Key'] <= 0:
                print(""" .--.
/.-. '----------.
\'-' .--"--""-"-'
 '--'""")
                print('YOU OBTAINED A KEY\n')
                inv['Key'] += 1
            else:
                print('You cannot do that.\n')
        elif str.lower(choice) == 'c':
            break
        elif annoyed == True and str.lower(choice) == 'b':
            print('He is mad at you and refuses to talk.\n')
        else:
            print('You cannot do that.\n')
def kitchen():
    global burnt
    print('You enter the kitchen. It\'s empty, although there is a closed pantry on your left and next to it a furnace. What do you do?\n')
    while True:
        choice = input('A: Check the pantry\nB: Check the furnace\nC: Leave the kitchen\n')

        if str.lower(choice)=='inventory':
          inventory(inv)
          continue

        while str.lower(choice) not in ['a','b','c']:
            choice = input('A: Check the pantry\nB: Check the furnace\nC: Leave the kitchen\n')

            if str.lower(choice)=='inventory':
              inventory(inv)
              continue

        if str.lower(choice) == 'a':
            if inv['Chicken'] == 0 and inv['Cooked Chicken'] == 0 and inv['Cake'] == 0 and burnt == False:
                print('You look in the pantry, and inside there is a chicken and a cake. You only have enough room to hold one.\n')
                choice = input('A: Take the chicken\nB: Take the cake\n')

                if str.lower(choice)=='inventory':
                  inventory(inv)
                  continue
                  
                while str.lower(choice) not in ['a','b']:
                    choice = input('A: Take the chicken\nB: Take the cake\n')

                    if str.lower(choice)=='inventory':
                      inventory(inv)
                      continue

                if str.lower(choice) == 'a':
                    print(r''' MM
<' \___/|
  \_  _/
    ][
''')
                    print('You decide to take the chicken.\n')
                    inv['Chicken'] = 1
                if str.lower(choice) == 'b':
                    print(r'''            (        (
             ( )      ( )          (
      (       Y        Y          ( )
     ( )     |"|      |"|          Y
      Y      | |      | |         |"|
     |"|     | |.-----| |---.___  | |
     | |  .--| |,~~~~~| |~~~,,,,'-| |
     | |-,,~~'-'___   '-'       ~~| |._
    .| |~       // ___            '-',,'.
   /,'-'     <_// // _  __             ~,\
  / ;     ,-,     \\_> <<_' ____________;_)
  | ;    {(_)} _,      ._>>`'-._          |
  | ;     '-'\_\/>              '-._      |
  |\ ~,,,      _\__            ,,,,,'-.   |
  | '-._ ~~,,,            ,,,~~ __.-'~ |  |
  |     '-.__ ~~~~~~~~~~~~ __.-'       |__|
  |\         `'----------'`           _|
  | '=._                         __.=' |
  :     '=.__               __.='      |
   \         `'==========='`          .'
    '-._                         __.-'
        '-.__               __.-'
             `'-----------'`''')
                    print('You decide to take the cake.\n')
                    inv['Cake'] = 1
            elif (inv['Chicken'] == 1 or inv['Cooked Chicken'] == 1) and burnt == False:
                print('You look in the pantry, and inside there is a cake. You don\'t have enough room to take it.\n')
                continue
            elif inv['Cake'] == 1:
                print('You look in the pantry, and inside there is a chicken. You don\'t have enough room to take it.\n')
                continue
            elif (inv['Chicken'] == 1 or inv['Cooked Chicken'] == 1) and burnt == True:
                print('You look in the pantry but it is empty.\n')
                continue
            elif inv['Chicken'] == 0 and inv['Cooked Chicken'] == 0 and burnt == True:
                print(r''' MM
<' \___/|
  \_  _/
    ][
''')
                print('You look in the pantry, and inside there is a chicken. You decide to take it.\n')
                inv['Chicken'] = 1
        elif str.lower(choice) == 'b':
            if inv['Chicken'] == 0 and inv['Cake'] == 0:
                if burnt == False:
                    print('There\'s nothing here. It\'s just a furnace.\n')
                elif burnt == True:
                    print('There\'s nothing here, other than the remains of a cake and a strong smell of vanilla.\n')
                continue
            if inv['Chicken'] == 1 or inv['Cake'] == 1:
                print('Would you like to use the furnace to cook your food?\n')
                choice = input('A: Yes\nB: No\n')

                if str.lower(choice)=='inventory':
                  inventory(inv)
                  continue

                while str.lower(choice) not in ['a','b']:
                    choice = input('A: Yes\nB: No\n')

                    if str.lower(choice)=='inventory':
                      inventory(inv)
                      continue

                if str.lower(choice) == 'a':
                    if inv['Chicken'] == 1:
                        print(r'''    \ \ \
 MM / / /
<* \___/|
  \_  _/
    ][
''')
                        print('You cooked the chicken. It looks more tasty now.\n')
                        inv['Chicken'] = 0
                        inv['Cooked Chicken'] = 1
                    if inv['Cake'] == 1:
                        print('You put your cake in the furnace and it melts down to a pool of icing. Why would you put a cake in a furnace?\n')
                        inv['Cake'] = 0
                        burnt = True
        elif str.lower(choice) == 'c':
          break

def dialogue(text):
    for char in text:
        print(char, end='')
        time.sleep(0.04)
def inventory(inv):
  if sum(inv.values()) == 0:
    print('You have nothing.\n')
    return
  for key,value in inv.items():
    if value > 0:
      print(key+':',str(value))
  print('')
  
while True:
  inv = {'Needle':0,'Gold':0,'Key':0,'Chicken':0,'Cooked Chicken':0,'Cake':0,'Sword':0}
  enemies = {'Guard':100,'Bear':300,'Bear Cub':200}
  hp = 100
  x = 32
  annoyed = False
  burnt = False
  name = str(input('Hello player. What is your name?\n'))
  time.sleep(1)
  print('Welcome to The Legend of ' + name + '!')
  time.sleep(1)
  print('Type "inventory" at any time to check your inventory.')
  time.sleep(3)
  for i in range(69):
    print('\n')
  print('You wake up half-naked in the back of a horse-drawn wagon, with a headache.')
  print(''' |___________|________________,,;;;`;     
  |,-. -|- ,-|        ,~(  )  , )~~\|       
  ( o )----( o )      \' / / --`--,         
  `-\'      `-\'        /  \    | \'  \n''')
  time.sleep(1)
  dialogue('''Prisoner: Hey you, you\'re finally awake. You were trying to cross the border,
right? Walked right into that Imperial ambush, same as us, and that thief over there.\n\n''')
  time.sleep(1)
  print('You are approaching a gated castle where you will be held prisoner in the dungeon.\n')
  print('''                                      ,.=,,==. ,,_
                        _ ,====, _   |I|`` ||  `|I `|
                      |`I|    || `==,|``   ^^   ``  |
                      | ``    ^^    ||_,===TT`==,,_ |
                      |,==Y``Y==,,__| \L=_-`'   +J/`
                        \|=_  ' -=#J/..-|=_-     =|
                        |=_   -;-='`. .|=_-     =|----T--,
                        |=/\  -|=_-. . |=_-/^\  =||-|-|::|____
                        |=||  -|=_-. . |=_-| |  =|-|-||::\____
                        |=LJ  -|=_-. . |=_-|_| =||-|-|:::::::
                        |=_   -|=_-_.  |=_-     =|-|-||:::::::
                        |=_   -|=//^\. |=_-     =||-|-|:::::::
                    ,   |/&_,_-|=||  | |=_-     =|-|-||:::::::
                  ,--``8%,/    ',%||  | |=_-     =||-|-|%::::::
              ,---`_,888`  ,.\'\'\'\'\'`-.,|,|/!,--,.&\|&\-,|&#:::::
            |;:;K`__,...;=\_____,=``           %%%&     %#,---
            |;::::::::::::|       `'.________+-------\   ``
            /8M%;:::;;:::::|                  |        `-------
  ''')
  time.sleep(3)
  print('You are thrown in a cell with a man huddled in the corner who appears to be crazy. There is also a stack of hay beside the man. What will you do?\n')
  while inv['Needle'] == 0:
      choice = input('A: Talk to the man\nB: Search the hay\n')

      if str.lower(choice)=='inventory':
            inventory(inv)
            continue
            
      if str.lower(choice) == 'a':
          if random.randint(1,3) == 3:
              dialogue('Prisoner: NYAHAHHAH\n\n')
          else:
              print('You try to talk to the man, he has no reaction\n')
      if str.lower(choice) == 'b':
          if inv['Needle'] == 0:
              if random.randint(1,x) == 1:
                  print('[O==================-\nYou found a needle in the haystack! You picked up the needle.')
                  inv['Needle'] = 1
              else:
                  print('You decide to rip the haystack apart a bit and make a mess. The haystack is smaller now.\n')
                  x /= 2
  time.sleep(2)
  print('You see the lock on the door is loose and the man is starting to twitch.\n')
  time.sleep(1)
  while inv['Needle'] == 1:
      choice = input('A:Poke the man with the needle\nB:Pick the lock on the door\n')

      if str.lower(choice)=='inventory':
          inventory(inv)
          continue

      if str.lower(choice) == 'a':
          if inv['Gold'] == 0:
              print('He dies. You search his body and find he has a bag of gold.')
              print(r"""    \`\/\/\/`/
     )======(
   .'        '.
  /    _||__   \
 /    (_||_     \
|     __||_)     |
|       ||       |
'.              .'
  '------------'""")
              print('YOU OBTAINED 10 GOLD\n')
              inv['Gold']+=10
          else:
              print('The man is already dead, you should stop poking him.\n')
      if str.lower(choice) == 'b':
          print('You successfully pick the lock and the needle breaks. The door swings open.')
          inv['Needle'] = 0
          time.sleep(2)

  print('You leave the cell. You notice that there is an exit to your left and two rooms on your right. One of them looks to be a kitchen and the other looks like a blacksmith\'s quarters. What do you do?\n')
  time.sleep(2)
  while True:
      choice = input('A:Exit the dungeon\nB:Enter the kitchen \nC:Enter the blacksmith\'s quarters\n')

      if str.lower(choice)=='inventory':
          inventory(inv)
          continue

      while str.lower(choice) not in ['a','b','c']:
          choice = input('A:Exit the dungeon\nB:Enter the kitchen \nC:Enter the blacksmith\'s quarters\n')

          if str.lower(choice)=='inventory':
            inventory(inv)  
            continue

      if str.lower(choice) == 'a'and inv['Key']<1:
          print('It is locked, you must obtain a key.\n')

      if str.lower(choice) == 'a'and inv['Key']>0:
          inv['Key']-=1
          break

      if str.lower(choice) == 'b':
          kitchen()

      if str.lower(choice) == 'c':
          africanamericansmith()
  print('You exit the dungeon and a guard spots you trying to escape.')
  print(r'''              ,
     __  _.-"` `'-.
    /||\'._ __{}_(
    ||||  |'--.__\
    |  L.(   ^_\^
    \ .-' |   _ |
    | |   )\___/
    |  \-'`:._]
    \__/;      '-.
    |   |o     __ \
    |   |o     )( |
    |   |o     \/ \ ''')
  fight(list(enemies.keys())[0])
  if hp <= 0:
    print('YOU DIED\nPlay again?')
    choice = input('Y/N\n')
    while str.lower(choice) not in ['y','n']:
      choice = input('Y/N\n')
    if str.lower(choice) == 'y':
      continue
    if str.lower(choice) == 'n':
      break
  print('You bandage your wounds with the clothes of the fallen guard and take his sword. You also eat a muffin you found in his pocket and feel rejuvinated.\nYour HP: 100')
  hp = 100
  inv['Sword']+=1
  time.sleep(3)
  print('You see a door that exits the castle up ahead.')
  choice = input('\nA: Run\nB: Sneak\nC: Crawl\nD: Moonwalk\nE: Play dead\n')
  if str.lower(choice)=='inventory':
          inventory(inv)
  if str.lower(choice) == 'e':
      print('You seem to be a little confused in the heat of the moment and play dead but nothing happens. There don\'t appear to be any bears nearby, and none of the guards are watching you.')
  while str.lower(choice) not in ['a','b','c','d']:
    choice = input('\nA: Run\nB: Sneak\nC: Crawl\nD: Moonwalk\nE: Play dead\n')
    if str.lower(choice)=='inventory':
          inventory(inv)
          continue
    if str.lower(choice) == 'e':
      print('You seem to be a little confused in the heat of the moment and play dead but nothing happens. There don\'t appear to be any bears nearby, and none of the guards are watching you.')
  if str.lower(choice) == 'a':
    print(r'''              .._
      _.""    .'       `-._
    .";      ;           ; `-.
  / /     .'           ;     `.
  / ;     ;             ;       \
; :      :             :     `-.\
; ;      :              `.      `;
: :      :                \      :
: \      `:                \   `.;
  \ \      `;                ;    ;
  \ : .'   ;                |   ;
    `>'     :              `.;   )
    / _.'               `.  ;/ _(
  ;,'     ;    `.        `.;    `-.
  ;' .'   :    `. `.       / \, \ \ \
  :,'     :      `. `. \  ; ::\_/_/_/::
.-=:.-"  -,-   "-.,=-.\ ;.; :::; ; ;::
|(`.`     :       .')| \: `.  :::::::
\\/      :       \//   ;   \              
  :      .:.       :  _/     ;            
  ;                ;  ;      |            
  :    _     _    ;  /       ;            
  `.  \;   ;/  .' .'       /             
    !  :   :  !_.'        /          
      `.:   :.'/\         ;      
        \ _ /  | :       :   
        ;"^"   | !       :
      .-'      | ;       |
    / / /    / /       /
    \_\_\__.'-|       ;
              /      .'
          .-'      (
          / , ,  , |/
          \|  |  |v'     
            v-;v-'       ''')
    print('You run out of cover exposing yourself in bare sight in front of all the guards. Unfortunately their pet mother bear, bearing cubs, is frightened, looks at you and bares her teeth.')
    fight(list(enemies.keys())[1])
    if hp <= 0:
      print('YOU DIED\nPlay again?')
      choice = input('Y/N\n')
      while str.lower(choice) not in ['y','n']:
        choice = input('Y/N\n')
      if str.lower(choice) == 'y':
        continue
      if str.lower(choice) == 'n':
        break
  if str.lower(choice) == 'b':
    print('You become a stealth ninja and do a triple backflip towards the door. The guards never notice your absence.')
    time.sleep(3)
  if str.lower(choice) == 'c':
    print('You attempt to crawl out towards the door but the guards notice you. Dumbfounded at your stupidity they deem you as not a threat and let you go.')
    time.sleep(3)
  if str.lower(choice) == 'd':
    print('You bust out some moves that would make any Michael Jackson fan proud while making your way to the door. The guards notice you from the oddly sexual sounds you\'re making along the way but are so impressed by your bomb moves that they open the door for you and usher you through.')
    time.sleep(3)
  print(r'''     .-. _,,,,,_ .-.
    ( , ' :   : ' , )
     /    :   :    \
    ;    0.---.0    ;
     \  /   _   \  /
      \ |  (_)  | /
    ." `\  -'-  /` ".
   /     `"""""`     \
  /   .'   .-== '.    \
 /   /       .-=='\    \
(   /              \    )
 '-;`.             .';-'
  /_  `-.______ .-` __\
/`  `\  /      `\  /   `\
\    | /         \ |    /
 `'--'`           `'--'`''')
  print('On the other side of the door, you are confronted by a bear cub.')
  fight(list(enemies.keys())[2])
  if hp <= 0:
      print('YOU DIED\nPlay again?')
      choice = input('Y/N\n')
      while str.lower(choice) not in ['y','n']:
        choice = input('Y/N\n')
      if str.lower(choice) == 'y':
        continue
      if str.lower(choice) == 'n':
        break
  print('As you take a deep breath of fresh air you see Shia Labeouf pop out of the woods. He greets you with these kind words.')
  time.sleep(3)
  dialogue('Do it. Just do it. Don\'t let your dreams be dreams. Yesterday, you said tomorrow. So just do it. Make your dreams come true. Just do it. Some people dream of success, while you\'re gonna wake up and work hard at it. Nothing is impossible. You should get to the point where anyone else would quit, and you\'re not gonna stop there. No, what are you waiting for? Do it! Just do it! Yes you can. Just do it.')
  for i in range(20):
    print('')
    time.sleep(0.2)
  print('CREDITS')
  for i in range(10):
    print('')
    time.sleep(0.2)
  print('Nicol Harrison Digital Entertainment Production Studios Co. Inc.')
  for i in range(10):
    print('')
    time.sleep(0.2)
  print('Regional Manager\nBob Nicol')
  for i in range(10):
    print('')
    time.sleep(0.2)
  print('Assistant to the Regional Manager\nOliver Harrison')
  for i in range(10):
      print('')
      time.sleep(0.2)
  print('Writers\nBob Nicol\nOliver Harrison')
  for i in range(10):
      print('')
      time.sleep(0.2)
  print('Programming\nBob Nicol\nOliver Harrison')
  for i in range(10):
      print('')
      time.sleep(0.2)
  print('Game Testing\nBob Nicol\nOliver Harrison')
  for i in range(10):
      print('')
      time.sleep(0.2)
  print('The End')
  for i in range(60):
      print('')
      time.sleep(0.2)
  print('\nYou Won. Play again?')
  choice = input('Y/N\n')
  while str.lower(choice) not in ['y','n']:
    choice = input('Y/N\n')
  if str.lower(choice) == 'y':
    continue
  if str.lower(choice) == 'n':
    break
