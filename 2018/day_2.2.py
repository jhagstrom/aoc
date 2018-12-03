indata_file = open("./2018/input_day2.txt", "r")
indata_txt = indata_file.readlines()
id1 = ""
for line in indata_txt:
    id1 = line.strip('\n')
    for match in indata_txt:
        id2 = match.strip('\n')
        if(id1 == id2):
            continue
        id_str = "".join([i for i, j in zip(id1,id2) if i==j])
        if((len(id1) == len(id2)) and (len(id1) == len(id_str) + 1)):
            print(id1, " and ", id2, " ", id_str)