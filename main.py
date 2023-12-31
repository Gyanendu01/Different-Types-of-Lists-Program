import time
num_strings = ["15", "100", "55", "42"]
num_ints = [15, 100, 55, 42]
num_floats = [15.4, 22.6, 76.43, 67.5]
num_lists = [[1,2,3], [4,5,6], [7,8,9]]

print("\n\t\t\tSummary Table")

print("\tThe variable num_strings is a {}".format(type(num_strings)))
print("\tIt contains the elements: {}".format(num_strings))
print("\tThe element {} is a {}".format(num_strings[0],type(num_strings[0])))

print("\n\tThe variable num_floats is a {}".format(type(num_floats)))
print("\tIt contains the elements: {}".format(num_floats))
print("\tThe element {} is a {}".format(num_floats[0],type(num_floats[0])))

print("\n\tThe variable num_lists is a {}".format(type(num_lists)))
print("\tIt contains the elements: {}".format(num_lists))
print("\tThe element {} is a {}".format(num_lists[0],type(num_lists[0])))

print("\n\tNow sorting num_strings and num_ints...")
time.sleep(1)
num_strings.sort()
print("\tSorted num_strings: {}".format(num_strings))
num_ints.sort()
print("\tSorted num_ints: {}".format(num_ints))
print("\n\tStrings are sorted alphabetically while integers are sorted numerically!")