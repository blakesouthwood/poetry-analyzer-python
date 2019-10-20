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


# list of poems will go there ... testing with three to start with


# Searches for substring phrase in multiple longstrings
# this searches for whether or not a phrase(substring) exists in a poem(big string)
# loop to search through each value in the dictionary based on the key

#import pdb; pdb.set_trace() #to use for debugging

'''

 count_word_match()   counts the number of times a word is used in one large string

 search_for_phrase()  searches through dictionary for a phrase in lots of large strings

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
 }

matching_list = []
# searches entire dictionary for a phrase(substring several words) that references large strings
#####================================================
##           search for phrase
#####================================================
def search_for_phrase(dname,phrase):
    matching_list.clear()             # need to empty list by default to start with to fix bug
    newphrase = "'" + phrase + "'"    # this adds a quote around the phrase
    count = 0
    for key in dname:                 # loops thru dictionary
        if phrase in dname.get(key):
            #print("match " + "in " + key)
            matching_list.append(key)  #this appends each match to end of list
            count += 1
    thelist = len(matching_list)        
    if thelist > 0:         #if there were matches print the list  
        if thelist == 1:
            print('there was', thelist,'match for',newphrase,'in poems')
        if thelist > 1:
            print('there were', thelist,'matches for',newphrase,'in poems')
        print(matching_list) 
        
    
    if count == 0: print("no matches for",newphrase,"in poems")  #this tests if no results 	

#testing searching for substring phrase in multiple strings

dname = smalldictionary            #dictionary name
a_phrase = "grandfather clock ticks"         #phrase looking for
length = len(smalldictionary)




# right here is what was here before


search_for_phrase(smalldictionary,"puddles of color")
print()
search_for_phrase(smalldictionary,"cat")
print()
search_for_phrase(smalldictionary,a_phrase)
print()
search_for_phrase(smalldictionary,"Trick or Treat")
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

