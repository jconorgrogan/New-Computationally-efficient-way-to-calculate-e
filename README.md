

Found an interesting way to calculate e which seems incredibly accurate as well as extremely computationally efficient. The interesting thing is that at EXTREMELY large values of n, it differes from the actual value of e by the absolute value of  7e/8 to -10^2n.... not sure why this is.


## Complementary Expressions Method for Approximating \( e \)

The complementary expressions method leverages two complementary limits that converge to \( e \) and \( \frac{1}{e} \) respectively. 

### Method Overview

1. **Expression for \( e \)**:
   \[
   \left(\frac{n+1}{n}\right)^n
   \]
   This expression approaches \( e \) as \( n \) increases. It is based on the limit definition of \( e \) from calculus:
   \[
   e = \lim_{n \to \infty} \left(1 + \frac{1}{n}\right)^n
   \]
   By manipulating the expression slightly, it becomes:
   \[
   \left(\frac{n+1}{n}\right)^n = \left(1 + \frac{1}{n}\right)^n
   \]

2. **Expression for \( \frac{1}{e} \)**:
   \[
   \left(\frac{n-1}{n}\right)^n
   \]
   This expression converges to \( \frac{1}{e} \) as \( n \) increases. The reciprocal of this value provides another approximation of \( e \).

### Calculation Steps

1. **Calculate \( \left(\frac{n+1}{n}\right)^n \)**:
   Compute this expression for a given \( n \). This value directly approximates \( e \).

2. **Calculate \( \left(\frac{n-1}{n}\right)^n \)**:
   Compute this expression for the same \( n \) and then take its reciprocal to get another approximation of \( e \):
   \[
   \frac{1}{\left(\frac{n-1}{n}\right)^n}
   \]

3. **Compare the Two Approximations**:
   Both approximations should be very close to the true value of \( e \). But the difference between them is even closer, specifically when  truncating the leading zeros).


  # Step-by-Step Calculation for example \( n = 100,000 \)

1. **Calculate \( \left(\frac{100,001}{100,000}\right)^{100,000} \)**:
   \[
   2.718268237174489668035064824426046447974446932677822863009164419845151804338017316089139403836951483
   \]
   (accurate to 6th decimal place)

3. **Calculate \( \left(\frac{99,999}{100,000}\right)^{100,000} \)**:
   \[
   \left(\frac{99,999}{100,000}\right)^{100,000}
   \]
   
   The reciprocal is:
   \[
   \frac{1}{\left(\frac{99,999}{100,000}\right)^{100,000}} \approx 2.718295419992776636984018555252864677526093772741773601919706552377623091327243183538793488615641215
   \]
    (accurate to 6th decimal place)

5. **Difference between the two approximations**:
   \[
   \left(\frac{100,001}{100,000}\right)^{100,000} - \frac{1}{\left(\frac{99,999}{100,000}\right)^{100,000}} = -0.000027182818286968948953730826818229551646840063950738910542132532471286989225867449654084778689732
   \]

   When you truncate the 0s and add a decimal after the first non-zero term, you get 2.7182818286968948953730826818229551646840063950738910542132532471286989225867449654084778689732
Which is accurate to the 11th decimal place!

As \( n \) approaches infinity, the difference between the approximations \((1 + \frac{1}{n})^n\) and \(\frac{1}{(1 - \frac{1}{n})^n}\) converges to \( e \). The error term associated with this convergence can be approximated by:

\[
E(n) = \left| (1 + \frac{1}{n})^n - \frac{1}{(1 - \frac{1}{n})^n} - \left( e - \frac{1}{e} \right) \right|
\]

Empirically, it has been determined that the error term \( E(n) \) can be approximated by:

\[
E(n) \approx 2.38 \times 10^{-2x - 1}
\]

where \( x = \log_{10}(n) \).

Thus, as \( n \) increases by an order of magnitude, the error term decreases by approximately two orders of magnitude. This relationship can also be expressed as:

\[
E(n) \approx \frac{7e}{8} \cdot 10^{-2x}
\]

where \( e \) is the base of the natural logarithm and \( x = \log_{10}(n) \).
