'''
This python script consists of a code that can be used to replace a string in the user input'''


def replace_String():
    input_string = "Hello <<UserName>>, How are you?"
    name = input("Enter a name: ")
    try:
        if len(name) >= 3:
            return f"Hello {name}, How are you?"
        else: 
            print("Enter the valid length")
    except:
        return replace_String()

def main():
    print(replace_String())

if __name__ == "__main__":
    main()
