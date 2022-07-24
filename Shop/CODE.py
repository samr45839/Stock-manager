def number(bus_stops):
    inner = 0
    out = 0
    for passenger in bus_stops:
        inner += int(passenger[0])
        out += int(passenger[1])

    sum = inner - out

    return print(sum)

number([[10,0],[3,5],[5,8]])