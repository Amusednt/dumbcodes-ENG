import matplotlib.pyplot as plt

# Sample data for the visualizations
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
categories = ['A', 'B', 'C', 'D']
values = [15, 30, 45, 10]

def plot_line_chart():
    plt.plot(x, y, marker='o')
    plt.title('Line Chart')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid()
    plt.show()

def plot_bar_chart():
    plt.bar(categories, values, color='skyblue')
    plt.title('Bar Chart')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.show()

def plot_pie_chart():
    plt.pie(values, labels=categories, autopct='%1.1f%%')
    plt.title('Pie Chart')
    plt.show()

def plot_scatter_plot():
    plt.scatter(x, y, color='red')
    plt.title('Scatter Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid()
    plt.show()

# User input to choose the type of chart
print("Choose the type of chart to display:")
print("1. Line Chart")
print("2. Bar Chart")
print("3. Pie Chart")
print("4. Scatter Plot")

choice = input("Enter the number of your choice (1-4): ")

if choice == '1':
    plot_line_chart()
elif choice == '2':
    plot_bar_chart()
elif choice == '3':
    plot_pie_chart()
elif choice == '4':
    plot_scatter_plot()
else:
    print("Invalid choice. Please enter a number between 1 and 4.")