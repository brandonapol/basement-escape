import colorama
from colorama import Fore
import os
from time import sleep

from doors import levels

colorama.init(autoreset=True)

def open_door(current_level):
    selection = 0
    while str(selection) != str(levels[current_level]["correct_answer"]):
        if selection == "1":
            print(Fore.WHITE + levels[current_level]["first_door"])
        elif selection == "2":
            print(Fore.WHITE + levels[current_level]["second_door"])
        elif selection == "3":
            print(Fore.WHITE + levels[current_level]["third_door"])
        selection = input(Fore.CYAN + "Choose a door 1/3: ")
    print("You found stairs up to the next level!")

def start_game():
    os.system("clear")
    print(Fore.RED + r"""
        ___________ __________________     _____ _____________________     _______      _____    _________.____________  
        \_   _____//   _____/\_   ___ \   /  _  \\______   \_   _____/     \      \    /  _  \  /   _____/|   \_   ___ \ 
        |    __)_ \_____  \ /    \  \/  /  /_\  \|     ___/|    __)_      /   |   \  /  /_\  \ \_____  \ |   /    \  \/ 
        |        \/        \\     \____/    |    \    |    |        \    /    |    \/    |    \/        \|   \     \____
        /_______  /_______  / \______  /\____|__  /____|   /_______  /    \____|__  /\____|__  /_______  /|___|\______  /
                \/        \/         \/         \/                 \/             \/         \/        \/             \/ 
        """)
    level = 0
    sleep(1)
    print(Fore.GREEN + "You are in the basement. You see three doors.")
    while level < len(levels):
        print(Fore.MAGENTA + "Level: " + str(level))
        open_door(level)
        level += 1
    os.system("clear")
    print(Fore.LIGHTBLUE_EX + "Congrats! You escaped the basement!")
    sleep(1)
    print(Fore.YELLOW + r"""                                       ..,                                      
                                       ..,                                      
                           .,.         ,.          ,..                          
                             .,.                  ,,,                           
                 .,                 ,,..,.,,..                                  
                  ,,,.         ,.   ,,,,,,,,.,             ,.,.,.               
                      ,,    .,.,...............,...  .                          
                           ,........................                            
                         ,...........................                           
                         ............................,.                         
                ,...    .,.............................      ..,.,              
                         ,............................ ,,                       
                         ,..........................., .                        
                          ,........................., .                         
                           ,....................... ,.                          
                 ,....,      ,....................,.      ...,,.                
                .,.             ,..............,              ,,,               
                              ,                   ,,                            
                           ,.,         ,.          .,..                         
                                       ..            ,                          
                                      ..,                                       
                                       ,,                                       
                                                                                
                                                              """)
    sleep(1)
    print(Fore.BLUE + r"""                                                                                       
         ____  _  _   __   __ _  __ _    _  _  __   _  _    ____  ____  ____  ____  __  ___  __ _     __   __ _  ____    __ _  __  ____  __ _ 
        (_  _)/ )( \ / _\ (  ( \(  / )  ( \/ )/  \ / )( \  (    \(  __)(  _ \(  _ \(  )/ __)(  / )   / _\ (  ( \(    \  (  / )(  )(  __)(  ( \
          )(  ) __ (/    \/    / )  (    )  /(  O )) \/ (   ) D ( ) _)  )   / )   / )(( (__  )  (   /    \/    / ) D (   )  (  )(  ) _) /    /
         (__) \_)(_/\_/\_/\_)__)(__\_)  (__/  \__/ \____/  (____/(____)(__\_)(__\_)(__)\___)(__\_)  \_/\_/\_)__)(____/  (__\_)(__)(____)\_)__)
    """)

start_game()
