from collections import Counter
indata_file = open("./2018/input_day2.txt", "r")
indata_txt = indata_file.readlines()
number_of_threes = 0
number_of_twos = 0
for line in indata_txt:
    line = line.strip('\n')
    characters = list(line)
    counts = list(Counter(characters).values())
    if(3 in counts):
        number_of_threes += 1
    if(2 in counts):
        number_of_twos += 1
print("Checksum: ", number_of_threes*number_of_twos)