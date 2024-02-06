# sp24-lab4
Materials for Week 4 Lab, which includes "Running Tests adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson.

_February 6, 2024_

Organization:
* SDX-ch6: The code files for the _SDX Ch.6_ activity (as downloaded directly from the book website, unmodified) 

## Team Members for Part 1
Enter your names here

## Team Roles for Part 1
Who will start out as
* DRIVER: Coden
* NAVIGATOR: Molly

You will switch halfway through the _SDX Ch. 3_ activity.

## Part 1 Documentation

Write your answers to the questions below.

* What were the main ideas from SDX chapter 6?
  Testing, how it works and different types of tests. There's different ways to do them and some are better for others depending on the scenario.
* What questions did you have about the material in the chapters? What did you find confusing?
  For assertRaises in unittest, are we expected to know and use all of the different types of errors in order to use it?

### Part A: Recreate the tests from SDX Ch. 6 in the unittest framework

Write a short description of what you did for Part A below. Some questions you might answer: 
* What was your experience putting the tests in unittest like? 
  Trial and error, referencing official documentation that was provided. Some errors/issues weren't clear but we figured it out.
* How is this different from Greg Wilson's simple implementation? 
  unittest must import what we want to test, can't be in the same file (like pytest).
* How is it similar? 
  it asserts. Each one runs the function we're testing and gives a value that it should be compared to.
* Why might you use pytest over unittest, or vice versa?
  unittest seems more helpful for bigger projects cuz you can probably run tests on multiple functions in one testing doc. pytest
  is probably more reasonable if you want to test just one function or have a smaller project.

### Part B: Exercises from the end of SDX Ch. 6

Write a short summary of what you did below, with answers to the questions embedded in the exercises.
