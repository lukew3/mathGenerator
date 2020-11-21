# mathgenerator

A math problem generator, created for the purpose of giving self-studying students and teaching organizations the means to easily get access to random math problems to suit their needs.

To try out generators, go to <https://todarith.ml/generate/>

If you have an idea for a generator, please add it as an issue and tag it with the "New Generator" label.

## Table of Contents
* [Installation](#installation)
* [Basic Usage](#basic-usage)
  * [More Complicated Usage](#more-complicated-usage)
* [Documentation](#documentation)
* [List of Generators](#list-of-generators)
  * [algebra](#algebra)
  * [basic_math](#basic_math)
  * [calculus](#calculus)
  * [computer_science](#computer_science)
  * [geometry](#geometry)
  * [misc](#misc)
  * [statistics](#statistics)

## Installation

The project can be install via pip

```bash
pip install mathgenerator
```

## Basic Usage
Here is an example of how you would generate an addition problem:

```python
from mathgenerator import mathgen

#generate an addition problem
problem, solution = mathgen.addition()

#another way to generate an addition problem using genById()
problem, solution = mathgen.genById(0)
```
### More Complicated Usage

```
import sys
from mathgenerator import mathgen

worksheet = mathgen.make_worksheet("2020-11-29")
mathgen.add_section_with_task_to_worksheet(worksheet, 105, 5)
mathgen.add_section_with_task_to_worksheet(worksheet, 2, 5)
mathgen.write_pdf(worksheet)
```

## Documentation
`getGenList()` returns a list of all generators in the repository in the format `[id, title, self, funcname]`

`genById(id)` generates a problem, solution set with generator id `id` in the form of a list in the format `[problem, solution]`

`make_pdf(id, count)` creates a printable pdf worksheet with `count` problems generated by the generator with id `id`.

## List of Generators
## algebra
| Id   | Skill | Example problem | Example Solution | Function Name |
|------|-------|-----------------|------------------|---------------|
| 11 | Basic Algebra | 7x + 6 = 6 | 0 | basic_algebra |
| 12 | Logarithm | log2(32) | 5 | log |
| 17 | Integer Multiplication with 2x2 Matrix | 7 * [[7, 1], [6, 0]] =  | [[49,7],[42,0]] | multiply_int_to_22_matrix |
| 20 | Midpoint of the two point | (-14,-19),(-2,15)= | (-8.0,-2.0) | midpoint_of_two_points |
| 21 | Factoring Quadratic | x^2+12x+20 | (x+2)(x+10) | factoring |
| 23 | Solve a System of Equations in R^2 | -7x + 3y = -2, -5x - 7y = 90 | x = -4, y = -10 | system_of_equations |
| 24 | Distance between 2 points | Find the distance between (-15, -7) and (8, -8) | sqrt(530) | distance_two_points |
| 26 | Linear Equations | 1x + 1y = -29, -15x + 11y = 149 | x = -18, y = -11 | linear_equations |
| 41 | Intersection of Two Lines | Find the point of intersection of the two lines: y = 3/2x - 6 and y = 4/4x + 5 | (22, 27) | intersection_of_two_lines |
| 43 | Cross Product of 2 Vectors | [-9, -3, -3] X [-18, 12, -10] =  | [66, -36, -162] | vector_cross |
| 45 | Simple Interest | Simple interest for a principle amount of 7669 dollars, 5% rate of interest and for a time period of 2 years is =  | 766.9 | simple_interest |
| 46 | Multiplication of two matrices | Multiply<table><tr><td>-4</td><td>4</td><td>0</td></tr><tr><td>1</td><td>-1</td><td>-1</td></tr><tr><td>-2</td><td>-1</td><td>1</td></tr></table>and<table><tr><td>-2</td><td>10</td></tr><tr><td>1</td><td>6</td></tr><tr><td>-3</td><td>-1</td></tr></table> | <table><tr><td>12</td><td>-16</td></tr><tr><td>0</td><td>5</td></tr><tr><td>0</td><td>-27</td></tr></table> | matrix_multiplication |
| 50 | Quadratic Equation | Zeros of the Quadratic Equation 70x^2+168x+95=0 | [-0.91, -1.49] | quadratic_equation |
| 65 | Multiplication of 2 complex numbers | (-18-9j) * (3+17j) =  | (99-333j) | multiply_complex_numbers |
| 72 | Dot Product of 2 Vectors | [7, 6, 5] . [17, 11, 10] =  | 235 | vector_dot |
| 74 | Inverse of a Matrix | Inverse of Matrix Matrix([[57, 55, 37], [82, 49, 79], [15, 71, 86]]) is: | Matrix([[465/71327, 701/71327, -844/71327], [5867/213981, -1449/71327, 1469/213981], [-5087/213981, 1074/71327, 1717/213981]]) | invert_matrix |
| 77 | Determinant to 2x2 Matrix | Det([[11, 9], [38, 16]]) =  |  -166 | int_matrix_22_determinant |
| 78 | Compound Interest | Compound interest for a principle amount of 6055 dollars, 6% rate of interest and for a time period of 8 year is =  | 9650.75 | compound_interest |
| 100 | complex Quadratic Equation | Find the roots of given Quadratic Equation 2x^2 + 9x + 8 = 0 | simplified solution : ((-1.219, -3.281)), generalized solution : ((-9 + sqrt(17))/2*2, (-9 - sqrt(17))/2*2) | complex_quadratic |
| 105 | Combine Like terms | 6x^1 + 4x^2 | 6x^1 + 4x^2  | combine_like_terms |
| 111 | Expanding Factored Binomial | (4x+2)(+7x-3) | 28*x^2+2*x-6 | expanding |
## basic_math
| Id   | Skill | Example problem | Example Solution | Function Name |
|------|-------|-----------------|------------------|---------------|
| 0 | Addition | 17+1= | 18 | addition |
| 1 | Subtraction | 59-56= | 3 | subtraction |
| 2 | Multiplication | 47*2= | 94 | multiplication |
| 3 | Division | 552/23= | 24 | division |
| 6 | Square Root | sqrt(25)= | 5 | square_root |
| 8 | Square | 6^2= | 36 | square |
| 13 | Complex Division | 48/29= | 1.66 | complex_division |
| 16 | Fraction Division | (1/10)/(2/4) | 1/5 | divide_fractions |
| 28 | Fraction Multiplication | (5/4)*(7/4) | 35/16 | fraction_multiplication |
| 31 | Factorial | 5! =  | 120 | factorial |
| 44 | Compare Fractions | Which symbol represents the comparison between 4/1 and 6/4? | > | compare_fractions |
| 47 | Cube Root | cuberoot of 727 upto 2 decimal places is: | 8.99 | cube_root |
| 53 | Exponentiation | 20^10 = | 10240000000000 | exponentiation |
| 71 | Absolute difference between two numbers | Absolute difference between numbers -51 and -93 =  | 42 | absolute_difference |
| 80 | Percentage of a number | What is 4% of 21? | Required percentage = 0.84% | percentage |
| 90 | isprime | 96 | False | is_prime |
| 97 | Power of Powers | The 34^2^2 = 34^(2*2) = 34^4 | 1336336 | power_of_powers |
## calculus
| Id   | Skill | Example problem | Example Solution | Function Name |
|------|-------|-----------------|------------------|---------------|
| 7 | Power Rule Differentiation | 1x^6 + 10x^6 + 2x^1 | 6x^5 + 60x^5 + 2x^0 | power_rule_differentiation |
| 48 | Power Rule Integration | 4x^9 + 9x^2 + 7x^9 | (4/9)x^10 + (9/2)x^3 + (7/9)x^10 + c | power_rule_integration |
| 88 | Differentiation | differentiate w.r.t x : d(sec(x)+6*x^(-2))/dx | tan(x)*sec(x) - 12/x^3 | differentiation |
| 89 | Definite Integral of Quadratic Equation | The definite integral within limits 0 to 1 of the equation 26x^2 + 14x + 50 is =  | 65.6667 | definite_integral |
| 110 | Stationary Points | f(x)=4*x^3 + 8*x^2 + 3 | (-4/3,209/27),(0,3) | stationary_points |
## computer_science
| Id   | Skill | Example problem | Example Solution | Function Name |
|------|-------|-----------------|------------------|---------------|
| 4 | Binary Complement 1s | 11101101= | 00010010 | binary_complement_1s |
| 5 | Modulo Division | 48%81= | 48 | modulo_division |
| 14 | Decimal to Binary | Binary of 42= | 101010 | decimal_to_binary |
| 15 | Binary to Decimal | 1111111001 | 1017 | binary_to_decimal |
| 56 | Fibonacci Series | The Fibonacci Series of the first 6 numbers is ? | [0, 1, 1, 2, 3, 5] | fibonacci_series |
| 62 | nth Fibonacci number | What is the 55th Fibonacci number? | 139583862445 | nth_fibonacci_number |
| 64 | Binary to Hexidecimal | 111110111 | 0x1f7 | binary_to_hex |
| 73 | Binary 2's Complement | 2's complement of 11001 = | 111 | binary_2s_complement |
| 79 | Decimal to Hexadecimal | Binary of 931= | 0x3a3 | decimal_to_hexadeci |
| 84 | Converts decimal to octal | The decimal number 3128 in Octal is:  | 0o6070 | decimal_to_octal |
| 91 | Binary Coded Decimal to Integer | Integer of Binary Coded Decimal 3 is =  | 13857 | bcd_to_decimal |
| 103 | Decimal to Binary Coded Decimal | BCD of Decimal Number 4809 is =  | 12129 | decimal_to_bcd |
## geometry
| Id   | Skill | Example problem | Example Solution | Function Name |
|------|-------|-----------------|------------------|---------------|
| 18 | Area of Triangle | Area of triangle with side lengths: 7 20 8 =  | (4.04507275167047e-15+66.06105130861906j) | area_of_triangle |
| 19 | Triangle exists check | Does triangle with sides 24, 27 and 33 exist? | Yes | valid_triangle |
| 22 | Third Angle of Triangle | Third angle of triangle with angles 60 and 33 =  | 87 | third_angle_of_triangle |
| 25 | Pythagorean Theorem | The hypotenuse of a right triangle given the other two lengths 1 and 7 =  | 7.07 | pythagorean_theorem |
| 29 | Angle of a Regular Polygon | Find the angle of a regular polygon with 7 sides | 128.57 | angle_regular_polygon |
| 32 | Surface Area of Cube | Surface area of cube with side = 9m is | 486 m^2 | surface_area_cube |
| 33 | Surface Area of Cuboid | Surface area of cuboid with sides = 8m, 3m, 13m is | 334 m^2 | surface_area_cuboid |
| 34 | Surface Area of Cylinder | Surface area of cylinder with height = 18m and radius = 6m is | 904 m^2 | surface_area_cylinder |
| 35 | Volum of Cube | Volume of cube with side = 11m is | 1331 m^3 | volume_cube |
| 36 | Volume of Cuboid | Volume of cuboid with sides = 12m, 3m, 5m is | 180 m^3 | volume_cuboid |
| 37 | Volume of cylinder | Volume of cylinder with height = 37m and radius = 3m is | 1046 m^3 | volume_cylinder |
| 38 | Surface Area of cone | Surface area of cone with height = 44m and radius = 10m is | 1731 m^2 | surface_area_cone |
| 39 | Volume of cone | Volume of cone with height = 16m and radius = 12m is | 2412 m^3 | volume_cone |
| 49 | Fourth Angle of Quadrilateral | Fourth angle of quadrilateral with angles 93 , 49, 8 = | 210 | fourth_angle_of_quadrilateral |
| 57 | Trigonometric Values | What is tan(45)? | 1 | basic_trigonometry |
| 58 | Sum of Angles of Polygon | Sum of angles of polygon with 3 sides =  | 180 | sum_of_polygon_angles |
| 60 | Surface Area of Sphere | Surface area of Sphere with radius = 2m is | 50.26548245743669 m^2 | surface_area_sphere |
| 61 | Volume of Sphere | Volume of sphere with radius 70 m =  | 1436755.0402417318 m^3 | volume_sphere |
| 70 | Angle between 2 vectors | angle between the vectors [416.61, 979.25, 782.01, 485.67, 343.15, 344.77, 437.04, 978.68, 284.87, 461.07, 157.63, 492.12, 721.78, 945.4, 317.4, 513.68, 59.33, 893.18] and [410.46, 30.13, 218.48, 678.66, 113.61, 827.02, 228.67, 365.48, 15.94, 677.05, 877.05, 654.78, 208.79, 259.1, 904.73, 789.02, 931.2, 621.62] is: | 0.89 radians | angle_btw_vectors |
| 75 | Area of a Sector | Given radius, 45 and angle, 29. Find the area of the sector. | Area of sector = 512.47230 | sector_area |
| 86 | Degrees to Radians | Angle 174 in radians is =  | 3.04 | degree_to_rad |
| 87 | Radians to Degrees | Angle 3 in degrees is =  | 171.89 | radian_to_deg |
| 95 | Curved surface area of a cylinder | What is the curved surface area of a cylinder of radius, 31 and height, 98? | CSA of cylinder = 19088.32 | curved_surface_area_cylinder |
| 96 | Perimeter of Polygons | The perimeter of a 7 sided polygon with lengths of [84, 23, 120, 68, 18, 107, 55]cm is:  | 475 | perimeter_of_polygons |
| 104 | Circumference | Circumference of circle with radius 6 | 37.69911184307752 | circumference |
| 108 | Arc length of Angle | Given radius, 21 and angle, 257. Find the arc length of the angle. | Arc length of the angle = 94.19542 | arc_length |
| 112 | Area of Circle | Area of circle with radius 61 | 11694.57142857143 | area_of_circle |
## misc
| Id   | Skill | Example problem | Example Solution | Function Name |
|------|-------|-----------------|------------------|---------------|
| 9 | LCM (Least Common Multiple) | LCM of 2 and 10 = | 10 | lcm |
| 10 | GCD (Greatest Common Denominator) | GCD of 10 and 11 =  | 1 | gcd |
| 27 | Prime Factorisation | Find prime factors of 101 | [101] | prime_factors |
| 40 | Common Factors | Common Factors of 61 and 80 =  | [1] | common_factors |
| 51 | HCF (Highest Common Factor) | HCF of 9 and 2 =  | 1 | hcf |
| 55 | Comparing surds | Fill in the blanks 74^(1/7) _ 95^(1/1) | < | surds_comparison |
| 63 | Profit or Loss Percent | Profit percent when CP = 163 and SP = 517 is:  | 217.17791411042944 | profit_loss_percent |
| 66 | Geometric Progression | For the given GP [10, 120, 1440, 17280, 207360, 2488320] ,Find the value of a,common ratio,8th term value, sum upto 9th term | The value of a is 10, common ratio is 12 , 8th term is 358318080 , sum upto 9th term is 4690709410.0 | geometric_progression |
| 67 | Geometric Mean of N Numbers | Geometric mean of 3 numbers 70 , 6 and 84 =  | (70*6*84)^(1/3) = 32.797659956001354 | geometric_mean |
| 68 | Harmonic Mean of N Numbers | Harmonic mean of 2 numbers 22 and 93 =  |  2/((1/22) + (1/93)) = 35.58260869565217 | harmonic_mean |
| 69 | Euclidian norm or L2 norm of a vector | Euclidian norm or L2 norm of the vector[819.5600005409527, 460.43358720959714, 312.8693242583006, 0.624754435091357, 233.6750010785489, 984.211085021748, 557.3047425779545, 236.05099006620688, 536.0418840782689, 612.4248321622609, 632.9588802226315] is: | 1853.157149219957 | euclidian_norm |
| 81 | Celsius To Fahrenheit | Convert 20 degrees Celsius to degrees Fahrenheit = | 68.0 | celsius_to_fahrenheit |
| 82 | AP Term Calculation | Find the term number 73 of the AP series: -14, -38, -62 ...  | -1742 | arithmetic_progression_term |
| 83 | AP Sum Calculation | Find the sum of first 71 terms of the AP series: -6, 81, 168 ...  | 215769.0 | arithmetic_progression_sum |
| 85 | Converts decimal to Roman Numerals | The number 396 in Roman Numerals is:  | CCCXCVI | decimal_to_roman_numerals |
| 92 | Complex To Polar Form | rexp(itheta) =  | 21.54exp(i-1.19) | complex_to_polar |
| 93 | Union,Intersection,Difference of Two Sets | Given the two sets a={1, 2, 4, 5, 6, 7, 8} ,b={4, 5, 6, 7, 9}.Find the Union,intersection,a-b,b-a and symmetric difference | Union is {1, 2, 4, 5, 6, 7, 8, 9},Intersection is {4, 5, 6, 7}, a-b is {8, 1, 2},b-a is {9}, Symmetric difference is {1, 2, 8, 9} | set_operation |
| 94 | Base Conversion | Convert 16646 from base 10 to base 13. | 7766 | base_conversion |
| 98 | Quotient of Powers with Same Base | The Quotient of 31^1 and 31^1 = 31^(1-1) = 31^0 | 1 | quotient_of_power_same_base |
| 99 | Quotient of Powers with Same Power | The Quotient of 5^1 and 37^1 = (5/37)^1 = 0.13513513513513514^1 | 0.13513513513513514 | quotient_of_power_same_power |
| 101 | Leap Year or Not | Year 1904  | is a leap year | is_leap_year |
| 102 | Minute to Hour conversion | Convert 919 minutes to Hours & Minutes | 15 hours and 19 minutes | minutes_to_hours |
| 106 | signum function | signum of -735 is = | -1 | signum_function |
| 109 | Binomial distribution | A manufacturer of metal pistons finds that, on average, 39.1% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 14 pistons will contain no more than 9 rejected pistons? | 98.53 | binomial_distribution |
## statistics
| Id   | Skill | Example problem | Example Solution | Function Name |
|------|-------|-----------------|------------------|---------------|
| 30 | Combinations of Objects | Number of combinations from 19 objects picked 6 at a time  | 27132 | combinations |
| 42 | Permutations | Number of Permutations from 10 objects picked 5 at a time =   | 30240 | permutation |
| 52 | Probability of a certain sum appearing on faces of dice | If 3 dice are rolled at the same time, the probability of getting a sum of 18 = | 1/216 | dice_sum_probability |
| 54 | Confidence interval For sample S | The confidence interval for sample [276, 220, 235, 205, 251, 237, 266, 240, 289, 247, 282, 228, 214, 218, 265, 269, 270, 293, 222, 202, 215, 236, 296, 244, 287, 213, 268, 233, 242, 277, 275, 267, 234, 212, 294, 250, 283, 281, 229] with 90% confidence is | (257.73707359556715, 243.03215717366362) | confidence_interval |
| 59 | Mean,Standard Deviation,Variance | Find the mean,standard deviation and variance for the data[22, 37, 46, 26, 34, 46, 15, 23, 38, 40, 42, 46, 44, 5, 50] | The Mean is 34.266666666666666 , Standard Deviation is 162.86222222222221, Variance is 12.761748399894985 | data_summary |
| 76 | Mean and Median | Given the series of numbers [28, 37, 79, 43, 87, 21, 23, 52, 22, 96]. find the arithmatic mean and mdian of the series | Arithmetic mean of the series is 48.8 and Arithmetic median of this series is 40.0 | mean_median |
| 107 | Conditional Probability | Someone tested positive for a nasty disease which only 1.91% of population have. Test sensitivity (true positive) is equal to SN= 93.22% whereas test specificity (true negative) SP= 94.46%. What is the probability that this guy really has that disease? | 24.68% | conditional_probability |
