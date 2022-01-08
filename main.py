from game import Game
import utils
import keyboard

def main():
    game = Game()
    game.set_state("main_menu")

    while game.get_state() != "done":
        game.handle_state()
        cmd = input("> ")
        game.process_command(cmd)

if __name__ == "__main__":
    main()