
# coding: utf-8

# In[1]:

import yaml
stream = open("C:/Users/Anshul/Desktop/Courses/Data Science/Final Project/ODI/2006-12-05_ODIBanZim.yaml", 'r')
for data in yaml.load_all(stream): 
    
    #Teams involved?
    teamA = data['info']['teams'][0]; teamB = data['info']['teams'][1]
    #print teamA, teamB
    
    #Who batted first innings and who played the second?
    teamPlayingFirst = data['innings'][0]['1st innings']['team']
    #print teamPlayingFirst
    teamPlayingSecond = (teamB if teamPlayingFirst == teamA else teamA)  #Obviously the other team will play second
    #print teamPlayingSecond
    
    #Who was the winner?
    teamWhoWon = data['info']['outcome']['winner']
    #print teamWhoWon
    
    #By How many Runs or wickets? Let's keep the result in winnerLine for displaying on Plot
    if data['info']['outcome']['by'].has_key('runs'):
        byRuns = data['info']['outcome']['by']['runs']
        winnerLine = teamWhoWon + " won by " + str(byRuns) + " Runs"
        #print winnerLine 
    else:
        byWickets = data['info']['outcome']['by']['wickets']
        winnerLine = teamWhoWon + " won by " + str(byWickets) + " wickets"
        #print winnerLine
    
    #First Innings Begins
    i=0; overTotal=0; score=0; overList1=[]; runPerOverList1=[]; scoreSoFar1=[]; wicketOver1=[]; scoreOnFallOfWicket1=[]
    
    #Let's keep track of ball. We do not want to miss the scores of last Over
    lastBowl = len(data['innings'][0]['1st innings']['deliveries']); ballCounter=0
    
    #Now let's compute over by over score, ball by ball addition
    for ball in data['innings'][0]['1st innings']['deliveries']:
        over = int(ball.keys()[0])
        runOnBall = ball[ball.keys()[0]]['runs']['total']
        if(i == over):
            overTotal = overTotal + runOnBall
        else:
            overList1.append(i+1)
            i=over
            runPerOverList1.append(overTotal)
            score = score + overTotal
            scoreSoFar1.append(score)
            overTotal=runOnBall
        ballCounter = ballCounter + 1 
        if ballCounter == lastBowl:   #Covers the case of including runs from last over
            overList1.append(i+1)
            runPerOverList1.append(overTotal)
            score = score + overTotal
            scoreSoFar1.append(score)
        
        #To keep track of Fall of wickets and the corresponding score at that time
        if (ball[ball.keys()[0]].has_key('wicket')):
            wicketOver1.append(over)
            scoreOnFallOfWicket1.append(scoreSoFar1[over-1]+5)

    
    #2nd Innings begins
    i=0; overTotal=0; score=0; overList2=[]; runPerOverList2=[]; scoreSoFar2=[]; wicketOver2=[]; scoreOnFallOfWicket2=[]
    
    #Let's keep track of ball. We do not want to miss the scores of last Over
    lastBowl = len(data['innings'][1]['2nd innings']['deliveries']); ballCounter=0
    
    #Now let's compute over by over score, ball by ball addition
    for ball in data['innings'][1]['2nd innings']['deliveries']:
        over = int(ball.keys()[0])
        runOnBall = ball[ball.keys()[0]]['runs']['total']
        if(i == over):
            overTotal = overTotal + runOnBall
        else:
            overList2.append(i+1)
            i=over
            runPerOverList2.append(overTotal)
            score = score + overTotal
            scoreSoFar2.append(score)
            overTotal=runOnBall
        ballCounter = ballCounter + 1 
        if ballCounter == lastBowl:   #Covers the case of including runs from last over
            overList2.append(i+1)
            runPerOverList2.append(overTotal)
            score = score + overTotal
            scoreSoFar2.append(score)
        
        #To keep track of Fall of wickets and the corresponding score at that time
        if (ball[ball.keys()[0]].has_key('wicket')):
            wicketOver2.append(over)
            scoreOnFallOfWicket2.append(scoreSoFar2[over-1]+5)  #Adding 5 to make the red dots visible clearly

#Let's Plot the result.            
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import matplotlib.patches as mpatches
style.use('fivethirtyeight')

fig=plt.figure(figsize=(12,8))
fig.suptitle('Match Summary for the match between '+ teamPlayingFirst +" and "+teamPlayingSecond +"\n"+ winnerLine, fontsize=15)
ax1=fig.add_subplot(1,1,1)

ax1.clear()
ax1.plot(overList1,scoreSoFar1, c='green')
ax1.scatter(wicketOver1,scoreOnFallOfWicket1, s=100,c='red', alpha=0.5)

ax1.plot(overList2,scoreSoFar2, c='blue')
ax1.scatter(wicketOver2,scoreOnFallOfWicket2, s=100,c='red', alpha=0.5)
ax1.set_autoscale_on(False)

#Fixing the axis
x=max(overList1[len(overList1)-1],overList2[len(overList2)-1])
y=max(scoreSoFar1[len(scoreSoFar1)-1],scoreSoFar2[len(scoreSoFar2)-1])+30
ax1.axis([0.0,x, 0.0,y])
ax1.set_xlabel('Overs',fontsize=15, color='r')
ax1.set_ylabel('Score',fontsize=15, color='r')

#Let's show the graph
plt.legend( (teamPlayingFirst, teamPlayingSecond, 'Wicket'), fontsize=14, loc='upper left')

plt.show()

