import utils
from colorama import Fore

class Game:
    def __init__(self):
        self.__game_state = "main_menu"

    # Handles the current game state.
    def handle_state(self):
        if self.__game_state == "main_menu":
            utils.clear_screen()
            utils.reposition_cursor(0, 0)
            logo = (Fore.CYAN + """
    d8888b. d8888b.  .d88b.     d88b d88888b  .o88b. d888888b      d8888b. d888888b .88b  d88.  .d88b.  d8888b. 
    88  `8D 88  `8D .8P  Y8.    `8P' 88'     d8P  Y8 `~~88~~'      88  `8D   `88'   88'YbdP`88 .8P  Y8. 88  `8D 
    88oodD' 88oobY' 88    88     88  88ooooo 8P         88         88oobY'    88    88  88  88 88    88 88oobY' 
    88~~~   88`8b   88    88     88  88~~~~~ 8b         88         88`8b      88    88  88  88 88    88 88`8b   
    88      88 `88. `8b  d8' db. 88  88.     Y8b  d8    88         88 `88.   .88.   88  88  88 `8b  d8' 88 `88. 
    88      88   YD  `Y88P'  Y8888P  Y88888P  `Y88P'    YP         88   YD Y888888P YP  YP  YP  `Y88P'  88   YD                                                                                    
                                                    v0.1a""" + "\x1b[0m") #5,35,245
            print(logo)

            # print the menu items
            menu_items = ["Singleplayer [single]", "Multiplayer (soon)", "Options [options/opt]", "Exit [exit]"]
            for i in range(len(menu_items)):
                print(f"{Fore.LIGHTBLACK_EX}{menu_items[i]}")
        elif self.__game_state == "singleplayer":
            utils.clear_screen()
            utils.reposition_cursor(0, 0)
        elif self.__game_state == "options":
            utils.clear_screen()
            utils.reposition_cursor(0, 0)
            print(f"{Fore.CYAN}Options{Fore.RESET}")
            print(Fore.LIGHTBLACK_EX, end="") # Setting the options colors
            print("Options not implemented yet.\nExit options [exit]")

    # Processes the commands based on the current game state.
    def process_command(self, cmd: str):
        if self.__game_state == "main_menu":
            if cmd == "single":
               self.set_state("singleplayer")
            elif cmd == "options" or cmd == "opt":
                self.set_state("options")
            elif cmd == "exit":
                self.set_state("done")
        elif self.__game_state == "options":
            if cmd == "exit":
                self.set_state("main_menu")

    def get_state(self):
        return self.__game_state

    def set_state(self, state: str):
        self.__game_state = state

    def update(self):
        self.handle_state()
        cmd = input("> ")
        self.process_command(cmd)