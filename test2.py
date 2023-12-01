import numpy as np

ratings = [1, 2, 3, 4, 5]
counts = [2, 1, 10, 10, 17]

# Calculate the average value (arithmetic mean) of satisfaction ratings
average_rating = np.dot(ratings, counts) / sum(counts)

# Calculate the standard deviation
variance = np.dot((ratings - average_rating)**2, counts) / sum(counts)
std_deviation = np.sqrt(variance)

print(f"Average value of satisfaction ratings: {average_rating:.2f}")
print(f"Standard deviation: {std_deviation:.2f}")
