import matplotlib.pyplot as plt #we named it plt instead of writing the whole name
x1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
y1 = [0, 1, 8, 27, 64, 125, 216, 343, 512]
x2 = [0, 2, 4, 6, 8, 10]
y2 = [0, 3, 12, 18, 24, 30]
plt.plot(x1, y1, linestyle= 'dotted')
plt.plot(x2, y2, linestyle= 'dashdot')
plt.xlabel('X')
plt.ylabel('Y')
plt.title("cubic and linear function", fontsize= 20, color='purple')
plt.show()