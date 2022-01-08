from game import Game

def main():
    game = Game()
    game.set_state("main_menu")

    while game.get_state() != "done":
        game.update()

if __name__ == "__main__":
    main()