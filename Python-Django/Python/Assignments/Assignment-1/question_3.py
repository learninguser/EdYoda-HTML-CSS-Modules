states = {'New Hampshire': ['Concord', 'Hanover'],
'Massachusetts': ['Boston', 'Concord', 'Springfield'],
'Illinois': ['Chicago', 'Springfield', 'Peoria']
}

state = states.keys()
cities = list(states.values())

output = {}
flat_list = []

for sublist in cities:
    for item in sublist:
        flat_list.append(item)

flat_list = set(flat_list)

for idx in flat_list:
    output.setdefault(idx, [])

tempVar = list(states.items())

for idx, value in enumerate(tempVar):
    for idy, val in enumerate(value[1]):
        if val in output:
            output[val].append(value[0])
print(output)