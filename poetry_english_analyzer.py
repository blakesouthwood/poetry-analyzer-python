# October 7, 2019 Gilroy, California
# Blake Southwood
# the idea for this project stemmed from a request from
# my mother a poet that wanted to check if she had used a phrase in her poems
# collection previously. I decided to recreate the Poetry Database in Python
# along with it's unique search characteristics.

# Analyzing English focusing on poetry first
# I decided to analyze hundreds of poems to master everything
# with strings and analysis of English
# I'm starting by analyzing 3 poems before searching through hundreds


# Searches for substring phrase in multiple longstrings
# this searches for whether or not a phrase(substring) exists in a poem(big string)
# loop to search through each value in the dictionary based on the key


'''

 count_word_match()        counts the number of times a word is used in one large string

 search_for_phrase()       searches through dictionary for a phrase in lots of large strings
 
 get_substring_location()  returns the location of first character of substring in string

'''

# module with all of the poems stored as strings
import poems


# ==== dictionary ====

smalldictionary = {                     # each poem is a long string stored in module poems
  "cat":           poems.catpoem,       # so each poem has a prefix of poems referencing the module.
  "homegardener":  poems.homegardenerpoem,
  "theview":       poems.theviewpoem,
  "december":      poems.december,
  "treebites":     poems.treebites,
  "oldpath":       poems.oldpath,
  "holmes":        poems.holmesappears,
  "nature":        poems.nature_tankas,
  "bellyflower":   poems.bellyflower_tanka_trio,
  "paintings":     poems.painting,
  "snowballs":     poems.snowballs,
  "pumpkins":      poems.halloween,
  "shaky":         poems.shaky,
  "honeylocust":   poems.honeylocustspring,
  "einstein":      poems.einstein,
  "stayhome":      poems.pleasestayhome,
  "newyears":      poems.newyearsevekiss,
 }

matching_list = []  #empty list
# searches entire dictionary for a phrase(substring several words) that references large strings
#####================================================
##           search for phrase
#####================================================
def search_for_phrase(dname,phrase):       # search for phrase in smalldictionary and get result
    #phrase = phrase.lower() #this is new
    matching_list.clear()                  # need to empty list by default to start with an empty list
    newphrase = "'" + phrase + "'"         # this adds a quote around the phrase
    count = 0                              # sets counter to 0
     
    for key in dname:     
        if phrase.casefold() in dname.get(key).casefold(): #using casefold() for str1 == str2
            get_substring_location(phrase,dname.get(key))  #gets location of substring in string and prints it
            matching_list.append(key)                      #this appends each match to end of list
            count += 1
         
    thelist = len(matching_list)
    if thelist > 0:                        #if there were matches print the list
        if thelist == 1:
            print(thelist,'match for',newphrase,'in poem')
        if thelist > 1:
            print(thelist,'matches for',newphrase,'in poems')
           
        if len(matching_list) > 0:         #prints list of phrase locations in string of each poem
            counter= 0
            for item in matching_list:
               print(matching_list[counter],"at loc",storage_list[counter])
               counter += 1
               
        storage_list.clear()               #clears out storage of locations of substring for poems
                                           #this tests if no results
    if count == 0: print("no matches for",newphrase,"in poems")  
    
    
    

    
storage_list = []  #empty list that stores loc of matches in each poem 

#find first occurence of substring in string
#this is only called if there is a match for the phrase in this particular string (poem)
#=========================================================
#=====       get_substring_location                =======
#=========================================================

def get_substring_location(z,zen):
    x= zen.casefold().find(z.casefold())    #this returns the number location of the substring inside of string
    storage_list.append(x);                 #puts x in storage_list[0] 
    return x;                               #ignoring case using .casefold()



#testing searching for substring phrase in multiple strings

dname = smalldictionary                 #dictionary name
a_phrase = "grandfather clock ticks"    #phrase looking for
length = len(smalldictionary)           #gets length of smalldictionary



#search for phrase in smalldictionary
#make each lowercase for matching - convert beforehand
#add this tomorrow when I have more time 
search_for_phrase(smalldictionary,"puddles of color")
print()
search_for_phrase(smalldictionary,"cat")
print()
search_for_phrase(smalldictionary,a_phrase)
print()
search_for_phrase(smalldictionary,"Trick or Treat")
print()
search_for_phrase(smalldictionary,"ancient plum")
print()
search_for_phrase(smalldictionary,"honey locust")
print()
search_for_phrase(smalldictionary,"shriveling flower")
print()
search_for_phrase(smalldictionary,"deep breath")
print()
search_for_phrase(smalldictionary,"kiss on the chime")
print()
search_for_phrase(smalldictionary,"do not care")
print()
search_for_phrase(smalldictionary,"time is endless")
print()
#this should count the number of times a phrase exists in a poem
#def testing_phrase_search(thepoem,thephrase):
#   answer = count(thephrase)

#testing_phrase_search(poems.nature_tankas,"Coleman light")

print()
print()



# try using string.casefold()
string  = poems.nature_tankas
substring = "we jogged on"

count = string.count(substring)


# print count
print( substring,"is in", "poems.nature_tankas ", count, " times")












'''
 Count number of times a word is used in a poem(big string)
 inputs are the poem(big string), and substring
 using a chain the methods lower() and count() are called
 this searches for a substring within a large string

 This function is designed to count in one string at a time
 and could easily be incorporated into a loop to be used in the dictionary
'''
#####===================================
##       count_word_match
#####===================================
def count_word_match(apoem,substring):
    print(apoem, substring)
    answer =eval("" + apoem + ".lower().count('" + substring + "')")
    print(answer , "result for " , substring, "in", apoem)



# calling function here
# example of method call which prints and returns number of occurences
count_word_match("poems.nature_tankas","mist")
