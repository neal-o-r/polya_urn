import random as rd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

class Urn(object):

        def __init__(self, samples):
                self.samples = samples
                self.urn = samples
       
        def grow_sample(self, n):
               
                while len(self.urn) < n:
                        item = rd.sample(self.urn, 1)
                        self.urn += item


dist = [rd.sample([0,0,0,1], 1)[0] for i in range(2000)]

plt.axhline(sum(dist)/len(dist))

for _ in range(50):

        u = Urn(rd.sample(dist, 100))

        urn_contents = []
        for n in [i * 100 for i in range(2,20)]:
                u.grow_sample(n)
                urn_contents.append(sum(u.urn)/len(u.urn))

        plt.plot(urn_contents, color='0.7', alpha=0.3)
        plt.ylim(0,1)

plt.show()
