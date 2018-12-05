def find_polar_opposites(units):
    for i in range(len(units)-1):
        if(units[i].swapcase() == units[i+1]):
            return units[i]+units[i+1]
    return ''

# indata_file = open("./2018/input_day5.txt", "r")
# units = indata_file.read()
# units = 'dabAcCaCBAcCcaDA'
polar_opposites = 'start_val'
while len(polar_opposites) > 0:
    polar_opposites = find_polar_opposites(units)
    units = units.replace(polar_opposites, '', 1)
print(units, len(units))


    
