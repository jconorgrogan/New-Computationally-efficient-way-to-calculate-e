import time
from decimal import Decimal, getcontext
import pandas as pd

# Set the precision for decimal calculations
getcontext().prec = 200

# Define methods for approximating e

def calculate_e_taylor_series(n):
    e_taylor = Decimal(0)
    factorial = Decimal(1)
    for k in range(n + 1):
        if k > 0:
            factorial *= k
        e_taylor += Decimal(1) / factorial
    return e_taylor

def calculate_e_approximations(n):
    n_decimal = Decimal(n)
    approx_e = ((n_decimal + Decimal(1)) / n_decimal) ** n_decimal
    approx_1_over_e = ((n_decimal - Decimal(1)) / n_decimal) ** n_decimal
    reciprocal_of_1_over_e = Decimal(1) / approx_1_over_e
    return approx_e, reciprocal_of_1_over_e

def continued_fraction_e(k):
    a0 = 0
    p_minus_1, p0 = 1, a0
    q_minus_1, q0 = 0, 1

    a = [a0, 1] + [4 * (n - 1) + 2 for n in range(2, k + 1)]

    p_prev, p_curr = p_minus_1, p0
    q_prev, q_curr = q_minus_1, q0

    for i in range(1, k + 1):
        p_next = a[i] * p_curr + p_prev
        q_next = a[i] * q_curr + q_prev
        p_prev, p_curr = p_curr, p_next
        q_prev, q_curr = q_curr, q_next

    e_approx = Decimal(2 * p_curr) / Decimal(q_curr) + 1
    return e_approx

# Function to measure time and accuracy
def time_and_accuracy_taylor_series(n, true_e):
    start_time = time.time()
    e_approx = calculate_e_taylor_series(n)
    end_time = time.time()
    accuracy = abs(e_approx - true_e)
    time_taken = Decimal(end_time - start_time)
    return e_approx, accuracy, time_taken

def time_and_accuracy_complementary_expressions(n, true_e):
    start_time = time.time()
    approx_e, reciprocal_of_1_over_e = calculate_e_approximations(n)
    end_time = time.time()
    accuracy_1 = abs(approx_e - true_e)
    accuracy_2 = abs(reciprocal_of_1_over_e - true_e)
    time_taken = Decimal(end_time - start_time)
    return approx_e, reciprocal_of_1_over_e, accuracy_1, accuracy_2, time_taken

def time_and_accuracy_continued_fraction(k, true_e):
    start_time = time.time()
    e_approx = continued_fraction_e(k)
    end_time = time.time()
    accuracy = abs(e_approx - true_e)
    time_taken = Decimal(end_time - start_time)
    return e_approx, accuracy, time_taken

# True value of e for comparison
true_e = Decimal(2.718281828459045235360287471352662497757247093699959574966967627724076630353547594571382178525166427427466391932003059921817413596629043572900334295260595630738132328627943490763233829880753195251019011573834187930702154089149934884167509244761460668082264800168477411853742345442437107539077744992069551702761838606261331384583000752044933826560297606737113200709328709127443)

# Parameters for each method
taylor_params = [100, 1000, 10000]
complementary_params = [10**6, 10**12, 10**18, 10**24, 10**50]
continued_fraction_params = [1500, 12000]

# Collect results
results = []

# Taylor series method
for n in taylor_params:
    e_approx, accuracy, time_taken = time_and_accuracy_taylor_series(n, true_e)
    results.append(('Taylor', n, e_approx, accuracy, time_taken, accuracy / time_taken))

# Complementary expressions method
for n in complementary_params:
    approx_e, reciprocal_of_1_over_e, accuracy_1, accuracy_2, time_taken = time_and_accuracy_complementary_expressions(n, true_e)
    results.append(('Complementary', n, approx_e, accuracy_1, time_taken, accuracy_1 / time_taken))
    results.append(('Complementary', n, reciprocal_of_1_over_e, accuracy_2, time_taken, accuracy_2 / time_taken))

# Continued fraction method
for k in continued_fraction_params:
    e_approx, accuracy, time_taken = time_and_accuracy_continued_fraction(k, true_e)
    results.append(('Continued Fraction', k, e_approx, accuracy, time_taken, accuracy / time_taken))

# Display results
columns = ['Method', 'Parameter', 'Approximation', 'Accuracy', 'Time Taken (s)', 'Accuracy/Time']
df_results = pd.DataFrame(results, columns=columns)

import ace_tools as tools; tools.display_dataframe_to_user(name="e Approximation Methods Comparison", dataframe=df_results)

df_results
