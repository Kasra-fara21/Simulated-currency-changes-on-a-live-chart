import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as ani
import random as rd

plt.style.use('dark_background')

fig = plt.figure()
ax = plt.axes()

x = []
y = []
z = []
dlr = []
Euro_list = []




dollar = float(input("Enter the dollar price: "))
Euro = float(input("Enter the Euro price: "))





for i in range(1, 100):
    dlr_changing= rd.uniform(float(-5.9), float(5.9))
    Euro_changing = rd.uniform(float(-5.9), float(5.9))
    dollar = dollar + dlr_changing
    Euro = Euro + Euro_changing
    dlr.append(dollar)
    Euro_list.append(Euro)
    
line, = ax.plot(x, y,
                color = 'green',
                linewidth=3,
                label='dollar price')
Euro_line, = ax.plot(x, z,
                     color='red',
                     linewidth=3,
                     label='Euro price')


def update(frame):
    x.append(frame)
    y.append(dlr[frame - 1])
    z.append(Euro_list[frame - 1])
    line.set_data(x, y)
    Euro_line.set_data(x, z)
    print(f'dollar price: {dlr[frame - 1]}')
    print(f'Euro price: {Euro_list[frame - 1]}')
    # Euro_line.set_data(x, Euro)

to_do = ani(
    fig,
    update,
    interval = 1000,
    frames= range(1, 100),
    repeat= False
)

ax.set_xlim(1, 100)
ax.set_ylim(1, 250)

ax.legend()

ax.set_title('Real-time fluctuations of global currencies')
ax.set_xlabel('time')
ax.set_ylabel('price change')
plt.show()