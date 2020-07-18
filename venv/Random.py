

import random
# # rand1 = ('I am', "I'm")
# # # ran2 = ('working on', 'starting','asking')
# # # ran3 = ('online', '')
# # # num = random.randrange(0,2)
# # # print(rand1[num],ran2[num],'this',ran3[num],'interview')
# # # # num = random.randrange(0,5)
# # # # print (nouns[num] + ' ' + verbs[num] + ' ' + adv[num] + ' ' + adj[num])
# # nouns = ("puppy", "car", "rabbit", "girl", "monkey")
# # verbs = ("runs", "hits", "jumps", "drives", "barfs")
# # adv = ("crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.")
# # adj = ("adorable", "clueless", "dirty", "odd", "stupid")
# # num = random.randrange(0,5)
# # print (nouns[num] + ' ' + verbs[num] + ' ' + adv[num] + ' ' + adj[num])
import random
random1 = ("I am", "I'm")
random2 = ("working on","starting")
random3 = ("online","")
random4 = ("very","extremely")
random5 = ("qualified","great","awesome")
random6 = ("!","|",".")
randomGenerator = random.randrange(0,2)

if randomGenerator is 0:
    randomPick = random4[randomGenerator]
else:
    randomPick = ""



print(random1[randomGenerator] + " " + random2[randomGenerator] + " this" + random3[randomGenerator] + " interview." + " I hope Cortx thinks I am "+ randomPick + random5[randomGenerator] + random6[randomGenerator])
"""
input = string
for i in len[input]
 if input[i] is {:
    search for ,
    increment counter
        if input[i] is }:
        print(random(o,counte)_
 """
