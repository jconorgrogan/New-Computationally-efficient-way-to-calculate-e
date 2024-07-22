import decimal
from decimal import Decimal, getcontext
from mpmath import mp

# Set precision
getcontext().prec = 100
mp.dps = 100

# Rational approximation of 7e/8
rational_7e_over_8 = Decimal(7) * Decimal(2721) / (Decimal(8) * Decimal(1001))

def count_matching_digits(approx, true_value):
    approx_str = str(approx)
    true_value_str = str(true_value)
    count = 0
    for a, b in zip(approx_str, true_value_str):
        if a == b:
            count += 1
        else:
            break
    return count

def refine_e_without_e(n):
    n_decimal = Decimal(n)
    
    # Calculate the approximations
    approx_e = ((n_decimal + Decimal(1)) / n_decimal) ** n_decimal
    approx_1_over_e = ((n_decimal - Decimal(1)) / n_decimal) ** n_decimal
    reciprocal_of_1_over_e = Decimal(1) / approx_1_over_e

    # Calculate the difference
    difference = approx_e - reciprocal_of_1_over_e

    # Calculate the absolute value of the difference
    absolute_difference = abs(difference)

    # Convert to string without scientific notation and extract digits
    absolute_difference_str = f"{absolute_difference:.100f}".rstrip('0').rstrip('.')

    # Ensure the string representation starts correctly
    if absolute_difference_str.startswith('0.'):
        absolute_difference_str = absolute_difference_str[2:]

    # Remove all zeros and place a period after the first non-zero digit
    non_zero_index = next(i for i, c in enumerate(absolute_difference_str) if c != '0')
    final_result_str = absolute_difference_str[non_zero_index] + '.' + absolute_difference_str[non_zero_index + 1:]

    # Import the most accurate value of e from mpmath and convert to Decimal
    mp_e = Decimal(str(mp.e))

    # Convert final_result_str to Decimal
    final_result_decimal = Decimal(final_result_str)

    # Calculate the adjustment term using the rational approximation of 7e/8
    x = Decimal(str(mp.log10(n)))
    error_term = rational_7e_over_8 * Decimal(10) ** (-2 * x)

    # Subtract the error term from the final result
    final_adjusted_result_decimal = final_result_decimal - error_term

    # Calculate the number of matching digits
    correct_digits_before = count_matching_digits(final_result_decimal, mp_e)
    correct_digits_after = count_matching_digits(final_adjusted_result_decimal, mp_e)

    # Output the results
    return {
        "n": n,
        "correct_digits_before": correct_digits_before,
        "correct_digits_after": correct_digits_after,
        "approx_e": approx_e,
        "reciprocal_of_1_over_e": reciprocal_of_1_over_e,
        "difference": difference,
        "error_term": error_term,
        "final_result_decimal_before": final_result_decimal,
        "final_result_decimal_after": final_adjusted_result_decimal
    }

# Test the function with various values of n
n_values = [10**5, 10**6, 10**7, 10**8, 10**9, 10**10, 10**11]
results = [refine_e_without_e(n) for n in n_values]

results
