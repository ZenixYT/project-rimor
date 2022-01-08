def clear_screen():
    """
    Clear the screen
    """
    print("\033[2J", end="")

def reposition_cursor(x: int, y: int):
    """
    Reposition the cursor to a specific position
    """
    print("\x1b[{};{}f".format(y, x), end="")

def print_bg(r: int, g: int, b: int, text: str, end: str = "\n"):
    """
    Set the background color
    """
    r = str(r)
    b = str(b)
    g = str(g)

    print(f"\x1b[38;2;{r};{g};{b}m{text}\x1b[0m", end=end)

def print_fg(r: int, g: int, b: int, text: str, end: str = "\n"):
    """
    Set the foreground color
    """
    r = str(r)
    b = str(b)
    g = str(g)

    print(f"\x1b[38;2;{r};{g};{b}m{text}\x1b[0m", end=end)
    