import gneu
import math

def fst(n):
    return n[0]


def snd(n):
    return n[1]


def depth(n):
    if is_leaf(n):
        return 0

    return max(depth(fst(n)), depth(snd(n)))+1


def magnitude(n):
    if is_leaf(n):
        return n[0]

    return 3*magnitude(fst(n)) + 2*magnitude(snd(n))


def max_n(n):
    if is_leaf(n):
        return n[0]
    else:
        return max(max_n(fst(n)), max_n(snd(n)))


def is_reduced(n):
    return depth(n) <= 4 and max_n(n) < 10 


def is_leaf(n):
    return len(n) == 1


def listify(n):

    if isinstance(fst(n), int):
        n[0] = [n[0]]
    else:
        n[0] = listify(n[0])
    if isinstance(snd(n), int):
        n[1] = [n[1]]
    else:
        n[1] = listify(n[1])

    return n


def leftmost(n):
    if is_leaf(n):
        return n
    else:
        return leftmost(fst(n))


def rightmost(n):
    if is_leaf(n):
        return n
    else:
        return rightmost(snd(n))


def explode(n, left_neighbor=None, right_neighbor=None, parent=None, level = 1):

    if is_leaf(n):
        return False
    
    if is_leaf(fst(n)) and is_leaf(snd(n)):
        if level > 4:
            print("exploding", n)
            print("left neigh", left_neighbor)
            print("right neigh", right_neighbor)
            if left_neighbor != None:
                left_neighbor[0] += fst(n)[0]
            if right_neighbor != None:
                right_neighbor[0] += snd(n)[0]
            n.clear()
            n.append(0)
            return True
        else:
            return False

    #explode left
    exploded = explode(fst(n), left_neighbor, leftmost(snd(n)), n, level+1)
    
    #explode right
    if not exploded:
        exploded = explode(snd(n), rightmost(fst(n)), right_neighbor, n, level+1)

    return exploded

def split(n):

    if is_leaf(fst(n)) and fst(n)[0] > 9:
        n[0] = split_leaf(fst(n))
        return True

    #try to split right
    if is_leaf(snd(n)) and snd(n)[0] > 9:
        n[1] = split_leaf(snd(n))
        return True

    if not is_leaf(fst(n)):
        if split(fst(n)):
            return True
    if not is_leaf(snd(n)):
        return split(snd(n))

    return False


def split_leaf(n):
    assert is_leaf(n)

    n = n[0]
    left = int(math.floor(n/2.0))
    right = int(math.ceil(n/2.0))
    print("split", n, left, right)
    assert n == left + right

    return [[left], [right]]

def reduce(n):

    while not is_reduced(n):
        #print(depth(n), max_n(n))
        print(n)
        if depth(n) > 4:
            print("explode")
            explode(n)
            continue
        if max_n(n) > 9:
            print("split")
            split(n)
            continue

    return n


def add(n1,n2):
    n = [n1, n2]
    n = reduce(n)
    return n

def add_all(numbers):
    acc = numbers.pop(0)

    while numbers:
        print("#######################current", acc)
        acc = add(acc, numbers.pop(0))

    print(acc)
    return acc

#print(listify(gneu.numbers[0]))
n = [[[[[9,8],1],2],3],4]
n = [7,[6,[5,[4,[3,2]]]]]
n = [[6,[5,[4,[3,2]]]],1]
n = [[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]
n = [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]
n = listify(n)
#print(n)
#explode(n)
#print(n)
#print(leftmost(n))
#print(rightmost(n))

#n1 = listify([[[[4,3],4],4],[7,[[8,4],9]]])
#n2 = listify([1,1])
#n = add(n1,n2)
#print(n)

#print(max_n(n))

#print(is_reduced(n))
#n = reduce(n)
#print(n)
#print(is_reduced(n))
#print(depth(n))

#numbers = [listify(n) for n in gneu.numbers_example]
#print(numbers)

#n = add(numbers[0], numbers[1])

#n = add_all(numbers[0:5])
#n = add_all(numbers)
#print(n)
#print(magnitude(n))

n1 = [[[[7,0],[7,7]],[[7,7],[7,8]]],[[[7,7],[8,8]],[[7,7],[8,7]]]]
n2 = [7,[5,[[3,8],[1,4]]]]

n1 = [[[[7,7],[7,8]],[[9,5],[8,7]]],[[[6,8],[0,8]],[[9,9],[9,0]]]]
n2 = [[2,[2,2]],[8,[8,1]]]

n1 = [[[[6,6],[6,6]],[[6,0],[6,7]]],[[[7,7],[8,9]],[8,[8,1]]]]
n2 = [2,9]

n1 = [[[[6,6],[7,7]],[[0,7],[7,7]]],[[[5,5],[5,6]],9]]
n2 = [1,[[[9,3],9],[[9,0],[0,7]]]]

n1 = [[[[7,8],[6,7]],[[6,8],[0,8]]],[[[7,7],[5,0]],[[5,5],[5,6]]]]
n2 = [[[5,[7,4]],7],1]

n1 = [[[[7,7],[7,7]],[[8,7],[8,7]]],[[[7,0],[7,7]],9]]
n2 = [[[[4,2],2],6],[8,7]]

n = add(listify(n1),listify(n2))
print(n)
