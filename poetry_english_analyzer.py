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


#list of poems will go there ... testing with three to start with
smalldict = {
  "cat":   catpoem,
  "lemon": lemonpoem,
  "tree":  treebites,
  }



 #phrase for the substring  that will be searched
a_phrase = "ivy and light"

# Searches for substring phrase in multiple longstrings
# this searches for whether or not a phrase(substring) exists in a poem(big string)
# loop to search through each value in
#the dictionary based on the key

def search_for_phrase(dname,a_phrase):
    for key in smalldict:
        if a_phrase in smalldict.get(key): 
            print("winner " + "in " + key) 
        else:
            print(key +" no joy")          
   

#sample calling the function to return number of phrase matches in a given dictionary
search_for_phrase(smalldict,a_phrase)  #(dictionary_name, phrase_substring)


# count number of times a word is used in a poem(big string)
# inputs are the poem(big string), and substring
# using a chain the methods lower() and count() are called 
def count_word_match(poem,substring):
    answer =eval("" + poem + ".lower().count('" + substring + "')")
    print(answer)
    return answer

#example of method call which prints and returns 3
count_word_match("treebites","leaves")



#poetry bigstrings below that are initially analyzed for a substring phrase

treebites = '''
Tree Bites

A eucalyptus branch scared the
bejesus out of me on a sweaty summer day,
when it landed next to where I stood with a rush of
wind and its leaves rustling on dark soft earth.

This old thick tree has wind-peeled bark --
stiff curling strips that crunch underfoot.
Its lofty top sways fragrant
twilight-tinted leaves.
It hosts myriad hummingbirds,
an iridescent swirl of dazzling blues and greens.
They whiz around, up and down,
tasting tangerine geraniums and worrying my eyes
with their needle-sharp beaks and whirring thrums.

My son, topping the tree
among sighing leaves,
twice heard a living creature utter
“Unh-UNH-unh” after he drew a saw
through branches soft as butter.
He scrambled to the ground, a curious
look on his face.

His legs started itching
in three days.
The tree’s teeth
turned out to be at its base.
The tree’s teeth have a name.
It is POISON OAK.
My son scratched as he shouted,
“I’ll be ready for you next time!”
'''


lemonpoem ='''

UBIQUITOUS  LEMON BALM   8/97

 We have lemon herbs
 in our garden -
 thyme, verbena
 and “creeping” balm
 that sneaks along under
 the ground,
 rooting haphazardly through
 chamomile, pennyroyal, or rue,
 and, no doubt,
 the neighbors’ yards too,
 ubiquitous as comfrey
 or bamboo.
 Year after year
 we try to dispose
 of the volunteers of balm.
 Lemon verbena and thyme
 grow where they’re planted,
 scent our linen,
 or add flavor to chicken,
 but lemon balm
 spreads like an epidemic,
 its downy, mint-green leaves
 like tiny profile cutouts
 of sugar-maple trees,
 on tough-as-a-chain, square stems,
 impossible to break.
 In some ways, though, it’s a delicacy:
 It blooms in your mouth,
 and makes fragrant tea.

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
