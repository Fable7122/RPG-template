import battle, dataController as dc, curses

dc.resetEnemy()
dc.resetData()
dc.resetMove()
stdscr = curses.initscr()
height, width = stdscr.getmaxyx()

def talk(message: str, person: str):
    if ":" not in person:
        person = person + ":"
    stdscr.clear()
    stdscr.addstr(height - 3, 0, person)
    stdscr.addstr(height - 1, 0, message)
    stdscr.refresh()
    k = 0
    while (k != 10):
        curses.curs_set(0)
        k = stdscr.getch()

def menu(options: list, back: bool, message="", person="") -> int:
    if person != "":
        if ":" not in person:
            person = person + ":"
    stdscr.clear()
    stdscr.refresh()
    k = 0
    optionsBackup = []
    loc = 0
    if back == True:
        options.append("Back")
    for x in range(len(options)):
        optionsBackup.append(options[loc])
        loc = loc + 1
    optionsBackup[0] = "[" + optionsBackup[0] + "]"
    menu = ""
    for i in optionsBackup:
        menu = menu + i + " "

    stdscr.addstr(height - 5, 0, person)
    stdscr.addstr(height - 3, 0, message)
    stdscr.addstr(height - 1, 0, menu)
    stdscr.refresh()
    curses.cbreak()
    curses.noecho()
    stdscr.keypad(True)
    loc = 0
    while True:
        stdscr.refresh()
        k = stdscr.getch()
        if k == curses.KEY_RIGHT:
            temp = ""
            optionsBackup.remove("[" + options[loc] + "]")
            optionsBackup.insert(loc, options[loc])
            try:
                loc = loc + 1
                temp = "[" + optionsBackup[loc] + "]"
                optionsBackup[loc] = temp
            except:
                optionsBackup = []
                loc = 0
                for x in range(len(options)):
                    optionsBackup.append(options[loc])
                    loc = loc + 1
                loc = 0
                temp = "[" + optionsBackup[loc] + "]"
                optionsBackup[loc] = temp
            menu = ""
            for i in optionsBackup:
                menu = menu + i + " "
            
            stdscr.addstr(height - 1, 0, menu)
            stdscr.refresh()

        elif k == curses.KEY_LEFT:
            temp = ""
            optionsBackup.remove("[" + options[loc] + "]")
            optionsBackup.insert(loc, options[loc])
            if loc > 0:
                loc = loc - 1
                temp = "[" + optionsBackup[loc] + "]"
                optionsBackup[loc] = temp
            else:
                optionsBackup = []
                loc = 0
                for x in range(len(options)):
                    optionsBackup.append(options[loc])
                    loc = loc + 1
                loc = len(options) - 1
                temp = "[" + optionsBackup[loc] + "]"
                optionsBackup[loc] = temp
            menu = ""
            for i in optionsBackup:
                menu = menu + i + " "
            
            stdscr.addstr(height - 1, 0, menu)
            stdscr.refresh()
        
        elif k == 127:
            if back == True:
                loc = len(options) - 1
                optionsBackup = []
                loc = 0
                for x in range(len(options)):
                    optionsBackup.append(options[loc])
                    loc = loc + 1
                loc = len(options) - 1
                temp = "[" + optionsBackup[loc] + "]"
                optionsBackup[loc] = temp
                menu = ""
                for i in optionsBackup:
                    menu = menu + i + " "

                stdscr.addstr(height - 1, 0, menu)
                stdscr.refresh()
        
        if k == 10:
            return loc


battle.battle("Bob", 10)