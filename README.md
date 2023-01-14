# Calculating-Polynomial-Coefficients-from-P-1-and-P-P-1
This script provides a way to calculate the coefficients of a polynomial from the values of P(1) and P(P(1)). The polynomial must be a single variable polynomial with natural number coefficients and a natural number degree, and it should not be a monomial and P(1) should not be equal to P(P(1)). The script uses integer division to calculate the coefficients of the polynomial.
# Usage
```python
p1 = 2
pp1 = 5
coefficients = get_coefficients(p1, pp1)
print(coefficients)
```
This script takes two inputs, p1 and pp1 which are the values of P(1) and P(P(1)) respectively, and returns the coefficients of the polynomial in the form of a list.
In this particular example, the result is gonna be:
```python
[1, 0, 1]
```
# Note
Please make sure that the polynomial function you are working with meets the criteria of the script before using it to calculate the coefficients.

# Dependencies
This script depends on the math library, it uses the math.floor function to calculate the degree of the polynomial.
