"""
 -[x] Create an Array of fruits.
     - Dislay the options in a list format. 
     - Allow the user to select the menu through typing the response. 
 -[x] Create User select menu. 
    - Selecting a correct awnser will store and output the selected items.
    - Selecting an invalid option will display the menu; 3 invalid answers will quit the program. 
-[x] Create a closing script for the user to access at any time.  
    - Use the Q shortcut to quit.
"""

import time
from simple_term_menu import TerminalMenu


def main():
    options = [
      '[0] apples', 
      '[1] peaches', 
      '[2] pears', 
      '[3] plums', 
      '[4] cherries', 
      '[5] grapes', 
      '[6] blueberries', 
      '[7] cranberries', 
      '[8] strawberries', 
      '[9] raspberries',
    ]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")

if __name__ == "__main__":
    main()
