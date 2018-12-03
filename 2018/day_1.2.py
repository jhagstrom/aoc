def list_duplicates(seq):
  seen = set()
  seen_add = seen.add
  seen_twice = set( x for x in seq if x in seen or seen_add(x) )
  return list( seen_twice )
  
indata_file = open("./2018/input_day1.txt", "r")
indata_txt = indata_file.readlines()
indata = []
for line in indata_txt:
    indata.append(int(line))
# indata = [1,-1]
# indata = [3, 3, 4, -2, -4]
# indata = [-6, 3, 8, 5, -6]
# indata = [7, 7, -2, -7, -4]
frequencies = []
frequency = 0
first_duplicate_frequency = None
while first_duplicate_frequency is None:
    for x in indata:
        frequency += x
        if frequency == 0:
            first_duplicate_frequency = frequency
            break
        elif frequency not in frequencies:
            frequencies.append(frequency)
        else:
            first_duplicate_frequency = frequency
            break
# print(frequencies)
print("first duplicate frequency: ", first_duplicate_frequency)
