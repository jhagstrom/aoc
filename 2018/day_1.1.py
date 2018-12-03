indata_file = open("./2018/input_day1.txt", "r")
indata_txt = indata_file.readlines()
frequency = 0
for x in indata_txt:
    frequency += int(x)      
print(frequency)
