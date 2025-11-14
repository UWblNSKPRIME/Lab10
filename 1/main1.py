import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-2, 5, 400)
y = x * np.sin(5 * x)

plt.plot(x, y,
         linestyle='-',                
         color='blue',                 
         linewidth=2,                  
         label='Y(x) = x * sin(5*x)')  

plt.title('Графік функції Y(x) = x * sin(5*x)') 
plt.xlabel('Вісь X')                             
plt.ylabel('Вісь Y')                             

plt.legend() 

plt.grid(True)

plt.show()