import time

def run_application():
    num_strings = ["15", "100", "55", "42"]
    num_ints = [15, 100, 55, 42]    
    num_floats = [15.4, 22.6, 76.43, 67.5]
    num_lists = [[1,2,3], [4,5,6], [7,8,9]]

    print("\n\t\t\tSummary Table")

    print("\tThe variable num_strings is a {}".format(type(num_strings))) # Determines the data type of num_strings
    print("\tIt contains the elements: {}".format(num_strings))
    print("\tThe element {} is a {}".format(num_strings[0],type(num_strings[0]))) # Determines the data type of first element of num_strings 

    print("\n\tThe variable num_floats is a {}".format(type(num_floats)))# Determines the data type of num_floats
    print("\tIt contains the elements: {}".format(num_floats))
    print("\tThe element {} is a {}".format(num_floats[0],type(num_floats[0]))) # Determines the data type of first element of num_floats

    print("\n\tThe variable num_lists is a {}".format(type(num_lists)))# Determines the data type of num_lists
    print("\tIt contains the elements: {}".format(num_lists))
    print("\tThe element {} is a {}".format(num_lists[0],type(num_lists[0]))) # # Determines the data type of first element of num_lists

    print("\n\tNow sorting num_strings and num_ints...")
    time.sleep(1)
    num_strings.sort() # Sorts the num_strings elements in ascending order of ASCII code of characters
    print("\tSorted num_strings: {}".format(num_strings)) 
    num_ints.sort() # Sorts the num_ints elements in ascending order
    print("\tSorted num_ints: {}".format(num_ints))
    print("\n\tStrings are sorted alphabetically while integers are sorted numerically!")

run_application()
