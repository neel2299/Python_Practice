# Problem 6
def centuries(scores):
    one = 0
    for elem in scores:
        if elem >= 100:
            one += 1
    return one


def average_first_last(scores):
    n = len(scores)
    fir = scores[:n // 2]
    las = scores[n // 2:]
    avf = sum(fir) / len(fir)
    avl = sum(las) / len(las)
    if avf > avl:
        return ("first")
    else:
        return ("last")


def mode(scores):
    dic = {}
    for elem in scores:
        if elem in dic.keys():
            dic[elem] += 1
        else:
            dic[elem] = 1
    maxi, maxj = [], 0
    for (i, j) in dic.items():
        if j > maxj:
            maxj = j
            maxi = [i]
        elif j == max:
            maxi.append(i)
    maxi = sorted(maxi)
    return maxi[0]


print(mode([2, 2, 3, 3, 3]))

# Problem 5
count = 0
depth = 0
string = input()
for ch in string:
    if ch == "(":
        count += 1
    elif ch == ")":
        count -= 1
    if count < 0:
        break
    if depth < count:
        depth = count
if count == 0:
    print(depth)
else:
    print("Not matched")


# Problem 4

def identical(dic, val):
    lis = []
    if val not in dic.values():
        return -1
    for i, j in dic.items():
        if (j == val):
            lis.append(i)
    lis = sorted(lis)
    return lis[-1] - lis[0]


# Problem 3
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def value(self):
        return (self.x, self.y)

    def duplicate(self):
        pt = Point(self.x, self.y)
        return pt


# Problem 2
i = int(input())
j = int(input())
k = int(input())
s = 0
for p in range(i, j + 1):
    if p % k == 0:
        s += p
print(s)

# Problem 1
lis = list(map(int, input().split(" ")))
av = sum(lis) / len(lis)
lis2 = []
for i in range(len(lis)):
    if lis[i] > av:
        lis2.append(lis[i])
lis2 = sorted(lis2)
for i in range(len(lis2)):
    print(lis2[i], end=" ")


# Problem 2(C)
def makeprimelis(n):
    lis = []
    for i in range(2, n + 1):
        flag = False
        for j in range(2, i):
            if i % j == 0:
                flag = True
        if flag == False:
            lis.append(i)
    return lis


n = int(input())
lis = makeprimelis(n)
for elem in lis:
    if (elem + 2) in lis:
        print(elem, elem + 2, sep=',')

# Problem 1(C)
lis = list(map(int, input().split(",")))
s = sum(lis)
temps = 0
lis = sorted(lis)
# print(lis)
n = len(lis)
for i in range(n):
    temps += lis[n - i - 1]
    if ((temps - (s - temps)) > 0):
        print(i + 1)
        break
