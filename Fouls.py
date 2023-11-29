import matplotlib.pyplot as plt

# Example data for teams
teams = ['Troy Trojans', 'Eastern Kentucky Colonels']
fouls = [13, 13]

# Create a bar graph
plt.bar(teams, fouls)

# Define colors for each team
Troy_color = 'Red'
eastern_kentucky_color = 'Maroon'

# Create a bar graph with custom colors
plt.bar(teams, fouls, color=[Troy_color, eastern_kentucky_color])


# Add title and labels
plt.title('Team Fouls')
plt.xlabel('Teams')
plt.ylabel('Fouls')

# Show the plot
plt.show()
