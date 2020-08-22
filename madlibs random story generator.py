# Mad Libs Random Story Generator
from random import randint
import copy

# create a dictionary to lookup words by type
word_dict = {
    'plural_noun':['ghosts','spirits','candies','brooms','boggies','haunts','witches','phantoms'],
    'noun':['bogeyman','cemetery','coffin','cobweb','cadaver','afterlife'],
    'adjective':['scary','spooky','startled','strange','icky','horrible','bloody','black'],
}

story = (
    "Halloween is my favorite holiday, because we get to dress up in {} "+
    "and visit {} in our {} saying '{}' or '{}'! "+
    "In exchange for a bag of {}. It's so {}! "+
    "This year, I'm going to dress up as a(n) {} {} my costume is going to be so {}!"
    )

def get_word(type, local_dict):
#get a random word from the word_dict based on word type '''
    words = local_dict[type]
    cnt = len(words)-1
    index = randint(0, cnt)
    return local_dict[type].pop(index)

def create_story():
#create a random story from word dict '''
    local_dict = copy.deepcopy(word_dict)
    return story.format(
        get_word('plural_noun', local_dict),
        get_word('plural_noun', local_dict),
        get_word('noun', local_dict),
        get_word('noun', local_dict),
        get_word('noun', local_dict),
        get_word('plural_noun', local_dict),
        get_word('adjective', local_dict),
        get_word('adjective', local_dict),
        get_word('noun', local_dict),
        get_word('adjective', local_dict)
)

print("STORY 1: ")
print(create_story())
print()
