from tqdm import tqdm

with open("input.txt", 'r') as f:
    line = f.readlines()[0].strip()

#line = "target area: x=20..30, y=-10..-5"

line = line.split(" ")
x = line[2].strip(",").split("=")[1].split("..")
y = line[3].split("=")[1].split("..")

x1, x2 = x
y1, y2 = y

target = (int(x1),int(x2),int(y1),int(y2))

def check_target(x,y,target):
    t = target
    #return x < t[1] and x > t[0] and y < t[3] and y > t[2]
    return x <= t[1] and x >= t[0] and y <= t[3] and y >= t[2]

def launch(dx, dy, max_it, target):
    x,y = 0,0
    maxy = -1000000
    success = False
    for i in range(max_it):
        x += dx
        y += dy

        if y > maxy:
            maxy = y

        if y < target[2] or x > target[1]:
    #        print("out of bounds", i)
            return False, maxy

        if check_target(x,y,target):
            print(i, maxy)
            return True, maxy

        if dx != 0:
            dx = dx-1 if dx>0 else dx+1
        dy -= 1

    #print("max iterations exceeded")
    return success, maxy

print(launch(5, 4, 1000, target))

sweep_x = range(0,int(x2)+1)
sweep_y = range(int(y1),1000)

sweep = [launch(x,y, 10000, target) for y in tqdm(sweep_y) for x in sweep_x]

sweep = list(filter(lambda x: x[0], sweep))
print(len(sweep))

maxy = max(sweep, key=lambda x: x[1])

print(maxy)

