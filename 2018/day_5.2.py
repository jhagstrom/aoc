import re
def find_polar_opposites(units):
    for i in range(len(units)-1):
        if(units[i].swapcase() == units[i+1]):
            return units[i]+units[i+1]
    return ''

def get_polymer_permutations(units):
    permutations = []
    for c in units:
        regex = re.compile(c, re.IGNORECASE)
        permutation = regex.sub('', units)
        if(permutation not in permutations):
            permutations.append(regex.sub('', units))
    return permutations

def reduce_polymer(units):
    polar_opposites = 'start_val'
    while len(polar_opposites) > 0:
        polar_opposites = find_polar_opposites(units)
        units = units.replace(polar_opposites, '', 1)
    return units
indata_file = open("./2018/input_day5.txt", "r")
units = indata_file.read()
# units = 'dabAcCaCBAcCcaDA'
polymer_permutations = get_polymer_permutations(units)
reduced_polymers = []
for polymer in polymer_permutations:
    reduced_polymers.append(reduce_polymer(polymer))
shortest_polymer = min(reduced_polymers, key=len)
print(shortest_polymer, len(shortest_polymer))

