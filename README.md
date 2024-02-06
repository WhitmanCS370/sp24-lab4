# sp24-lab4
Materials for Week 4 Lab, which includes "Running Tests adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson.

_February 6, 2024_

Organization:
* SDX-ch6: The code files for the _SDX Ch.6_ activity (as downloaded directly from the book website, unmodified) 

## Team Members for Part 1
Neel Troeger, Rhys Sorenson-Graffs


## Team Roles for Part 1
Who will start out as
* DRIVER: Rhys
* NAVIGATOR: Neel

You will switch halfway through the _SDX Ch. 3_ activity.

## Part 1 Documentation

Write your answers to the questions below.

* What were the main ideas from SDX chapter 6?
How to write tests using assert and how to find functions for testing.

* What questions did you have about the material in the chapters? What did you find confusing?

### Part A: Recreate the tests from SDX Ch. 6 in the unittest framework

Write a short description of what you did for Part A below. Some questions you might answer: 
* What was your experience putting the tests in unittest like? 
* How is this different from Greg Wilson's simple implementation? 
* How is it similar? 
* Why might you use pytest over unittest, or vice versa?

### Part B: Exercises from the end of SDX Ch. 6

#### Exercise 1:

This code does not work:
```
for name in globals():
    print(name)
```

However, this code does. It returns the list of functions.
```
name = None
for name in globals():
    print(name)
```

They are different because in the first name gets added to globals() while trying to iterate through it, while in the second it gets added before.




Write a short summary of what you did below, with answers to the questions embedded in the exercises.