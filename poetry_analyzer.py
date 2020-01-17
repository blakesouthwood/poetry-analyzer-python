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

# just added January 2020 searching for multiple words in a string in dictionary
# this is essentially a boolean and where each word in a list must exist within
# a string; in short this is searching for all substring words in a list inside of a dictionary
# that has strings for the data; succinctly find matching strings that contain 
# all substrings in a string in a dictionary. For the example it's searching through
# poems that all use a list of words


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
# this searches for phrase in dname (dictionary with poems)

def search_for_phrase(dname,phrase):       # search for phrase in smalldictionary and get result
    matching_list.clear()                  # need to empty list by default to start with an empty list
    newphrase = "'" + phrase + "'"         # this adds a quote around the phrase
    count = 0
                                           # sets counter to 0
    peach.clear()                          # start with empty peach list; peach holds
    for key in dname:  #loop  if phrase in dictionary
        if phrase.casefold() in dname.get(key).casefold():          #using casefold() for str1 == str2
            get_substring_location(phrase,dname.get(key))           #gets first location of substring in string and prints it
            apple =count_substring_in_string(phrase,dname.get(key)) #counts how many times the phrase occurs in string
            peach.append(apple)                                     #this adds the count(apple) of substrings within a poem in list peach
            matching_list.append(key)                               #this appends each match to end of list

    thelist = len(matching_list)
    if thelist > 0:                        #if there were matches print the list
        if thelist == 1:
            print(thelist,'match for',newphrase,'in poem')
        else:
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












#version 1 searching thru strings for list of substrings(words)

storage_list = []  #empty list that stores loc of matches in each poem

new_list = ['eucalyptus', 'crocheted', 'fragrance']
#make sure they are all lowercase for simplicity

result_list = []
def more_testing():    
    small_counter = 0
    print("length of dictionary = ", len(smalldictionary)) 
    print("new_list = ", new_list);
 
    
    #LOOP
    for value in smalldictionary.values(): #look thru all of them
        starbucks = value.lower();
        i = 0;
     
        
        result_list.clear()
        while i < len(new_list):
            if str(new_list[i]) in starbucks: #current poem value string
                result_list.append('True');
                i = i + 1
               
            else:
                result_list.append('False');
                i = i + 1
                
            
            if len(result_list) == len(new_list) and "False" not in result_list: #means all true
                print(" ALL TRUE meaning all matches in this poem")
                print("this is poem ",small_counter)
                print()
            else:
                pass
        small_counter += 1; 
                 
    
more_testing();









## Thursday, January 16, 2020
## version 2 seraching for strings that contain substrings from strings in a dictionary

###========search for multiple words from list of words thru searching in dictionary
new_list = ['horrible', 'dinosaur', 'treats', 'trick', 'treat', 'princess', 'candy', 'adam', 'eve'];
total_poems_matched = []
number_in_list_of_strings_searched = []
result_list = []
# find list of words in each string searching thru a dictionary of strings

##========================================================================
##   find_many_words_in_string  searches thru a dictionary of strings
##========================================================================


def find_many_words_in_string(): #searches thru entire dictionary could do millions of strings
    small_counter = 0
    print("length of dictionary = ", len(smalldictionary)) 
    print("new_list = ", new_list);
    for value in smalldictionary.values():    #loop thru each string and
        starbucks = value.lower();            #check if all words in list are in current string
        
        i = 0;
        result_list.clear() 
        while i < len(new_list):
             if str(new_list[i]) in starbucks: #current poem value string
                result_list.append('True');
                i = i + 1
             else:
               result_list.append('False');
               i = i + 1
                                                      #means all true
             if len(result_list) == len(new_list) and "False" not in result_list: 
                print(" All matches in this poem ", small_counter)
                number_in_list_of_strings_searched.append(small_counter)
                total_poems_matched.append('True');
                print()
             else:
                pass
        small_counter += 1; 
        number_of_poems = len(total_poems_matched)
    if len(total_poems_matched) > 0: #if one or more strings contained all of the substrings
        print("total poems that matched the substring list ",number_of_poems) 
        print("poem(strings) numbers in db that matched = ", number_in_list_of_strings_searched) 
    else:                            #if there weren't any matches of list of words in strings in dictionary 
        print()
        print("no matches in any strings in dictionary for all words in substring list")


find_many_words_in_string()










#find first occurence of substring in string
#this is only called if there is a match for the phrase in this particular string (poem)
#=========================================================
#=====       get_substring_location                =======
#=========================================================
'''
   this returns the location of the first occurence
   of the phrase substring in the string(poem)
   using the find method.

'''
#uses method find then appends it to storage.list

def get_substring_location(z,zen):          #string,phrase  THIS RETURNS THE LOCATION OF THE FIRST OCCURENCE only
    x= zen.casefold().find(z.casefold())    #this returns the number location of the substring inside of string
    storage_list.append(x);                 #puts x in storage_list[0] front far left of list
    return x;                               #ignoring case using .casefold()



















#=========================================================
#=====       count_substring_in_string()           =======
#=========================================================
'''
    this uses the count method to count the number of
    occurences(times) that this phrase is in each string(poem)

'''
def count_substring_in_string(z,zen):        #this COUNTS if multiple phrases  and returns the count
    c= zen.casefold().count(z.casefold())     #in one string (poem)
    return c;








###=============================
alpha = "merry christmas"
beta  = "merry chritmas"
charlie = "scrooge";

def compare_strings(x,y):
    print("x =",x, "y =",y)
    if (x.casefold() == y.casefold()):
       print('True');
       return True;
    else:
       print('False');
       return False;
     #end if
#end function









def test_compare(z,zz):
    answer = compare_strings(z,zz)
    print("answer = ",answer);





test_compare(alpha,beta); #called








#testing searching for substring phrase in multiple strings

dname = smalldictionary                 #dictionary name
a_phrase = "grandfather clock ticks"    #phrase looking for
length = len(smalldictionary)           #gets length of smalldictionary

#these are words searching for matches in all poems
#multiple word searches
search_list =['content', 'ivy', 'English', 'porch']
weasel =list(smalldictionary)[0]
money = poems.catpoem
#money2 = poems.homegardenerpoem

poetry_list = ["poems.catpoem", "poems.homegardenerpoem", 
   "poems.theviewpoem", "poems.december","poems.treebites",
    "poems.oldpath","poems.holmesappears","poems.nature_tankas",
    "poems.bellyflower_tanka_trio","poems.painting", "poems.snowballs",
    "poems.halloween","poems.shaky", "poems.honeylocustspring", "poems.einstein",
    "poems.pleasestayhome","poems.newyearsevekiss"]
  
#if I can search through one I can use eval to iterate through more than one






#january 15, 2020 new function
# this was my initial one.

# this example function only searches through one poem and not all of them

def search_for_many_words_in_string(po):
   
  
    fill_list = []; #empty list
    
    #for value in smalldictionary.values(): #this should go through all of the poems
    i = 0; j = 0;t =0;
    while i < len(search_list):
        for word in search_list:          #for loop for searching for one word
            if word in money:   #only searches in one poem
               
                test1 = 'True'
                j += 1;
                print("word=",word);
                i += 1;
                fill_list.append(test1)
            else:
                test1 = 'False'
                i += 1;
                fill_list.append(test1)


        print("fill_list=",fill_list);

        if 'False' not in fill_list: #meaning they are all true with ands
            print("they are all true")
            print("the words were ",search_list);
            print("the number of words tested was ", len(fill_list));
        if 'True' not in fill_list: #meaning they are all False
            print("None of the words were found in the poem")
        if 'True' in fill_list:
            print ("there were ",j ," words matched in the poem");

 





# ====================#
#  testing seaching for separate words within a poem like boolean word1 and word2
#  and then I will search thru all of the poems
#========






# this works looking for phrase in strings in dictionary of poems
# list of substring phrases to search for in dictionary of poems
phraselist =["puddles of color", "cat", "trick or treat",
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
        #search_all_poems_for_words_in_list(dname,search_list);
        print()





#=========================================================
#=====                   main()                    =======
#=========================================================
'''
 main() calls look_in_list() to do the search thru the list of poem strings
 for the matching and count of the substring phrases.
'''

def main():
    look_in_list();  #this calls the search
    count_word_match("poems.nature_tankas","mist")
    count_word_match("poems.honeylocustspring","honey locust")











#####===================================
##           count_word_match
#####===================================
'''
 Count number of times a word is used in a poem(big string)
 inputs are the poem(big string), and substring
 using a chain the methods lower() and count() are called
 this searches for a substring within a large string

 This function is designed to count in one string at a time
 and could easily be incorporated into a loop to be used in the dictionary
'''
def count_word_match(apoem,substring):
    print(apoem, substring)
    answer =eval("" + apoem + ".lower().count('" + substring + "')")
    print(answer , "result for " , substring, "in", apoem)

#there has to be at least one match in the string(poem) and then
#we should be able to figure out which poem it is.








if __name__ == '__main__':
    main()
