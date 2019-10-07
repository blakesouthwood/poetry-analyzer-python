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
# this is an example DICTIONARY with keys and values, the values are actually large strings

# ==== dictionary ====
smalldict = {
  "cat":   catpoem,
  "lemon": lemonpoem,
  "tree":  treebites,
  "memories": memoriespoem,
  "december": decemberpoem,
  "theview":  theviewpoem,
  "parkinsons": parkinsonspoem,
  "homegardner": homegradernerpoem,
  "holmesappears": holmeasappearspoem,
  "oldpath":  oldpathpoem,
  "theview":  theviewpoem,
  }





#####====== this is the substring phrase

 #phrase for the substring  that will be searched
a_phrase = "ivy and light"




# Searches for substring phrase in multiple longstrings
# this searches for whether or not a phrase(substring) exists in a poem(big string)
# loop to search through each value in
# the dictionary based on the key


#####===================================
##          search_for_phrase
#####===================================
def search_for_phrase(dname,phrase):
    for key in dname: 
        if phrase in dname.get(key): 
            print("winner " + "in " + key) 
        else:
            print(key +" no joy")        
   

dname    = smalldict            #dictoinary name
a_phrase = "ivy and light"      #phrase looking for

#calling function here
search_for_phrase(smalldict,a_phrase)         
   










# count number of times a word is used in a poem(big string)
# inputs are the poem(big string), and substring
# using a chain the methods lower() and count() are called 
# this searches fora substring within a large string

#####===================================
##       count_word_match
#####===================================

def count_word_match(poem,substring):
    answer =eval("" + poem + ".lower().count('" + substring + "')")
    print(answer)
    return answer



#example of method call which prints and returns 3
count_word_match("treebites","leaves")


#### sample large strings below which happen to be real poems
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




memoriespoem = '''

MEMORIES
Jan. 12, 2000


The widow taps her stick as she shuffles
through time around her dusty house.  Her pale
eyes stare without sight, reflecting silver
like a winter lake.  She can no longer
buy thrift-shop sweaters for a pittance,
unravel, wash, color them with homemade
dyes, then knit with still strong hands and ancient
flair into pullovers or cardigans
dressed up with exquisite painted buttons.

For company, she listens to TV
or talking books.  On cloudless mornings of
golden sun when she can make out shadowy
shapes, she carefully makes tea, pale as the bark
of sycamore trees, in a bone china
cup smooth as mother-of-pearl.  She gently
taps its leaf-thin rim with her grandmother’s worn
silver-plated spoon, for the bell-like sound it makes,
the way her mother showed her long ago.
She knows how the cup glows with radiant
light with the early morning sun flowing through.

Her house is scented with potpourri from
the summer she dried and hung in a recess
in the wall of her creamy white front hall
a garland of sweet-smelling  lavender,
lemon verbena, and rose geranium.
She placed it by an ivory Kwan Yin
which had gleamed at her from a dark cobwebby
corner at a garage sale, appearing
to her like a cat to its chosen owner.
At night she lights the niche with amber light,
the way her husband liked.  It feels to her
then as if he’s just left the room, soothes
the inner sobbing she feels through the
long lonely days, the long lonely nights.
'''



decemberpoem = '''

DECEMBER

I heard the bell
announce Noel -
a midnight bell -
Emanuel.

Like buoy bells,
marking channels,
stand sentinel
in salty swells,

my fears dispel
with their tinkles.

'''


oldpathpoem = '''


Like shade from white lace parasols,
below the overhanging trees
sunlight and shadow dance a reel.
Wind sways the leaf-green canopy.

The path we jogged on long ago
is still the one we stroll along,
while those new neighbors we don’t know
lope right on past us, being young.

When I’m at home and I recall
the fragrant bay and twisting oak,
I feel the aura mystical
that’s present in the woods we walk.
'''




holmesappearspoem = '''


Spring 1997

A Seance?

A dozen of us, readers,
are gathered in a circle
of upholstered chairs
on an autumn night
while outside the wind rustles
eucalyptus leaves.
Lamps cast circles of light
in the redwood-paneled room.
We’re aficionados
of Sherlock Holmes,
his habits, his intelligence.
We discuss Dr. Bell,
role model for Holmes’s methods
and attention to detail.

I’m suddenly aware that
In the center of the circle,
by a redwood-burl coffee table,
there’s a powerful other presence:
Holmes is among us,
no doubt standing tall,
in tweeds and deerstalker,
brought to life by us all.
He exudes the aura
of nights on the moor,
Elizabeth Southwood  “A Waban Girl”


and a howling hound,
of midnight knocks at 221B,
of cement-gray drifting fog
obscuring cobblestoned Baker Street,
of challenges from Moriarty,
and the impish Irene,
footprints in mud,
messages scrawled in blood.
And edifying chats with dear Dr. Watson.
'''


parkinsonspoem = '''

Oct. 29, 1998

Parkinsons murders some of its victims
though supposedly we die of other stuff.
When I swallow, Parkinsons chokes me.
It throws me off balance when I walk.
At different times in the last couple of years,
It has knocked me down cement stairs,
dashed my head on bricks,
slammed me on a street,
strained the tendons in a shoulder,
cracked a rib,
and fractured a hip.

While I was waiting to see the surgeon recently,
a bent woman with a walker smiled at me as she pushed by
and so did a down-jacketed, slow-walking man with a cane,
like members of a fraternity.  Another member
and I shared war stories, both of us caged in walkers.
We compared our frequent falls -- unpredictable as the way
eucalyptus branches come crashing down
on a warm and windless summer day.

While I sat for five weeks, mending,
with my new stainless steel hip,
the sweet man for whom I’ve cooked
since we married cooked for me.
Elizabeth Southwood  “A Waban Girl”


When I came home from the hospital
my cat avoided me in my walker for a week,
then finally settled by me, purring, and rubbed
it with his jaw and cheeks.
My family and friends warn me
to be careful, go slow, chew carefully.
I did and do.  I’m not sure ‘careful’
 is enough.
'''




homegardnerpoem = '''


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




