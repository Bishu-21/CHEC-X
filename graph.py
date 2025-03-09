import matplotlib.pyplot as plt
import time

# Initialize data lists
xdata = []
ydata = []

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 100)
ax.set_ylim(0, 50)  # Adjusted for better visualization
line, = ax.plot([], [], 'r-', label="y = x/2")

# Add labels and legend
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Real-time Data Plot")
ax.legend()

# Function to update the graph dynamically
def update_graph():
    for i in range(100):
        xdata.append(i)
        ydata.append(i / 2)
        
        # Update line data
        line.set_data(xdata, ydata)
        
        # Adjust x-axis dynamically
        ax.set_xlim(0, max(10, i + 10))
        
        plt.draw()
        plt.pause(0.05)  # Smooth update
    plt.show()  # Keep the graph window open at the end

# Run the update function
update_graph()
