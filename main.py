import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Basic graph
x = [0,1,2,3,4,5]
y = [0,2,4,6,8,10]
# Resize Graph
plt.figure(figsize=(5, 3.7),dpi=100)
# plt.plot(x,y, label='2x', c='#ababab', linewidth=2, marker='.',linestyle='--', markersize=10, markeredgecolor='red')

#  Use short notation
#  fmt = '[color][marker][line]'
plt.plot(x,y, 'bo--', label='2x')

#  Line number two
x2 = np.arange(0,4,0.5)
plt.plot(x2[:6], x2[:6]**2, 'r.-', label='x^2')
plt.plot(x2[5:],x2[5:]**2,'y--')
plt.title('First Graph!', fontdict={'fontname': 'Comic Sans MS', 'fontsize':24})
plt.xlabel('X Axis!',fontdict={'fontname': 'Comic Sans MS'})
plt.ylabel('Y Axis!')

plt.xticks([0,1,2,3,4,5])
plt.yticks([0,2,4,6,8.5,10])

plt.legend()
plt.savefig('mygraph.png', dpi=300)
plt.show()

labels = ['A', 'B', 'C']
values = [32, 45, 100]

bars = plt.bar(labels, values)

patterns = ['/', 'o', '*']
for bar in bars:
    bar.set_hatch(patterns.pop(0))
# bars[0].set_hatch('/')
# bars[1].set_hatch('o')
# bars[2].set_hatch('*')
plt.figure(figsize=(6, 5))
plt.show()