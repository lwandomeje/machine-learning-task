import numpy as np

total_marks = np.arange(20)
print("\nOriginal array:")
print(total_marks)

#mean
r1 = np.mean(total_marks)
r2 = np.average(total_marks)
assert np.allclose(r1, r2)
print("\nMean: ", r1)

#standard devaition
r1 = np.std(total_marks)
r2 = np.sqrt(np.mean((total_marks - np.mean(total_marks)) ** 2))
assert np.allclose(r1, r2)
print("\nstd: ", r1)

#variance
r1 = np.var(total_marks)
r2 = np.mean((total_marks - np.mean(total_marks)) ** 2)
assert np.allclose(r1, r2)
print("\nvariance: ", r1)

import matplotlib.pyplot as pd
import numpy as np

blood_suger_men = [100,80,90,115,140,87,80,120,79]
blood_suger_women = [76,89,102,120,87,59,66,135,133]

suger_level = [blood_suger_men,blood_suger_women]
colors = ['r','g']
label = ['men','woman']
pd.xlabel("Blood suger range")
pd.ylabel("number of patients")

# 70-100 = normal
#100-130 = pre-diabetic
#above 130 diabetic
bins = [70,100,130,150]

pd.hist(suger_level,bins=bins,rwidth=0.99,color=colors ,label=label)
pd.title("Blood suger levels chart")
pd.legend()
pd.show()


















