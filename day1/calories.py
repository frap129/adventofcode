input = open('input', 'r')

cur = (0, 0)
num1 = (0, 0)
num2 = (0, 0)
num3 = (0, 0)

def updateTopElves():
    global cur, num1, num2, num3
    if num1[1] < cur[1]:
        num3 = num2
        num2 = num1
        num1 = cur
    elif num2[1] < cur[1]:
        num3 = num2
        num2 = cur
    elif num3[1] < cur[1]:
        num3 = cur

    cur = (cur[0] + 1, 0)

for line in input:
    if line.isspace():
        updateTopElves()
        continue
    cur = cur[0], cur[1] + int(line)

updateTopElves()

top3Total = num1[1] + num2[1] + num3[1]
print("#1 Elf %d: %d calories" % num1)
print("#2 Elf %d: %d calories" % num2)
print("#3 Elf %d: %d calories" % num3)
print("Top 3 elves total calories: %d" % top3Total)
