# imported timer module to sleep on final greeting
import time

# Created a function call main
def main():

    """
      # Printed greetinig for computer.
      # Created a variable for input from the user.
      # Added sleep timer to delay final message.
      # Closed off final conversaton.
    """"

    print("Hello World")
    name = input("What is your name? ")
    print("Nice to meet you", name)
    time.sleep(1)
    print("Bot: Hope you have a great time learning python", name)

# make sure the function is only beinig used when called.
if __name__ == "__main__":
    main()

# Close other background processes
exit()
