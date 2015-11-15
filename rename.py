__author__ = 'Anshul'
import os
import yaml
import json
import cPickle as pickle
count=0
newFormats = {}
listODI=[]
listTest=[]
listT20=[]
listAllElse=[]
for eachfile in os.listdir("C:/Users/Anshul/Desktop/Courses/Data Science/Final Project/allMatches"):
     #with open("C:/Users/Anshul/Desktop/Courses/Data Science/Final Project/allMatches/" + eachfile, 'r') as stream:
    stream = open("C:/Users/Anshul/Desktop/Courses/Data Science/Final Project/allMatches/" + eachfile, 'r')
    for data in yaml.load_all(stream):
        format = data['info']['match_type']
        teamA = data['info']['teams'][0][:3]         #Ban
        teamB = data['info']['teams'][1][:3]         #Zim
        dateOfMatch = str(data['info']['dates'][0])  #2006-12-05
        matchKey = dateOfMatch + "_" + format + teamA + teamB    #OdiBanZim2006-12-05
        print matchKey
        stream.close()
        if format == "ODI":
            a= "C:/Users/Anshul/Desktop/Courses/Data Science/Final Project/allMatches/" + str(eachfile)
            b= "C:/Users/Anshul/Desktop/Courses/Data Science/Final Project/ODI/" + str(matchKey) + ".yaml"
            #os.rename("C:/Users/Anshul/Desktop/Courses/Data Science/Final Project/allMatches/" + str(eachfile), "C:/Users/Anshul/Desktop/Courses/Data Science/Final Project/ODI/" + str(matchKey) + ".yaml")
            os.rename(a,b)
            count = count+1
            listODI.append(str(matchKey))
            break
        elif format == "Test":
            a= "C:/Users/Anshul/Desktop/Courses/Data Science/Final Project/allMatches/" + str(eachfile)
            b= "C:/Users/Anshul/Desktop/Courses/Data Science/Final Project/Test/" + str(matchKey) + ".yaml"
            #os.rename("C:/Users/Anshul/Desktop/Courses/Data Science/Final Project/allMatches/" + str(eachfile), "C:/Users/Anshul/Desktop/Courses/Data Science/Final Project/ODI/" + str(matchKey) + ".yaml")
            os.rename(a,b)
            count = count+1
            listTest.append(str(matchKey))
            break
        elif format == "T20":
            a= "C:/Users/Anshul/Desktop/Courses/Data Science/Final Project/allMatches/" + str(eachfile)
            b= "C:/Users/Anshul/Desktop/Courses/Data Science/Final Project/T20/" + str(matchKey) + ".yaml"
            #os.rename("C:/Users/Anshul/Desktop/Courses/Data Science/Final Project/allMatches/" + str(eachfile), "C:/Users/Anshul/Desktop/Courses/Data Science/Final Project/ODI/" + str(matchKey) + ".yaml")
            os.rename(a,b)
            count = count+1
            listT20.append(str(matchKey))
            break
        else:
            if format not in newFormats:
                newFormats[format]=1
            else:
                newFormats[format]= newFormats[format] +1
            count = count+1
            a= "C:/Users/Anshul/Desktop/Courses/Data Science/Final Project/allMatches/" + str(eachfile)
            b= "C:/Users/Anshul/Desktop/Courses/Data Science/Final Project/allElse/" + str(matchKey) + ".yaml"
            os.rename(a,b)
            listAllElse.append(str(matchKey))
            continue

dictODI={'ODI':listODI}
dictTest={'Test':listTest}
dictT20={'T20':listT20}
dictAllElse={'AllElse':listAllElse}

pickle.dump(listODI,open("C:/Users/Anshul/Desktop/Courses/Data Science/Final Project/FormatListDumps/ODI.p", "wb"))
pickle.dump(listTest,open("C:/Users/Anshul/Desktop/Courses/Data Science/Final Project/FormatListDumps/Test.p", "wb"))
pickle.dump(listT20,open("C:/Users/Anshul/Desktop/Courses/Data Science/Final Project/FormatListDumps/T20.p", "wb"))
pickle.dump(listAllElse,open("C:/Users/Anshul/Desktop/Courses/Data Science/Final Project/FormatListDumps/AllElse.p", "wb"))
print "Finished processing files", count
print newFormats
