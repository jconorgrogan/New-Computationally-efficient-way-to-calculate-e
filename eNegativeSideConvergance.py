import time
from mpmath import mp, mpf, e
import sys

# Function to compute and compare results
def compute_and_compare(num_nines):
    # Increase the string conversion limit
    sys.set_int_max_str_digits(num_nines + 1000)  # Add buffer for safety
    
    # Adjust precision based on the number of 9s
    precision = num_nines + 50  # Extra buffer for intermediate calculations
    mp.dps = precision  # Set mpmath precision

    # Define x with the specified number of 9s
    x = mpf('-0.' + '9' * num_nines)

    # Start timing the computation
    start_time = time.time()

    # Stepwise computation for stability
    term1 = 1 + x
    term2 = mp.power(term1, 1 / x)
    term3 = 1 / term2
    term4 = 1 + term3
    result = mp.power(term4, term2)

    # Record computation time
    elapsed_time = time.time() - start_time

    # Convert result to string and truncate for display
    result_str = str(result)

    # Output the result and timing
    return {
        "result": result_str[:100],  # Show the first 100 digits of the result
        "time_taken": elapsed_time
    }

# Example usage: Compute for 100,000 nines
num_nines = 10000
result = compute_and_compare(num_nines)

# Print the output
print(f"First 100 digits of result: {result['result']}")
print(f"Time taken: {result['time_taken']:.6f} seconds")
