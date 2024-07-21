import decimal
from decimal import Decimal, getcontext
from mpmath import mp

# Set the precision high enough to handle large values of n
getcontext().prec = 100  # Increase if you need more precision
mp.dps = 100  # Set mpmath precision to 100 decimal places

# Define n
n = 100000000000
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

# Subtract e from the absolute difference string result
result_after_subtraction = final_result_decimal - mp_e

# Multiply the result by 8/7
multiplier = Decimal(8) / Decimal(7)
result_after_multiplication = result_after_subtraction * multiplier

# Print the results
print("approx_e:", approx_e)
print("reciprocal_of_1_over_e:", reciprocal_of_1_over_e)
print("difference:", difference)
print("absolute difference without leading zeros, first digit in the ones column:", final_result_str)
print("result after subtracting e to 100 decimals:", f"{result_after_subtraction:.100f}")
print("result after multiplying by 8/7 to 100 decimals:", f"{result_after_multiplication:.100f}")
