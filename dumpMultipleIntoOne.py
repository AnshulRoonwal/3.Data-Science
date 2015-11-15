__author__ = 'Anshul'
import yaml
import os
import cPickle as pickle
dictODI={}
listODI=[]
for eachfile in os.listdir("C:/Users/Anshul/Desktop/Courses/Data Science/Final Project/ODI"):
    stream = open("C:/Users/Anshul/Desktop/Courses/Data Science/Final Project/ODI/" + eachfile, 'r')
    for data in yaml.load_all(stream):
        dictODI[eachfile] = data
        listODI.append(eachfile)
pickle.dump(dictODI,open("C:/Users/Anshul/Desktop/Courses/Data Science/Final Project/FormatListDumps/ODIDump.p", "wb"))
print listODI
stream.close()