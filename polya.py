import random as rd
import matplotlib.pyplot as plt

class Urn(object):

	def __init__(self, samples):
		self.samples = samples
		self.urn = samples
	
	def grow_sample(self, n):
		
		while len(self.urn) < n:
			item = rd.sample(self.urn, 1)
			self.urn += item


dist = [rd.sample([0,0,0,1], 1)[0] for i in range(2000)]

u = Urn(rd.sample(dist, 100))
u.grow_sample(2000)

plt.hist(dist, alpha=0.5, label='Original')
plt.hist(u.urn, alpha=0.5, label='Urn')
plt.legend()
plt.show()
