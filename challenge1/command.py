
def hello(message):
    # When this command is used, everything after the word "hello" in the message will be sent to this function.
    # Example: "@Jam hello Ronan" -> this function receivces "Ronan" as the messsage.
    #
    # Your job is to process the message so that this function returns the correct outputs for challenge 1.
    # (for now, it just echoes back the same message)

    message = input("please enter your name: ")

    if len(message) > 0:
        print("Hello,",message)
    
    elif len(message) == 0:
        return("Hello Cisco!") 
