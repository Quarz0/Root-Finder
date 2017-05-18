# Intro:-
The aim of this app is to apply different root finding algorithms, compare and analyse their behaviour.
It supports the following root finding algorithms:-
- Bisection
- False-Position
- Newton-Raphson
- Secant
- Fixed-Point
- Birge-Vieta
The user can choose to solve an equation using one or multiple methods, and also provide each method with its required parameters.

# General Method:-
In addition to the previous methods, the app supports root finding using a general method where no parameters are required.
The general method works as follows:
- It starts by first generating a random number as an initial guess
- It proceeds by testing the fixed-point convergence criteria, and applies it if true
- If the latter was a false condition, a solution is generated using the modified-Newton-Raphson method
- If no solution found, repeat
And for the method not to get stuck in an infinite loop in the case of no solution after several unsuccessful trials, another stopping criteria was added which is a one-minute time limit for the algorithm to find the most accurate answer possible or else raise an error flag.

# Other features:-
- Saving and loading in JSON file formats
- Plotting equations, boundaries for all iterations, errors and roots.
- Displaying the input equation in LaTeX
- Specifying max number of iterations and epsilon as stopping criterias
- Displaying results of each iteration in a table (root, abs error, etc)
- Calculation of precision, execution time and error bound for some methods

# Packages used:-
- SymPy
- NumPy
- PyQt4
- MatPlotLib

# Screenshots:-

<img width="1430" alt="screen shot 2017-05-18 at 1 40 13 am" src="https://cloud.githubusercontent.com/assets/15021613/26223589/15cd7aae-3c1f-11e7-932c-10c32cecf871.png">
<img width="347" alt="screen shot 2017-05-18 at 1 40 26 am" src="https://cloud.githubusercontent.com/assets/15021613/26223590/15dec4e4-3c1f-11e7-9a81-077edb62cfe2.png">
<img width="1417" alt="screen shot 2017-05-18 at 1 42 04 am" src="https://cloud.githubusercontent.com/assets/15021613/26223591/15e708f2-3c1f-11e7-9d3d-a9ee2dcbab83.png">
<img width="316" alt="screen shot 2017-05-18 at 1 42 48 am" src="https://cloud.githubusercontent.com/assets/15021613/26223593/15f8445a-3c1f-11e7-9e29-51a01f70c152.png">
<img width="313" alt="screen shot 2017-05-18 at 1 48 39 am" src="https://cloud.githubusercontent.com/assets/15021613/26223594/16066abc-3c1f-11e7-8b03-51a3ba19df18.png">
<img width="607" alt="screen shot 2017-05-18 at 2 49 45 am" src="https://cloud.githubusercontent.com/assets/15021613/26223597/163e4aa4-3c1f-11e7-8267-804edc63af1f.png">
<img width="616" alt="screen shot 2017-05-18 at 2 59 01 am" src="https://cloud.githubusercontent.com/assets/15021613/26223598/1656749e-3c1f-11e7-9b67-f9365b259609.png">
<img width="613" alt="screen shot 2017-05-18 at 3 22 30 am" src="https://cloud.githubusercontent.com/assets/15021613/26223599/166131ea-3c1f-11e7-94d2-b0770d792014.png">
<img width="1427" alt="screen shot 2017-05-18 at 1 51 31 am" src="https://cloud.githubusercontent.com/assets/15021613/26223595/161d2ad6-3c1f-11e7-995d-fa99a663509f.png">
<img width="672" alt="screen shot 2017-05-18 at 1 54 04 am" src="https://cloud.githubusercontent.com/assets/15021613/26223596/162dc760-3c1f-11e7-9750-751abfae8ee2.png">

