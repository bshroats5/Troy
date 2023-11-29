import matplotlib.pyplot as plt
# Initialize figure and axis
fig, ax = plt.subplots()

# Data for Eastern Kentucky
eastern_kentucky_fg = 29
eastern_kentucky_fga = 65
eastern_kentucky_3pt = 9
eastern_kentucky_3pta = 21

# Data for Troy
Troy_fg = 25
Troy_fga = 69
Troy_3pt = 13
Troy_3pta = 28

# Calculate percentages
eastern_kentucky_fg_percentage = eastern_kentucky_fg / eastern_kentucky_fga * 100
eastern_kentucky_3pt_percentage = eastern_kentucky_3pt / eastern_kentucky_3pta * 100
Troy_fg_percentage = Troy_fg / Troy_fga * 100
Troy_3pt_percentage = Troy_3pt / Troy_3pta * 100

# Set bar width and positions
bar_width = 0.35  # Width of each bar
index = [1, 2, 4, 5]  # X-axis positions for the bars

# Set bar colors
colors = ["#800000", "#000000", "#FF0000", "#000000"]  # Maroon, Black, Red, Black

# Create the bars
ax.bar(index[0], eastern_kentucky_fg_percentage, bar_width, label="EKU FG%", color=colors[0])
ax.bar(index[1], eastern_kentucky_3pt_percentage, bar_width, label="EKU 3PT%", color=colors[1])
ax.bar(index[2], Troy_fg_percentage, bar_width, label="Troy FG%", color=colors[2])
ax.bar(index[3], Troy_3pt_percentage, bar_width, label="Troy 3PT%", color=colors[3])

# Set x-axis ticks and labels
ax.set_xticks([index[0] + bar_width / 2, index[1] + bar_width / 2, index[2] + bar_width / 2, index[3] + bar_width / 2])
ax.set_xticklabels(["EKU FG%", "EKU 3PT%", "Troy FG%", "Troy 3PT%"])

# Show the graph
plt.show()
