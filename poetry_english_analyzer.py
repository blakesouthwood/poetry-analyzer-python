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


'''
The two functions are beneath the poems.

 count_word_match()   counts the number of times a word is used in one large string
 
 search_for_phrase()  searches through dictionary for a phrase in lots of large strings

'''



homegardenerpoem = '''
Gray white-edged clouds
blow through the sky,
seemingly swept along
by dancing switches
of white blossoms:
quaint hearth brooms made from
our ancient plum, its pale green lichen
crusting its soft-gray limbs.
I hold on to the tree,
cautious from tripping
on gopher excavations.
I watch you down the years
tending the yard:  mowing,
weeding, raking, pruning.
Now It smells of new blooms:
roses, nasturtiums,
honey locust, Scotch broom.
Bright-blue stellar jays caw
in the oak. A neighbor’s
black and white cat startles at their squawks,
then rolls around in your freshly-weeded
rose-garden dirt as if it were catnip.
You stretch as you stand up,
and smile, satisfied with
the piles of weeds destined
for the compost, “found”
earthworms to circulate air too.
'''


theviewpoem = '''
Gray white-edged clouds
blow by,
switches
of white blossoms seeming to sweep them
along like quaint hearth brooms made from
ancient plum -- pale green lichen
crusting soft-gray limbs.
I hold on to you,
cautious from tripping.
Was the view always this clear?
Houses like white gift boxes
ribboned with waving greens,
rimmed on the far side by
slate-gray bay, camel hills and sky.
We stand on the edge
of the cliff every day.
I hang onto the plum’s rough trunk,
stare at the view...memorizing it with you.
'''

catpoem = '''
CAT AND I

My cat and I
sat on the stairs
leading to the front porch
last night
in a golden arc of light.
A cricket chirped in the thicket
of English ivy and light blue-green juniper
tangled around the bright white railing.

My entranced, long-haired cat,
purred as he sat on a steep step.
With the rhythmic throbs 
of the cricket’s sharp chirps
and my cat’s soothing purrs,
I was content.
'''



#  the dictionary definition needs to be above the functions but below the big strings
#  search through keys in dictionary
#  the dictionary must be above the functions to work
 
# ==== dictionary ====  

smalldictionary = {
  "cat": catpoem,
  "homegardener": homegardenerpoem,
  "theview": theviewpoem,
  }
  
  
# searches entire dictionary for a phrase(substring several words) that references large strings  
#####================================================
#           search for phrase          
#####================================================
def search_for_phrase(dname,phrase):
    for key in dname:                  #loops thru dictionary
        if phrase in dname.get(key): 
            print("winner " + "in " + key) 
        else:
            print(key +" no joy")        
   

dname = smalldictionary            #dictionary name
a_phrase = "ivy and light"         #phrase looking for

#calling function here
search_for_phrase(smalldictionary,a_phrase)         






# count number of times a word is used in a poem(big string)
# inputs are the poem(big string), and substring
# using a chain the methods lower() and count() are called 
# this searches fora substring within a large string
# This function is designed to count in one string at a time
# and could easily be incorporated into a loop to be used in the dictionary

#####===================================
##       count_word_match
#####===================================
def count_word_match(poem,substring):
    answer =eval("" + poem + ".lower().count('" + substring + "')")
    print(answer , "result for " , substring, "in", poem)
    return answer



#example of method call which prints and returns number of occurences
count_word_match("theviewpoem","tripping")



