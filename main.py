from week0 import ship
from week0.swap import swap
from week1.fibonacci import fibonacci
from week1.family import family
from week2.factorial import factorial
from week2.lcm import lcm
main_menu = [
]
week0_sub_menu = [
  ["Ship", ship.driver],
  ["Swap", swap],
]
week1_sub_menu = [
  ["Fibonacci", fibonacci],
  ["family", family],
]
week2_sub_menu = [
  ["Factorial", factorial],
  ["LCM", lcm],
]
border = "======================="
banner = f"\n{border}\nPlease Select An Option\n{border}"
def menu():
    title = "Weekly Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Week 0", week0_submenu])
    menu_list.append(["Week 1", week1_submenu])
    menu_list.append(["Week 2", week2_submenu])
    buildMenu(title, menu_list)
def week0_submenu():
    title = "Week 0 Submenu" + banner
    buildMenu(title, week0_sub_menu)
def week1_submenu():
    title = "Week 1 Submenu" + banner
    buildMenu(title, week1_sub_menu)
def week2_submenu():
    title = "Week 2 Submenu" + banner
    buildMenu(title, week2_sub_menu)
def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op
    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '- ', value[0])
    # get user choice
    choice = input("Type your choice: ")
    print()
    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try
    print()
    buildMenu(banner, options)  # recursion, start menu over again
if __name__ == "__main__":
    menu()