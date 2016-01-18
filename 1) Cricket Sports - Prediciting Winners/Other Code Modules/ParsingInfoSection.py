
# coding: utf-8

# In[2]:

import yaml
import os
import json
import csv

return_citys_country_Dict = {'Christchurch' : 'New Zealand','Johannesburg' : 'South Africa','Perth' : 'Australia','Fatullah' : 'Bangladesh','Skating and Curling Club' : 'Canada','Ayr' : 'Scotland','Mirpur' : 'Bangladesh','Bloemfontein' : 'South Africa','Abu Dhabi' : 'United Arab Emirates','Delhi' : 'India','Queenstown Events Centre' : 'New Zealand','Khulna' : 'Bangladesh','Kochi' : 'India','Sydney Cricket Ground' : 'Australia','Hamilton' : 'Canada','Sind' : 'Pakistan','Ahmedabad' : 'India','Dominica' : 'West Indies','Mombasa Sports Club Ground' : 'Kenya','St Vincent' : 'West Indies','King City' : 'Canada','Chittagong' : 'Bangladesh','Dublin' : 'Ireland','Nagpur' : 'India','Gwalior' : 'India','Nelson' : 'New Zealand','Antigua' : 'West Indies','Dunedin' : 'New Zealand','Jamaica' : 'West Indies','Kanpur' : 'India','Brisbane' : 'Australia','Sheikhupura Stadium' : 'Pakistan','Benoni' : 'South Africa','Nottingham' : 'England','Sharjah Cricket Stadium' : 'United Arab Emirates','Manchester' : 'England','Visakhapatnam' : 'India','Hambantota' : 'Sri Lanka','Ranchi' : 'India','Auckland' : 'New Zealand','Kolkata' : 'India','Lincoln' : 'England','Centurion' : 'South Africa','Chester-le-Street' : 'England','Edinburgh' : 'Scotland','Rajkot' : 'India','Kuala Lumpur' : 'Malaysia','Leeds' : 'England','London' : 'England','Bangalore' : 'India','Karachi' : 'Pakistan','Southampton' : 'England','Cape Town' : 'South Africa','Cuttack' : 'India','Chennai' : 'India','Hyderabad' : 'India','Dharmasala':'India','Dharamsala' : 'India','Margao' : 'India','Sharjah Cricket Association Stadium' : 'United Arab Emirates','Aberdeen' : 'Scotland','Belfast' : 'Ireland','Mount Maunganui' : 'New Zealand','Vadodara' : 'India','Lahore' : 'Pakistan','Pune' : 'India','Durban' : 'South Africa','Jaipur' : 'India','Faisalabad' : 'Pakistan','Napier' : 'New Zealand','Hobart' : 'Australia','Toronto' : 'Canada','Chittagong Divisional Stadium' : 'Bangladesh','Dubai Sports City Cricket Stadium' : 'United Arab Emirates','Wellington' : 'New Zealand','Bogra' : 'Bangladesh','Grenada' : 'West Indies','Nairobi' : 'Kenya','Whangarei' : 'New Zealand','Dubai International Cricket Stadium' : 'United Arab Emirates','Canberra' : 'Australia','Melbourne Cricket Ground' : 'Australia','Birmingham' : 'England','Guwahati' : 'India','Barbados' : 'West Indies','Trinidad' : 'West Indies','Pallekele International Cricket Stadium' : 'Sri Lanka','Mumbai' : 'India','Port Elizabeth' : 'South Africa','Dubai' : 'United Arab Emirates','Rangiri Dambulla International Stadium' : 'Sri Lanka','Darwin' : 'Australia','Glasgow' : 'Scotland','Chandigarh' : 'India','St Kitts' : 'West Indies','Bulawayo' : 'Zimbabwe','Adelaide Oval' : 'Australia','East London' : 'South Africa','Kimberley' : 'South Africa','Multan Cricket Stadium' : 'Pakistan','St Lucia' : 'West Indies','Potchefstroom' : 'South Africa','Bristol' : 'England','Guyana' : 'West Indies','Indore' : 'India','Paarl' : 'South Africa','Amstelveen' : 'Netherlands','Harare Sports Club' : 'Zimbabwe','Colombo' : 'Sri Lanka','Cardiff' : 'England'}
print return_citys_country_Dict['Dharmasala']

#eachfile = "2006-11-01_ODIAusNew.yaml"
count = 0
file = open('C:/Users/Anshul/Desktop/test.txt', "w")
every_row_in_csv_as_list = ['file_name','match_type','data','teamA','teamB','who_played_first','who_played_second','neutral_venue','city','home_ground_of_team','venue','winner','winner_by_runs','winner_by_wickets','toss_winner','toss_winner_decided_to','umpire_1','umpire_2','player_of_match']
#Write the headings
for i in range(len(every_row_in_csv_as_list)-1):
    file.write(str(every_row_in_csv_as_list[i])+':')
file.write(str(every_row_in_csv_as_list[len(every_row_in_csv_as_list)-1]) + '\n' )

#delete all the elements in the list
del every_row_in_csv_as_list[:]

#Let's do for all the files-
dummy_count =0
for eachfile in os.listdir("C:/Users/Anshul/Desktop/Courses/Data Science/Final Project/ODI"):
    dummy_count = dummy_count+1
        
    with open("C:/Users/Anshul/Desktop/Courses/Data Science/Final Project/ODI/" + eachfile, 'r') as stream:
            for data in yaml.load_all(stream):
                every_row_in_csv_as_list=[]
                infoDict = data['info']
                match_type = infoDict['match_type']
                date = str(infoDict['dates'][0])    
                teamA = infoDict['teams'][0]       
                teamB = infoDict['teams'][1]          
                neutral_venue = 'no'           
                city = 'NA'
                home_ground_of_team = 'none'
                venue = 'NA'           
                winner = 'no result' #infoDict['outcome']['winner']
                winner_by_runs = 'NA' 
                winner_by_wickets = 'NA'

                toss_winner = infoDict['toss']['winner']
                toss_winner_decided_to = infoDict['toss']['decision']
                umpire_1 = infoDict['umpires'][0]
                umpire_2 = infoDict['umpires'][1]
                player_of_match = 'NA' #infoDict['player_of_match'][0]
                
                if infoDict.has_key('player_of_match'):
                    player_of_match = infoDict['player_of_match'][0]

                if infoDict.has_key('city'):
                    city = infoDict['city']
                    venues_country = return_citys_country_Dict[city]
                
                if infoDict.has_key('venue'):
                    venue = infoDict['venue']
                    if city=='NA':
                        venues_country = return_citys_country_Dict[venue]
                    
                if infoDict.has_key('neutral_venue'):
                    neutral_venue = 'yes'

                #Teams HomeGround
                if neutral_venue == 'yes':
                    home_ground_of_team = 'none'
                else:
                    if venues_country == teamA:
                        home_ground_of_team = teamA
                    elif venues_country == teamB:
                        home_ground_of_team = teamB
                print venues_country
                print home_ground_of_team
                
                
                #Condition when there is no outcome of the match
                if not infoDict['outcome'].has_key('result'):
                    winner = infoDict['outcome']['winner']
                    
                
                if winner != 'no result' and infoDict['outcome']['by'].has_key('runs'):
                    winner_by_runs = str(infoDict['outcome']['by']['runs'])

                if winner != 'no result' and infoDict['outcome']['by'].has_key('wickets'):
                    winner_by_wickets = str(infoDict['outcome']['by']['wickets'])
                
                count = count+1
                print count
                if toss_winner == teamA:
                    if toss_winner_decided_to == 'field':
                        who_played_first = teamB
                        who_played_second = teamA
                    else:
                        who_played_first = teamA
                        who_played_second = teamB
                else:
                    if toss_winner_decided_to == 'field':
                        who_played_first = teamA
                        who_played_second = teamB
                    else:
                        who_played_first = teamB
                        who_played_second = teamA
                        
                every_row_in_csv_as_list.append(eachfile)
                every_row_in_csv_as_list.append(match_type)
                every_row_in_csv_as_list.append(date)
                every_row_in_csv_as_list.append(teamA)
                every_row_in_csv_as_list.append(teamB)
                every_row_in_csv_as_list.append(who_played_first)
                every_row_in_csv_as_list.append(who_played_second)
                every_row_in_csv_as_list.append(neutral_venue)
                every_row_in_csv_as_list.append(city)
                every_row_in_csv_as_list.append(home_ground_of_team)
                every_row_in_csv_as_list.append(venue)
                every_row_in_csv_as_list.append(winner)
                every_row_in_csv_as_list.append(winner_by_runs)
                every_row_in_csv_as_list.append(winner_by_wickets)
                every_row_in_csv_as_list.append(toss_winner)
                every_row_in_csv_as_list.append(toss_winner_decided_to)
                every_row_in_csv_as_list.append(umpire_1)
                every_row_in_csv_as_list.append(umpire_2)
                every_row_in_csv_as_list.append(player_of_match)

                for i in range(len(every_row_in_csv_as_list)-1):
                    file.write(str(every_row_in_csv_as_list[i])+':')
                file.write(str(every_row_in_csv_as_list[len(every_row_in_csv_as_list)-1]) + '\n')

                del every_row_in_csv_as_list[:]
            


            
#             print 'who_played_first' + ' : ' + who_played_first
#             print 'who_played_second' + ' : ' + who_played_second
#             print 'umpire_1' + ' : ' + umpire_1
#             print 'umpire_2' + ' : ' + umpire_2
#             print 'player_of_match' + ' : ' + player_of_match 
            
            #             print 'match_type' +' : '+ match_type
#             print 'file_name' + ' : '+ eachfile
#             print 'date' + ' : ' + date
#             print 'teamA' + ' : ' + teamA
#             print 'teamB' + ' : ' + teamB
#             print 'toss_winner' + ' : ' + toss_winner
#             print 'toss_winner_decided_to' + ' : ' + toss_winner_decided_to


file.close()

