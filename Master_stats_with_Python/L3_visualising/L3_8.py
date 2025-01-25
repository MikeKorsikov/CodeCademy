import matplotlib.pyplot as plt
from music_data import two_thousand, two_thousand_one, two_thousand_two

plt.boxplot([two_thousand, two_thousand_one, two_thousand_two], 
labels = ["2000 Songs", "2001 Songs", "2002 Songs"])
plt.xlabel("Release year")
plt.ylabel("Song duaration (s)")
plt.show()