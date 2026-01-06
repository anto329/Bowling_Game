def bowling_game(game):
  frame=[]   #List to store pin values of each roll

   #Converting symbols to roll values
  for ch in game:
    if ch=="X":         #strike
      frame.append(10)
    elif ch=="-":        #miss
      frame.append(0)
    elif ch=="/":          #spare
      frame.append(10-frame[-1])
    else:                 #digits[0-9]
      frame.append(int(ch))

  score=0  #total score
  index=0   #points to current roll in frames
  for rolls in range(10):  #Calculate score for exactly 10 frames
    if frame[index]==10: #strike
      score=score+ 10 + frame[index+1] + frame[index+2]
      index+=1
    else:  #spare or open frame 
      sum=frame[index]+frame[index+1]
      if sum==10:    #spare
        score=score+10+frame[index+2]
      else:   #open frame
        score=score+sum
      index+=2
  return score


print(bowling_game("9-9-9-9-9-9-9-9-9-9-"))   # 90
print(bowling_game("XXXXXXXXXXXX"))         # 300
print(bowling_game("5/5/5/5/5/5/5/5/5/5/5")) # 150
