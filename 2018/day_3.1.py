def extract_position_and_dimension(id_line):
    split_item = id_line.split('@')
    coords_and_dim = split_item[1]
    item_id = split_item[0].strip('#')
    item_id = item_id.strip(' ')
    coords_and_dim = coords_and_dim.split(':')
    coords = coords_and_dim[0].strip(' ')
    dim = coords_and_dim[1].strip(' ')
    coords = coords.split(',')
    dim = dim.split('x')
    item = { 
        "id": item_id, 
        "position": (int(coords[0]),int(coords[1])), 
        "dimension": (int(dim[0]),int(dim[1]))
    }
    return item

def apply_patch(item, matrix):
    number_of_overlapping = 0
    hpos = 0
    hstop = item["dimension"][0]
    item_pos = item["position"]
    item_id = int(item["id"])
    while hpos < hstop:
        vpos = 0
        vstop = item["dimension"][1]
        while vpos < vstop:
            sq = int(matrix[item_pos[0] + hpos, item_pos[1] + vpos])
            if(sq != 0):
                if(sq != item_id):
                    if(sq != -1):
                        matrix[item_pos[0] + hpos, item_pos[1] + vpos] = -1
                        number_of_overlapping += 1
            else:
                matrix[item_pos[0] + hpos, item_pos[1] + vpos] = item_id
            vpos += 1
        sp = matrix[item_pos[0] + hpos, item_pos[1]]
        if(sp != 0):
            if(sp != item_id):
                if(sp != -1):
                    matrix[item_pos[0] + hpos, item_pos[1] + vpos] = -1
                    number_of_overlapping += 1
        else:
            matrix[item_pos[0] + hpos, item_pos[1] + vpos] = item_id
        hpos += 1
    return number_of_overlapping

import numpy as np

shape = (1000, 1000)
cloth = np.zeros(shape, dtype=int)
indata_file = open("./2018/input_day3.txt", "r")
indata_txt = indata_file.readlines()
sq_inches_claimed = 0
for line in indata_txt:
    line = line.strip('\n')
    item = extract_position_and_dimension(line)
    sq_inches_claimed += apply_patch(item, cloth)
print(cloth)
print(sq_inches_claimed)