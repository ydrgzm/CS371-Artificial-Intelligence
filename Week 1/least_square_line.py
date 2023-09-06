def calculate_squared_error(m, points):
    """
    Calculate the squared error between a linear model and data points.

    Args:
        m (float): The slope of the linear model.
        points (list of tuples): A list of data points, each represented as a tuple (x, y).

    Returns:
        float: The SE between the linear model and the data points.
    """
    result = 0
    for p in points:
        result += (m * p[0] - p[1]) ** 2
    return result

def calculate_gradient(m, points):
    """
    Calculate the gradient of the squared error (SE) with respect to the slope 'm'.

    Args:
        m (float): The current slope of the linear model.
        points (list of tuples): A list of data points, each represented as a tuple (x, y).

    Returns:
        float: The gradient of the SE with respect to 'm'.
    """
    result = sum([2 * x * (m * x - y) for x, y in points])
    return result

# Sample data points
points = [(2, 4), (4, 2)]

# Initialize the slope 'm' to 0
m = 0

# optimization loop
for t in range(100):
    # Calculate the current squared error (SE)
    val = calculate_squared_error(m, points)
    
    # Calculate the gradient of the SE with respect to 'm'
    df = calculate_gradient(m, points)
    
    # Update 'm' 
    learning_rate = 0.01
    m = m - learning_rate * df
    
    # Print iteration information
    print(f'Iteration = {t+1}\nm = {m}, SE = {val}, Gradient = {df}\n')

# Print the optimized slope 'm'
print(f'Optimized slope (m) = {m}')