import time
from decimal import Decimal, getcontext
import pandas as pd

# Set the precision for decimal calculations
getcontext().prec = 200

# Define methods for approximating e

def calculate_e_approximations(n):
    n_decimal = Decimal(n)
    approx_e = ((n_decimal + Decimal(1)) / n_decimal) ** n_decimal
    approx_1_over_e = ((n_decimal - Decimal(1)) / n_decimal) ** n_decimal
    reciprocal_of_1_over_e = Decimal(1) / approx_1_over_e
    return approx_e, reciprocal_of_1_over_e

def compare_to_true_e(difference, true_e):
    # Convert to string to find the position of the first non-zero digit
    str_diff = str(difference).lstrip('0.')
    non_zero_position = len(str(difference)) - len(str_diff) + 1  # Position in the string including leading zeros

    # Compare starting from the non-zero position
    str_true_e = str(true_e)[non_zero_position:]
    str_test_e = str(difference)[non_zero_position:]

    # Count the number of matching digits
    matching_digits = 0
    for true_digit, test_digit in zip(str_true_e, str_test_e):
        if true_digit == test_digit:
            matching_digits += 1
        else:
            break

    return non_zero_position, matching_digits

# Function to measure time and accuracy
def time_and_accuracy_complementary_expressions(n, true_e):
    start_time = time.time()
    approx_e, reciprocal_of_1_over_e = calculate_e_approximations(n)
    difference = abs(approx_e - reciprocal_of_1_over_e)
    end_time = time.time()
    time_taken = Decimal(end_time - start_time)
    non_zero_position, matching_digits = compare_to_true_e(difference, true_e)
    return approx_e, reciprocal_of_1_over_e, difference, non_zero_position, matching_digits, time_taken

# True value of e for comparison
true_e = Decimal('2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391932003059921817413596629043572900334295260595630738132328627943490763233829880753195251019011573834187930702154089149934884167509244761460668082264800168477411853742345442437107539077744992069551702761838606261331384583000752044933826560297606737113200709328709127443')

# Parameters for each method
complementary_params = [10**6, 10**12, 10**18, 10**24, 10**50]

# Collect results
results = []

# Complementary expressions method
for n in complementary_params:
    approx_e, reciprocal_of_1_over_e, difference, non_zero_position, matching_digits, time_taken = time_and_accuracy_complementary_expressions(n, true_e)
    results.append(('Complementary', n, approx_e, reciprocal_of_1_over_e, difference, non_zero_position, matching_digits, time_taken, difference / time_taken))

# Display results
columns = ['Method', 'Parameter', 'Approximation (e)', 'Reciprocal Approximation (e)', 'Difference', 'First Non-Zero Position', 'Matching Digits', 'Time Taken (s)', 'Difference/Time']
df_results = pd.DataFrame(results, columns=columns)

import ace_tools as tools; tools.display_dataframe_to_user(name="Refined e Approximation Methods Comparison with Detailed Differences", dataframe=df_results)

df_results
