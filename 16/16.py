with open("input.txt", 'r') as f:
    lines = f.readlines()
    line = lines[0].strip()

#line = "D2FE28"
#line = "38006F45291200"
#line = "EE00D40C823060"
#line = "8A004A801A8002F478"
#line = "620080001611562C8802118E34"
#line = "C0015000016115A2E0802F182340"
#line = "A0016C880162017C3686B18A3D4780"

binary = bin(int(line, 16))[2:].zfill(4*len(line))

total = 0

def parse(binstr, subpacket=False):

    if subpacket:
        prefix = "    "
    else:
        prefix = ""

    print(binstr)
    if binstr == '':
        return ""

    consumed = 0

    version = int(binstr[0:3],2)
    consumed += 3
    print(prefix, "version", version)
    #if version == 0:
    #    return ""
    global total
    total += version
    typeid = int(binstr[3:6],2)
    print(prefix, "type", typeid)
    consumed += 3

    if typeid == 4:
        remaining_str = parse_lit(binstr[6:])
        consumed += len(binstr[6:]) - len(remaining_str)
    else:

        lengthid = int(binstr[6],2)
        consumed += 1

        if lengthid == 0:
            print(prefix, "15 bit mode")
            sub_length = int(binstr[7:22],2)
            print(prefix, "length", sub_length)
            consumed += 15
            n_bits_parsed = 0
            remaining = binstr[22:]
            while n_bits_parsed < sub_length:
                l = len(remaining)
                remaining = parse(remaining, subpacket=True)
                n_bits_parsed += l-len(remaining)
            consumed += sub_length

        elif lengthid == 1:
            print(prefix, "11 bit mode")
            n_sub = int(binstr[7:18],2)
            print(prefix, "nsub", n_sub)
            consumed += 11
            remaining = binstr[18:]
            for i in range(n_sub):
                print(i)
                remaining = parse(remaining, subpacket=True)
            consumed += len(binstr[18:]) - len(remaining)

    if not subpacket:
        return ""
        if consumed % 4 != 0:
            consumed += 4 - (consumed % 4)
    return binstr[consumed:]

def parse_lit(binstr, curr=""):

    print("group", binstr[1:5])

    if binstr[0] == "0":
        #return curr + binstr[1:5], binstr[6]
        print("literal", int(curr+binstr[1:5], 2))
        return binstr[5:]

    return parse_lit(binstr[5:], curr + binstr[1:5])

remaining = binary
while remaining:
    remaining = parse(remaining)


print("total version", total)
