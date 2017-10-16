import random as rd
import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.stats

plt.style.use('ggplot')

def mean_confidence_interval(data, confidence=0.95):
	a = 1.0*np.array(data)
	n = len(a)
	m, se = np.mean(a), scipy.stats.sem(a)
	h = se * sp.stats.t._ppf((1+confidence)/2., n-1)
	return m, h


class Urn(object):

        def __init__(self, samples):
                self.samples = samples
                self.urn = samples
       
        def grow_sample(self, n):
               
                while len(self.urn) < n:
                        item = rd.sample(self.urn, 1)
                        self.urn += item


dist = [rd.sample([0,0,0,1], 1)[0] for i in range(2000)]
s = rd.sample(dist, 100)
m, h = mean_confidence_interval(s)

plt.axhline(sum(dist)/len(dist))
plt.axhline(m+h, ls='--', c='r') 
plt.axhline(m-h, ls='--', c='r') 

for _ in range(50):

        u = Urn(rd.sample(dist, 100))

        urn_contents = []
        for n in [i * 100 for i in range(2,20)]:
                u.grow_sample(n)
                urn_contents.append(sum(u.urn)/len(u.urn))

        plt.plot(urn_contents, color='0.7', alpha=0.3)

plt.ylim(0,1)
plt.xlim(0,len(urn_contents)-1)
plt.show()
