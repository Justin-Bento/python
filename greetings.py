# imported timer module to sleep on final greeting
import time

# This function handles the greeting. 
def main():
    # Prints a Hello World greeting 
    print("Bot: Hello World")
    # create an name variable to collect your name.  
    name = input("Bot: What is your name? ")
    # Greets you with the words you typed.  
    print("Bot: Nice to meet you", name)
    # Delays the final message for 0.40s  
    time.sleep(0.40)
    # Displays final message  
    print("Bot: Hope you have a great time learning python", name)

# make sure the function is only beinig used when called.
if __name__ == "__main__":
    main()
    