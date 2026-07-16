print("hello world")

i = 1
print(f"i={i}")
f = 0.24
print(f"f={f}")
c = 'a'
print(f"c={c}")

i,j = 10,3

# 加算
sum = i+j
# 減算
sub = i-j
# 乗算
mul = i*j
# 除算
div = i/j

i,j = True,False

# AND
AND = i and j
# OR
OR = i or j
# NOT
NOT = not i

i = 0b1001
j = 0b1010
# AND
AND = i & j
# OR
OR = i | j
# XOR
XOR = i ^ j
# NOT
NOT = ~ i

i = 0b00100
# right bit shift
Rshift = i >> 2
# left bit shift
Lshift = i << 2

j = 20
# mod
i = j % 3

a,b = 3,4

if a == b:
    # 等しい
    print("is equal")
else:
    # 等しくない
    print("is not equal")

count = 0
while count < 10:
    print("hello world")
    count += 1

for count in range(10):
    print("hello world")

def add(i,j):
    return i+j

a = [1,4,3]

for i in a:
    print(f"{i}")
    # 1 4 3