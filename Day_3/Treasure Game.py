print('''
88888888888888888888888888888888888888888888888888888888888888888888888
88.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..88
88   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  88
88      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  88
88..__  |     |`-!._ | `.| |_______________||."'|  _!.;'   |     _|..88
88   |``"..__ |    |`";.| i|_|MMMMMMMMMMM|_|'| _!-|   |   _|..-|'    88
88   |      |``--..|_ | `;!|l|MMoMMMMoMMM|1|.'j   |_..!-'|     |     88
88   |      |    |   |`-,!_|_|MMMMP'YMMMM|_||.!-;'  |    |     |     88
88___|______|____!.,.!,.!,!|d|MMMo * loMM|p|,!,.!.,.!..__|_____|_____88
88      |     |    |  |  | |_|MMMMb,dMMMM|_|| |   |   |    |      |  88
88      |     |    |..!-;'i|r|MPYMoMMMMoM|r| |`-..|   |    |      |  88
88      |    _!.-j'  | _!,"|_|M<>MMMMoMMM|_||!._|  `i-!.._ |      |  88
88     _!.-'|    | _."|  !;|1|MbdMMo-MMMMM|l|`.| `-._|    |``-.._  | 88
88..-i'     |  _.''|  !-| !|_|MMMoMMMMoMM|_|.|`-. | ``._ |     |``"..88
88   |      |.|    |.|  !| |u|MoMMMMoMMMM|n||`. |`!   | `".    |     88
88   |  _.-'  |  .'  |.' |/|_|MMMMoMMMMoM|_|! |`!  `,.|    |-._|     88
88  _!"'|     !.'|  .'| .'|[@]MMMMMMMMMMM[@] |  `. | `._  |   `-._   88
88-'    |   .'   |.|  |/| /                 |`.  |`!    |.|      |`- 88
88      |_.'|   .' | .' |/                      |  `.  | `._-|--|    88
88     .'   | .'   |/|  /                      |`!   |`.|    `.  |   88
88  _.'     !'|   .' | /                       |  `  |  `.    |`.|   88
88888888888888888888888888888888888888888888888888888888888888888888888
''')
print("You are an explorer of ancient ruins who finds themselves standing before a giant stone gate leading to an underground vault known as 'The Crimson Moon Dungeon'."
      "It is said that the Treasure is hidden within its depths, but the path is riddled with illusory traps and logical puzzles.")
print("You enter the dungeon, and the stone gate slams shut behind you."
      "You find yourself in a long corridor that ends at a fork in the road.")
choice1 = input("Option 1 (Right): A passage smelling of old paper and ink, lit by dim, flickering candles."
                "Option 2 (Left): Stone stairs descending toward a strangely glowing blue mist.\n").lower()
if choice1 == "right":
    print("You proceed safely and reach a vast hall")
    print("You reach an underground lake where the water is pitch black. "
          "On the shore sits a rickety wooden boat with a silent guardian in a tattered cloak, holding out his hand toward you.")
    choice2 = input("Option 1 (Pay): You give him a silver coin found in your pocket and wait for him to ferry you across."
                    "Option 2 (Swim): You ignore the guardian and decide to swim across the lake yourself.\n").lower()
    if choice2 == "pay":
        print("The guardian nods silently and ferries you safely to the opposite shore, where you face the final chamber.")
        print("At the end of the shore, you find yourself in a circular room containing three massive doors. "
              "Each door bears a different symbol, and you must choose the correct one to escape with the truth:")
        choice3 = input("Door 1 (Red): Engraved with a bleeding crimson eye."
                        "Door 2 (Black): Engraved with a flower blooming in the darkness."
                        "Door 3 (Copper): Engraved with mechanical gears and complex logical symbols.\n").lower()
        if choice3 == "copper":
            print("The gears turn with a soft mechanical hum; the door opens to reveal the ancient treasure radiating a golden light."
                  "You have survived through your intellect! "
                  "(You Win)")
            print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`." ` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
            ''')
        elif choice3 == "red":
            print("You open the door only to be engulfed by illusory crimson flames that consume you. "
                  "(Game Over)")
            print(r'''
            (
                .            )        )
                         (  (|              .
                     )   )\/ ( ( (
             *  (   ((  /     ))\))  (  )    )
           (     \   )\(          |  ))( )  (|
           >)     ))/   |          )/  \((  ) \
           (     (      .        -.     V )/   )(    (
            \   /     .   \            .       \))   ))
              )(      (  | |   )            .    (  /
             )(    ,'))     \ /          \( `.    )
             (\>  ,'/__      ))            __`.  /
            ( \   | /  ___   ( \/     ___   \ | ( (
             \.)  |/  /   \__      __/   \   \|  ))
            .  \. |>  \      | __ |      /   <|  /
                 )/    \____/ :..: \____/     \ <
          )   \ (|__  .      / ;: \          __| )  (
         ((    )\)  ~--_     --  --      _--~    /  ))
          \    (    |  ||               ||  |   (  /
                \.  |  ||_             _||  |  /
                  > :  |  ~V+-I_I_I-+V~  |  : (.
                 (  \:  T\   _     _   /T  : ./
                  \  :    T^T T-+-T T^T    ;<
                   \..`_       -+-       _'  )
                      . `--=.._____..=--'. ./ 
            ''')
        else:
            print("The engraved flower releases a toxic gas, plunging you into a deep sleep from which there is no waking. "
                  "(Game Over)")
            print(r"""
            .-.
       ,-( o )-.
      ( o )-( o )
     .-\-'.|,`-/-.      .-.
    ( o )--*--( o )  ,-( o )-.
     `-/-.'|`,-\-'  ( o )-( o )
      ( o )-( o )  .-\-'.|,`-/-.
       `-( o )-' _( o )--*--( o )
          `-' \/_/ `-/-.'|`,-\-'
            __ |    ( o )-( o )
            \_\|   .'`-( o )-'
               | .'\    `-' 
               |/   |\
            __ |    \|
            \_\|
               | __
               |/_/
            __ |
            \_\|
               | __
               |/_/
            __ |
            \_\|
               | __
               |/_/
            __ |
            \_\|
               | __
               |/_/
            __ |
            \_\|
               | __
               |/_/
            """)
    else:
        print("The black waters hide slimy monsters that drag you to the bottom. "
              "(Game Over)")
        print(r'''
                                               ,--,  ,.-.
                ,                   \,       '-,-`,'-.' | ._
               /|           \    ,   |\         }  )/  / `-,',
               [ '          |\  /|   | |        /  \|  |/`  ,`
               | |       ,.`  `,` `, | |  _,...(   (      _',
               \  \  __ ,-` `  ,  , `/ |,'      Y     (   \_L\
                \  \_\,``,   ` , ,  /  |         )         _,/
                 \  '  `  ,_ _`_,-,<._.<        /         /
                  ', `>.,`  `  `   ,., |_      |         /
                    \/`  `,   `   ,`  | /__,.-`    _,   `\
                -,-..\  _  \  `  /  ,  / `._) _,-\`       \
                 \_,,.) /\    ` /  / ) (-,, ``    ,        |
                ,` )  | \_\       '-`  |  `(               \
               /  /```(   , --, ,' \   |`<`    ,            |
              /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
        ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
       (-, \           ) \ ('_.-._)/ /,`    /
       | /  `          `/ \\ V   V, /`     /
    ,--\(        ,     <_/`\\     ||      /
   (   ,``-     \/|         \-A.A-`|     /
  ,>,_ )_,..(    )\          -,,_-`  _--`
 (_ \|`   _,/_  /  \_            ,--`
  \( `   <.,../`     `-.._   _,-`
   `                      ```
        ''')
else:
     print("The blue mist is an illusory trap that drains the mind; you wander the labyrinth forever. "
           "(Game Over)")
     print('''
                        :::!~!!!!!:.
                  .xUH WH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~

     ''')

