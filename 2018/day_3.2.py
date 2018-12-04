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
            else:
                matrix[item_pos[0] + hpos, item_pos[1] + vpos] = item_id
            vpos += 1
        sp = matrix[item_pos[0] + hpos, item_pos[1]]
        if(sp != 0):
            if(sp != item_id):
                if(sp != -1):
                    matrix[item_pos[0] + hpos, item_pos[1] + vpos] = -1
        else:
            matrix[item_pos[0] + hpos, item_pos[1] + vpos] = item_id
        hpos += 1

def apply_all_patches(all_patches, cloth):
    for line in all_patches:
        line = line.strip('\n')
        patch = extract_position_and_dimension(line)
        apply_patch(patch, cloth)

def get_non_overlapping_patches(all_patches, cloth):
    non_overlapping_patches = []
    for line in all_patches:
        line = line.strip('\n')
        patch = extract_position_and_dimension(line)
        if(patch_does_not_overlap(patch, cloth)):
            non_overlapping_patches.append(patch)
    return non_overlapping_patches

def patch_does_not_overlap(item, matrix):
    no_overlap = True
    hpos = 0
    hstop = item["dimension"][0]
    item_pos = item["position"]
    while hpos < hstop:
        vpos = 0
        vstop = item["dimension"][1]
        while vpos < vstop:
            sq = int(matrix[item_pos[0] + hpos, item_pos[1] + vpos])
            if(sq == -1):
                no_overlap = False
                break
            vpos += 1
        sp = int(matrix[item_pos[0] + hpos, item_pos[1]])
        if(sp == -1):
            no_overlap = False
        hpos += 1
    return no_overlap

import numpy as np

# shape = (20, 20)
shape = (1000, 1000)
cloth = np.zeros(shape, dtype=int)
# indata_file = open("./2018/test_input_day3.txt", "r")
indata_file = open("./2018/input_day3.txt", "r")
indata_txt = indata_file.readlines()
apply_all_patches(indata_txt, cloth)
print("All patches applied")
non_overlapping_patches = get_non_overlapping_patches(indata_txt, cloth)
print(cloth)
print(non_overlapping_patches)