'''
NOTE:
- [x] Create voter profiles
    - [x] Write code to pickle the profiles.
    - [x] Generate profiles and see if they can be opened.
- [x] Implement the iterative version of adding and deleting candidates 
    - [x] Implement the iterative version of adding.
    - [x] Implement the deleting feature.
- [x] Compare the results of the new Copeland score with the original Copeland score to see if it got the winners right. 
'''

import iterative_copeland as ic
import pickle
import numpy as np
from array import array

import matplotlib.pyplot as plt
import collections

# Reading pickled files and storing the data.
filename = "profile"
pickled_file = open("voter_profiles/"+filename+".vt", "rb")
preference_profile = pickle.load(pickled_file)
true_copeland_score = None

try:
    true_copeland_score = pickle.load(pickled_file)
except:
    None

pickled_file.close()

# Processing the data.
candidates = len(preference_profile)
agents = len(preference_profile[0])

def deletionCopeland(preference_profile, step, deletion_ratio):
    i_preference_profile = []
    for i in range(0, candidates, step):
        # Growing set of candidiates.
        i_preference_profile.extend(preference_profile[i : i+step])
        score_list = ic.pairwiseScoreCalcListFull(
            i_preference_profile, len(i_preference_profile), agents)
        copeland_score = ic.copelandScoreFull(score_list, len(i_preference_profile), agents)
        
        sorted_copeland_score = np.argsort(copeland_score)
        no_of_deleted_candidates = int(deletion_ratio*len(i_preference_profile))
        
        to_be_deleted = sorted_copeland_score[0:no_of_deleted_candidates]
        i_preference_profile = [i for j, i in enumerate(i_preference_profile) if j not in to_be_deleted]
    score_list = ic.pairwiseScoreCalcListFull(
            i_preference_profile, len(i_preference_profile), agents)
    copeland_score = ic.copelandScoreFull(score_list, len(i_preference_profile), agents)
    return (i_preference_profile, copeland_score)

ipp, cs = deletionCopeland(preference_profile, 5, 0.2)

not_deleted_candidate_ids = []
for i,x in enumerate(preference_profile.tolist()):
    if x in np.array(ipp).tolist():
        not_deleted_candidate_ids.append(i)
print(not_deleted_candidate_ids)

fig, (ax1, ax2) = plt.subplots(2)
fig.suptitle('Copeland Scores and Frequencies')

ax1.plot(not_deleted_candidate_ids, cs, 'ro')
ax1.plot(range(candidates), true_copeland_score, 'bo')
ax1.legend(['Copeland Score Post Deletion','Real Copeland Score'])
ax1.set_xlabel('Candidates')
ax1.set_ylabel('Copeland Score')

plt.hist(true_copeland_score, bins=np.arange(min(true_copeland_score), max(true_copeland_score)+1), color='b')
ax2.hist(cs, bins=np.arange(min(cs), max(cs)+1), color='r')
ax2.legend(['Real Copeland Score Frequency','Copeland Score Post Deletion Frequency'])
ax2.set_xlabel('Copeland Score')
ax2.set_ylabel('Frequency')
plt.savefig(filename+".png")
plt.show()