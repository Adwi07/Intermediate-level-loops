# Print the following pattern

# *

# **

# ***

# ****

# *****

# Setup the total number of rows

N = 5

print("--- Increasing Pattern ---")
for i in range(1, N + 1):
    # Print 'i' stars in row i
    for j in range(i):
        print("*", end="")
    print()  # Move to the next line


# Print

# *****

# ****

# ***

# **

# *



print("\n--- Decreasing Pattern ---")
for i in range(N, 0, -1):
    # Loop backwards from N down to 1
    for j in range(i):
        print("*", end="")
    print()  # Move to the next line








# For the Increasing Pattern: In row i (starting at 1), we need to print exactly i stars.

# Row i=1: Print 1 star

# Row i=5: Print 5 stars

# For the Decreasing Pattern: In row i (starting at 1), we need to print N−i+1 stars.

# Row i=1: Print 5−1+1=5 stars

# Row i=5: Print 5−5+1=1 star


