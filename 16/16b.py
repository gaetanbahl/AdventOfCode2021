with open("input.txt", 'r') as f:
    line = f.readlines()[0].strip()

#line = "D2FE28"
#line = "38006F45291200"
#line = "EE00D40C823060"
#line = "8A004A801A8002F478"
#line = "620080001611562C8802118E34"
#line = "C0015000016115A2E0802F182340"
#line = "A0016C880162017C3686B18A3D4780"

binary = bin(int(line, 16))[2:].zfill(4*len(line))

def mul(l):
    acc = l[0]
    for n in l[1:]:
        acc *= n
    return acc


functions = {0:sum,
             1:mul,
             2:min,
             3:max,
             5:lambda x : x[0] > x[1],
             6:lambda x : x[0] < x[1],
             7:lambda x : x[0] == x[1]}

def parse(binstr, subpacket=False):

    print("\nremaining length", len(binstr))

    version = int(binstr[0:3],2)
    print("version", version)

    typeid = int(binstr[3:6],2)
    print("type", typeid)

    consumed = 6
    value = 0

    if typeid == 4:
        literal, remaining_str = parse_lit(binstr[6:])
        value = literal
        consumed += len(binstr[6:]) - len(remaining_str)
    else:

        fun = functions[typeid]
        print("function", fun)
        values = []

        lengthid = int(binstr[6],2)
        consumed += 1

        if lengthid == 0:
            print("15 bit mode")
            sub_length = int(binstr[7:22],2)
            print("length", sub_length)
            consumed += 15
            n_bits_parsed = 0
            remaining = binstr[22:]
            while n_bits_parsed < sub_length:
                l = len(remaining)
                value, remaining = parse(remaining, subpacket=True)
                n_bits_parsed += l-len(remaining)
                values.append(value)
            consumed += sub_length

        elif lengthid == 1:
            print("11 bit mode")
            n_sub = int(binstr[7:18],2)
            print("nsub", n_sub)
            consumed += 11
            remaining = binstr[18:]
            for i in range(n_sub):
                value, remaining = parse(remaining, subpacket=True)
                values.append(value)
            consumed += len(binstr[18:]) - len(remaining)

        value = fun(values)

    if not subpacket:
        return value, ""
        if consumed % 4 != 0:
            consumed += 4 - (consumed % 4)
    return value, binstr[consumed:]

def parse_lit(binstr, curr=""):

    print("group", binstr[1:5])

    if binstr[0] == "0":
        literal = int(curr+binstr[1:5], 2)
        print("literal", literal)
        return literal, binstr[5:]

    return parse_lit(binstr[5:], curr + binstr[1:5])

remaining = binary
while remaining:
    value, remaining = parse(remaining)
    print("final value", value)

