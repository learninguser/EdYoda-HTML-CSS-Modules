# travel_trip = {"Chennai":"Banglore","Bombay":"Delhi","Goa":"Chennai","Delhi":"Goa"}

def travel_sequence(travel_trip):

    keys = set(travel_trip.keys())
    values = set(travel_trip.values())

    diff_values = keys.symmetric_difference(values)

    for idx in diff_values:
        if idx not in keys:
            end_trip = idx
        else:
            start_trip = idx

    start = True
    trip = {}

    while start:
        city = travel_trip[start_trip]
        trip[start_trip] = city
        if city == end_trip:
            start = False
        else:
            start_trip = travel_trip[start_trip]

    return trip

# print(travel_sequence({"A":"C","C":"D","E":"G","D":"E","G":"F"}))
print(travel_sequence({"X":"Z","Z":"U","A":"B","B":"X"}))


# trip = {}

# start_trip = "Bombay"
# end_trip   = "Banglore"

# a = travel_trip[start_trip]

# trip[start_trip] = a
# trip[a] = travel_trip[a]

# b = travel_trip[a]
# trip[b] = travel_trip[b]

# c = travel_trip[b]
# trip[c] = travel_trip[c]

# print(trip)