import time
from decimal import Decimal, getcontext, InvalidOperation
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

# Function to transform the difference by moving the first significant digit
def transform_difference(difference):
    diff_str = str(difference).lstrip('0.')
    if not diff_str:  # handle case where diff_str is empty
        return Decimal(0)
    transformed_str = diff_str[0] + '.' + diff_str[1:]
    try:
        transformed_diff = Decimal(transformed_str)
    except InvalidOperation:
        transformed_diff = Decimal(0)
    return transformed_diff

# Function to measure time and accuracy
def time_and_accuracy_complementary_expressions(n, true_e):
    start_time = time.time()
    approx_e, reciprocal_of_1_over_e = calculate_e_approximations(n)
    difference = abs(approx_e - reciprocal_of_1_over_e)
    transformed_diff = transform_difference(difference)
    end_time = time.time()
    accuracy = abs(transformed_diff - true_e)
    time_taken = Decimal(end_time - start_time)
    return approx_e, reciprocal_of_1_over_e, difference, transformed_diff, accuracy, time_taken

# True value of e for comparison
true_e = Decimal('2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391932003059921817413596629043572900334295260595630738132328627943490763233829880753195251019011573834187930702154089149934884167509244761460668082264800168477411853742345442437107539077744992069551702761838606261331384583000752044933826560297606737113200709328709127443')

# Parameters for each method
complementary_params = [10**6, 10**12, 10**18, 10**24, 10**50]

# Collect results
results = []

# Complementary expressions method with differences of continued
for n in complementary_params:
    approx_e, reciprocal_of_1_over_e, difference, transformed_diff, accuracy, time_taken = time_and_accuracy_complementary_expressions(n, true_e)
    results.append(('Differences of Continued', n, transformed_diff, accuracy, time_taken, accuracy / time_taken))

# Display results
columns = ['Method', 'Parameter', 'Transformed Difference', 'Accuracy', 'Time Taken (s)', 'Accuracy/Time']
df_results = pd.DataFrame(results, columns=columns)

import ace_tools as tools; tools.display_dataframe_to_user(name="Differences of Continued Method Comparison", dataframe=df_results)

df_results
