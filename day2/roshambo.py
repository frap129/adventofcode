input = open('input', 'r')

score = 0
score2 = 0

def evalMatchPart1(line):
    global score
    winRock = line[0] == 'C' and line[2] == 'X'
    winPaper = line[0] == 'A' and line[2] == 'Y'
    winScissors = line[0] == 'B' and line[2] == 'Z'
    draw = (ord(line[0])) == (ord(line[2]) - 23)

    score += 6 if winRock or winPaper or winScissors else 0
    score += 3 if draw else 0
    score += 1 if line[2] == 'X' else 0
    score += 2 if line[2] == 'Y'  else 0
    score += 3 if line[2] == 'Z'  else 0

def evalMatchPart2(line):
    global score2
    win = line[2] == 'Z'
    draw = line[2] == 'Y'
    lose = line[2] == 'X'
    them = line[0]
    rock = (win and them == 'C') or (draw and them == 'A') or (lose and them == 'B')
    paper = (win and them == 'A') or (draw and them == 'B') or (lose and them == 'C')
    scissors = (win and them == 'B') or (draw and them == 'C') or (lose and them == 'A')

    score2 += 6 if win else 0
    score2 += 3 if draw else 0
    score2 += 1 if rock else 0
    score2 += 2 if paper else 0
    score2 += 3 if scissors else 0

for line in input:
    evalMatchPart1(line)
    evalMatchPart2(line)

print("Part 1 score is %d" % score)
print("Part 2 score is %d" % score2)
