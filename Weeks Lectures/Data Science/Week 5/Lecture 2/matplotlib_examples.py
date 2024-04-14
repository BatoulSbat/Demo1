import matplotlib.pyplot as  plt
import seaborn as sns
import numpy as np

# #histograms, subplots
# N = 100 #an array of length 100
# x1 = np.random.rand(N) #creating 100 random numbers - this is the data for histogram
# x2 = np.random.rand(N)
# #print(x)

# #subplot, rows, columns, index of the plot
# plt.subplot(1,2,1)
# plt.hist(x1, color = 'b', alpha = 0.5)

# plt.subplot(1,2,2)
# plt.hist(x2, color = 'r')

# plt.show()

#seaborn
print(sns.get_dataset_names())

df = sns.load_dataset('penguins')
df.info()

#kernal density plot
sns.kdeplot(data = df, x = 'body_mass_g', hue = 'species', fill = True)
plt.show()

