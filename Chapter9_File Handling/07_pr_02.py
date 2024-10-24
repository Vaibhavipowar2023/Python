'''Q2. The game() function ina program lets a user play a game and returns the score as an integer . You need ot read file
'Hiscore.txt' which is either blank or contain the previous Hi-Score .
You need to write a program to  update the Hi score whenever game() breaks the Hi-score'''

def game() :
    return 56

score = game()
with open('hiscore.txt') as f:
    hiscorestr = f.read()

if int(hiscorestr)<score or hiscorestr == ' ':
    with open("hiscore.txt" ,'w') as f :
        f.write(str(score))

