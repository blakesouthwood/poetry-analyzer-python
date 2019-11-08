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
peach = []   #empty list to have count inside of it






# searches entire dictionary for a phrase(substring several words) that references large strings
#####================================================
##           search for phrase
#####================================================
'''
inputs substring and string
search for substring in strings from list in dictionary
find location of first substring in a string
count number of substring in each string
'''

def search_for_phrase(dname,phrase):       # search for phrase in smalldictionary and get result
    matching_list.clear()                  # need to empty list by default to start with an empty list
    newphrase = "'" + phrase + "'"         # this adds a quote around the phrase
    count = 0     
    #breakpoint()                         # sets counter to 0
    peach.clear()                          # start with empty peach list; peach holds
    for key in dname:  #loop
        if phrase.casefold() in dname.get(key).casefold(): #using casefold() for str1 == str2
            get_substring_location(phrase,dname.get(key))  #gets first location of substring in string and prints it
            apple =count_substring_in_string(phrase,dname.get(key)) #counts how many times the phrase occurs in string
            peach.append(apple)                            #this adds the count(apple) of substrings within a poem in list peach
            matching_list.append(key)                      #this appends each match to end of list

    thelist = len(matching_list)
    if thelist > 0:                        #if there were matches print the list
        if thelist == 1:
            print(thelist,'match for',newphrase,'in poem')

        if thelist > 1:
            print(thelist,'matches for',newphrase,'in poems')

        if len(matching_list) > 0:         #prints list of phrase locations in string of each poem
            counter= 0
            for item in matching_list:     #loop
               if peach[counter] > 1:      #this is the count of the phrase occurence in this string(poem)
                  print(matching_list[counter],"at loc",storage_list[counter], ", occurs",peach[counter], "times")
               else:
                  print(matching_list[counter],"at loc",storage_list[counter])

               count   += 1
               counter += 1
        storage_list.clear()               #clears out storage of locations of substring for poems
    if count == 0: print("no matches for",newphrase,"in poems")  #this tests if no results











storage_list = []  #empty list that stores loc of matches in each poem

#find first occurence of substring in string
#this is only called if there is a match for the phrase in this particular string (poem)
#=========================================================
#=====       get_substring_location                =======
#=========================================================
'''
   this return the location of the first occurence
   of the phrase substring in the string(poem)
   using the find method.

'''
def get_substring_location(z,zen):          #string,phrase  THIS RETURNS THE LOCATION OF THE FIRST OCCURENCE only
    x= zen.casefold().find(z.casefold())    #this returns the number location of the substring inside of string
    storage_list.append(x);                 #puts x in storage_list[0]
    return x;                               #ignoring case using .casefold()









#=========================================================
#=====       count_substring_in_string()           =======
#=========================================================
'''
    this uses the count method to count the number of 
    occurences(times) that the phrase is in each string(poem)
    
'''
def count_substring_in_string(z,zen):  #this COUNTS if multiple phrases in one string (poem) and returns the count
    c= zen.casefold().count(z.casefold())
    return c;











#testing searching for substring phrase in multiple strings

dname = smalldictionary                 #dictionary name
a_phrase = "grandfather clock ticks"    #phrase looking for
length = len(smalldictionary)           #gets length of smalldictionary



# search for phrase in smalldictionary
# make each lowercase for matching - convert beforehand



# list of substring phrases to search for in dictionary of poems
phraselist =["puddles of color", "cat",a_phrase, "trick or treat",
             "ancient plum", "honey locust", "shriveling flower",
             "deep breath", "trick or treat", "do not care",
             "time is endless", "coleman light", "down the years",
             "sighing leaves", "we stroll along" ]




#=========================================================
#=====               look_in_list()                =======
#=========================================================
'''
    this goes thru the phrase list in a loop and 
    calls search_for_phrase() to find the location
    and number of occurences in each poem of the phrase
    the list of phrases is just above called phraselist
'''

def look_in_list():
    print()
    for item in phraselist:  #loop thru phraselist above of phrases
        search_for_phrase(smalldictionary,item)
        print()
    

look_in_list();  #this calls the search 












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

#there has to be at least one match in the string(poem) and then
#we should be able to figure out which poem it is.


# calling function here
# example of method call which prints and returns number of occurences
count_word_match("poems.nature_tankas","mist")
count_word_match("poems.honeylocustspring","honey locust")
