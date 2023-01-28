print('''  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____________~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/''')


print('### Welcome to the treasure hunting game ###')
print('What is your mission? Find the treassure Sherlock! \n')

print('''You find 2 ways,The path to the left leads through dense jungle, with tall trees blocking out much of the sunlight. The underbrush is thick and difficult to navigate, and there are likely to be dangerous animals lurking in the shadows. The path to the right is rocky and steep, with a narrow path winding up the side of a mountain. The path is treacherous, with loose rocks and steep drop-offs, but the view from the top is sure to be breathtaking.
It's important to note that this decision is all yours, as the main character is just a fictional representation of the person playing the game. Choose a path "left" or "right". ''')
path = input('Your choice: ').lower()

if path == 'right':
    print('''Holly molly you've tried to climb the mountain but strong wind make you fall down, Game Over''')

elif path == 'left':
    print('''The path to the left leads to a small clearing, where you can see a small stream running through the jungle. The stream is clear and shallow, and appears to be safe for swimming. The path to the right leads to a rocky outcropping overlooking the ocean. You can see a small boat anchored in the distance, and the water looks calm and inviting.
    The option of waiting, you could sit and rest, maybe gather some resources, and observe the environment, trying to gain more knowledge of the island and what it holds.
    On the other hand, if you choose to swim, you could explore the ocean, discover new places, fish, and maybe find some new resources, but also you could face the dangers of the sea such as sharks or jellyfish.
    Again, the decision is up to the player, and they will have to weigh the pros and cons of each option and decide which one to take based on their own preferences and the information you have provided.''')
    path = input('Your choice: ').lower()

    if path == 'swim':
        print('That wasnt a good idea, you are eatten buy a Megadolon')
    elif path == 'wait':
        print('''You decide to wait, and after an hour it appears two portals with two doors, the blue door leads to a large underground cave system. Inside, you find a network of tunnels and caverns, with sparkling crystals lining the walls. The air is cool and damp, and you can hear the sound of running water in the distance. The cave appears to be safe, but it's hard to know what kind of treasures or dangers may be hidden within.
        The red door leads to a small, dark room. Inside, you find a treasure chest filled with gold and jewels. The room is dimly lit and musty, and you can hear the sound of scurrying rats in the distance. The treasure is tempting, but you can't help but wonder what kind of traps or dangers may be waiting for you inside.
        Both options have their pros and cons. The blue door offers the opportunity to explore an unknown cave system and the potential to find valuable resources, but also the risk of getting lost or facing unknown dangers. On the other hand, the red door offers the immediate reward of treasure, but also the risk of falling into traps or facing other hazards.
        It's up to the player to decide which path to take, based on their own preferences and the information you have provided.
        The yellow door leads to a secret garden. Inside, you find a beautiful garden, with a variety of flowers and plants, a small pond with fish and frogs. The garden appears to be well-maintained and safe, but as you explore further, you notice a small tool shed in the corner, which may hold some useful tools or equipment.
        This option could be a change of pace, giving the player a chance to take a break from the adventure, relax, and enjoy the beauty of nature. The garden could also provide some resources such as fruits, herbs, and other useful plants. On the other hand, the tool shed may contain some useful equipment or tools that could help the player in their journey.''')
        
        path = input('Your choice: ').lower()
        if path == 'red':
            print('Red or blue if you chose that you are death duba du. Game Over')
        elif path == 'blue':
            print('Red or blue if you chose that you are death duba du. Game Over')
        elif path == 'yellow':
            print('''Congratulations! You have chosen the yellow door and have found the treasure! The treasure you have found is a chest filled with gold and jewels, as well as rare artifacts and ancient relics. You also found a map that leads to even more treasure hidden around the island. As you explore the garden further, you also find a small tool shed in the corner which contains useful tools and equipment that will help you on your journey.
            The treasure you have found is valuable not only for its monetary value, but also for the knowledge and clues it contains about the island and its history. The rare artifacts and ancient relics will give you insight into the island's past and the cultures that once inhabited it. The map will lead you to even more treasure and secrets, making your adventure all the more exciting.
            In addition, the tool shed provides useful equipment and tools that will help you on your journey, making your exploration easier and safer. With this treasure, you have the opportunity to continue your adventure and uncover even more secrets and riches on the island.
            Overall, the yellow door was a great choice that not only rewarded you with a treasure, but also provided valuable resources and knowledge that will help you in your journey.''')
