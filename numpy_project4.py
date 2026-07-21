import numpy as np
score=np.array([75, 82, 120, 68, 95, 88, 76, 84, 91, 79])
print("Scores:", score)
print("Highest score:", np.max(score))
print("Lowest score:", np.min(score))
print("Average score:", np.mean(score))
print("Half century score:", score[score > 50])
print("Century score:", score[score > 100])