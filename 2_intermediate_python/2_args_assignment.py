# Write a Python function concat_strings that takes any number of strings as
# arguments and returns a single concatenated string.

def concate_strings(*args):
    """
        Concated a string passed as arguments.

        Parameters:
        *args: list of string
            Arbitrary number of positional arguments.

    Returns:
        string
            concatenation of string  passed as arguments.
    """


    concated_string = ""
    for arg in args:
        return concated_string.join(args)
    
def main():
    print(concate_strings('apple','banana'))
    print(concate_strings('I ','AM ','FUSEHUMANS.'))

if __name__ == "__main__":
    main()
