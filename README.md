# sp24-lab4
Materials for Week 4 Lab, which includes "Running Tests adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson.

_February 6, 2024_

Organization:
* SDX-ch6: The code files for the _SDX Ch.6_ activity (as downloaded directly from the book website, unmodified) 

## Team Members for Part 1
Sam, Clara

## Team Roles for Part 1
Who will start out as
* DRIVER: Sam
* NAVIGATOR: Clara

You will switch halfway through the _SDX Ch. 3_ activity.

## Part 1 Documentation

Write your answers to the questions below.

* What were the main ideas from SDX chapter 6?
Unit testing libraries. I liked how the code used the global function to pull test function names from the environemnt

* What questions did you have about the material in the chapters? What did you find confusing?
No question from either of us

### Part A: Recreate the tests from SDX Ch. 6 in the unittest framework

Write a short description of what you did for Part A below. Some questions you might answer: 
* What was your experience putting the tests in unittest like?
It was pretty straightforward. We did a lot of copying and pasting from the freeCodeCamp example into our environment and did a couple tweaks

* How is this different from Greg Wilson's simple implementation?
It seems much cleaner and more legible

* How is it similar?
They both abstract the test functions and then call them iteratively in main 

* Why might you use pytest over unittest, or vice versa?
We did not use pytest for these examples, only unittest

### Part B: Exercises from the end of SDX Ch. 6

Write a short summary of what you did below, with answers to the questions embedded in the exercises.
We did exercise 1 through 4 included, except for 2.2. The exercise descriptions were confusing to begin with but we got through. We almost did a form of TDD making skeleton setup and teardown functions and then creating the interface to them in the runner function but then leaving the implementation alone 