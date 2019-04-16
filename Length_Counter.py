error_input = str(input("Please enter in the input message that caused the error: "))


def error_length(error: str) -> str:
    error_len = len(error)
    result = "\r\nThe length of the message is: {}\r\n".format(error_len)
    return result


print(error_length(error_input))

close = input("Press any key to exit")
