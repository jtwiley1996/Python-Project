import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Create a sample DataFrame
data = {
    'x': np.arange(10),
    'y': np.random.randint(0, 100, 10)
}
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

# Plot the data
plt.plot(df['x'], df['y'])
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Sample Plot')
plt.show()
