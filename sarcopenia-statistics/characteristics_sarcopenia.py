##  to test whether there is any correlation with sarcopenia and cliniopathological features

from scipy.stats import mannwhitneyu , fisher_exact
import numpy as np

a1 = np.array([19,4,9])
a2 = np.array([35,8,15])

a = mannwhitneyu(a1,a2,use_continuity=False,alternative='two-sided')
print(a)

b1 = np.array([27,7,0,1,0])
b2 = np.array([57,15,0,2,0])

b = mannwhitneyu(b1,b2,use_continuity=False,alternative='two-sided')
print(b)

c1 = np.array([10,3,4,16])
c2 = np.array([17,7,18,31])

c = mannwhitneyu(c1,c2,use_continuity=True,alternative='two-sided')
print(c)

d1 = np.array([12,11,4,6,0])
d2 = np.array([30,29,5,7,1])

d = mannwhitneyu(d1,d2,use_continuity=True,alternative='two-sided')
print(d)

e = fisher_exact([[7,28],[28,46]], alternative='two-sided')
f = fisher_exact([[21,14],[37,37]], alternative='two-sided')
print(e)
print(f)
