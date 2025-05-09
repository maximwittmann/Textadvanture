# Ascii Art from: http://www.ascii-art.de/ascii/index_uvw.shtml
import os
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def start():

    clear()
    print("""

                      |
                     _=_
                     \ /.           _=links
        .-.    _ .-_ |  |_         |  |
 "   _  | |   | ||  \|    |_.--.   |  |
 |  | |_| |-__| ||          |  |,-.|  |-_   __
|H|-|   '                          |     | |  |
                                         |_|  |
""")
    print("""
            _                                             -      )
          (`  `.                    __                   (   (     )
         (     ).                .:(`  )`.         _     `(   `   )
      _(      )'`.             :(        )       (`   )    ` __.:'     _
  .=(`(      .   )       .--    -    -  ) )     (       )            (`  ).
 ((    (..__.:,-_     .+(   )    `+_ ,)  )        ( _.:'     _      (      ).
 `(       ) ) |-_'-,  (   .  )      :  _)                   ( ` )_(        '`.
   ` __.:'   )|-_'-' (   (   ))      ;-_            ._    (  .=(`(      .    )
         `- ' |-_'/   `- __.'        |=_',       .-(`  )   `(     (..__.:` -'
    /;-,_     |-_'           _       |-_';      :(      ) ,-_`      ) )
   /-.-;,-,___|'            /=-,_    |=_'         ` __.:  |=_- -__.:'   )
  /;-;-;-;_;_/|\_ _ _ _ _  /-,-=_-,__|'           ,_      |-_|     ` --'
     x_( __`|_P_|`-;-;-;-|/,-,-,-_=,/|\ _ _ _ _  /,-;-,___|-'
     |\ \    _||   `-;-;-'   x_( _`|_P_|-;-;-;-|`-;-,-;-,/|\_ _ _ _
     | \`   -_|.      '-'    :\ \   _||  `-,-,-'   x_(_`|_P_-;-;-;-/
     | /   /-_| `            : \`  /-|.     `-'    :\ | ,=||  `-,-,  ,'`,
     |/   /'-_|  \           : /  /-=| \           : V  |-| \    ` _-;`;`;
     /____`'-_|___\          :/__|_-_|__\          :/__|`-|__\    ( ; ;`;`:
_,-,__]__|__-_'|_[___,.,______]_|_`-='|_[_,-,_______]_|_`-'|_[____/^/;`;`;`,_,
    ,      .           `:.   , .,            `'.               _,/ / ';`;`;.
.,,,\||,;//\,.,,,>..__  _.;, \|\|\<`,..___   ,.,:,_.,   _,;.,-.`\-_';-;`;`;`;_
           -      _       -   _    -  _   -    - _   -  _   -   _ -`-`_'-`-'_
                                  -       -   _    -   _   -   -  _-   - _-  _   
    """)

    print("Willkommen zum Textadventure!")
    print("Du befindest dich in einem dunklen Wald. Vor dir gibt es zwei Wege.")
    print("Wählst du den linken oder den rechten Weg?")
    choice = input("Gib 'links' oder 'rechts' ein: ").lower().strip()

    if choice == 'links':
        left_path()
    elif choice == 'rechts':
        right_path()
    else:
        print("Ungültige Eingabe! Versuche es noch einmal.")
        start()


def left_path():
    clear()
    print("""
             !!!!!!!!!\========[ /]]|[[\ ]=====/
            /-_--_-_-_[[[[[[[[[||==  == ||]]]]]]
           /-_--_--_--_|=  === ||=/^|^\ ||== =|
          /-_-/^|^\-_--| /^|^\=|| | | | ||^\= |
         /_-_-| | |-_--|=| | | ||=|_|_|=||"|==|
        /-__--|_|_|_-_-| |_|_|=||______=||_| =|
       /_-__--_-__-___-|_=__=_.`---------'._=_|__
      /-----------------------\===========/-----/
     ^^^\^^^^^^^^^^^^^^^^^^^^^^[[|]]|[[|]]=====/
         |.' ..==::'"'::==.. '.[ /~~~~~\ ]]]]]]]
         | .'=[[[|]]|[[|]]]=`._||==  =  || =\ ]
         ||== =|/ _____ \|== = ||=/^|^\=||^\ ||
         || == `||-----||' = ==|| | | |=|| |=||
         ||= == ||:^s^:|| = == ||=| | | || |=||
         || = = ||:___:||= == =|| |_|_| ||_|=||
        _||_ = =||o---.|| = ==_||_= == =||==_||_
        \__/= = ||:   :||= == \__/[][][][][]\__/
        [||]= ==||:___:|| = = [||]\\//\\//\\[||]
        }  {---'"'-----'"'- --}  {//\\//\\//}  {
      __[==]__________________[==]\\//\\//\\[==]_
     |`|~~~~|================|~~~~|~~~~~~~~|~~~~||

    """)
    print("\nDu gehst den linken Weg entlang und findest eine alte Hütte.")
    print("Möchtest du die Hütte betreten oder weitergehen?")
    choice = input("Gib 'betreten' oder 'weitergehen' ein: ").lower()

    if choice == 'betreten':
        enter_hut()
    elif choice == 'weitergehen':
        continue_path()
    else:
        print("Ungültige Eingabe! Versuche es noch einmal.")
        left_path()


def right_path():
    clear()
    print("""
                              _.._
       _________....-~    ~-.______
    ~~~                            ~~~~-----...___________..--------
                                               |   |     |
                                               | |   |  ||
                                               |  |  |   |
                                               |'. .' .`.|
    ___________________________________________|0oOO0oO0o|____________
     -          -         -       -      -    / '  '. ` ` \    -    -
          --                  --       --   /    '  . `   ` \    --
    ---            ---          ---       /  '                \ ---
         ----               ----        /       ' ' .    ` `    \  ----
    -----         -----         ----- /   '   '        `      `   \

    """)
    print("\nDu gehst den rechten Weg entlang und hörst ein seltsames Geräusch.")
    print("Möchtest du dem Geräusch folgen oder umkehren?")
    choice = input("Gib 'folgen' oder 'umkehren'links ein: ").lower()

    if choice == 'folgen':
        follow_sound()
    elif choice == 'umkehren':
        start()
    else:
        print("Ungültige Eingabe! Versuche es noch einmal.")
        right_path()


def enter_hut():
    clear()
    print("""
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-" "-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
    """)
    print("\nIn der Hütte findest du eine alte Schatztruhe.")
    print("Möchtest du die Truhe öffnen oder die Hütte verlassen?")
    choice = input("Gib 'öffnen' oder 'verlassen' ein: ").lower()

    if choice == 'öffnen':
        print("\nDie Truhe enthält einen wertvollen Schatz! Du hast das Spiel gewonnen!")
    elif choice == 'verlassen':
        print("\nDu verlässt die Hütte und gehst zurück in den Wald.")
        left_path()
    else:
        print("Ungültige Eingabe! Versuche es noch einmal.")
        enter_hut()


def continue_path():
    clear()
    print("""

     ''--'              _,--)            ~   ,-.
          `-'   `---'      /            ,--.                      ~
 _ -'-._/    _   -.    `-./  ~~  ~               ~~
              `--. __,-- ' ----...__,-,--.___.....__        ~~        ~
         `/-._           \           .              `''''------..._____
      ,-'            --'  |    .        ,-. ,--.
  --._         __         /            ,--./,--.  ,--.  _    .
         __,     `--.    (            ( ,-'|--. ),--.,'' )        :.
                          )      .     (  ||  '   ,-',--.`    .
   --'     ,--'          _\    ___ ,-.    || ,--.( _||   )
                   __,--' /   ',--`,--.   || ,--.,--.)             .
`-   \                 ,-'    (,--.,-. )    ( ,-.,--.)
      `-._   --._,-  _/       (   ||  )      (  ||   `   .
          `--.__,.--'             ||            ||
  ---'         /        ,--. _,-. ||    ,'`--.._||           __   ,-.
         `--   |       _,--./,--.     ,'         `'--.._    ( _`./,--.
             __/      (  ,-.|--. )  ,'               ,' `-._ (,-.,--. )
       _,--' (   .      (  ||   )   `--..__        ,'    _.| (  ||
    ,         \            ||       | |`-. `'--..,' _,||  ||    ||
,--'       `-- \           ||       | '-.|  |`'| | |  |'-'_|    ||
               |     __,--``--..__  `--..__ `--' | |  |,-'
     `.        \_,--'   _,--..__  ``--..__ `'--..|_|-'  `-.
       `-._     )   _,-'        ``--..__  ``--..__,-'  _,-'
  """)
    print("\nDu gehst weiter und findest einen verborgenen Pfad, der zu einem ruhigen See führt.")
    print("Herzlichen Glückwunsch! Du hast einen friedlichen Ort zum Ausruhen gefunden.")
    print("Das Abenteuer endet hier.")


def follow_sound():
    clear()
    print("""
               ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO
       ::::::;       ;          OOOOO
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#   
    """)
    print("\nDu folgst dem Geräusch und wirst von einem wilden Tier angegriffen!")
    print("Leider hast du das Spiel verloren.")


# Start the game
start()
