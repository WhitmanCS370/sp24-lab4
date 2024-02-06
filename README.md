# sp24-lab4
Materials for Week 4 Lab, which includes "Running Tests adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson.

_February 6, 2024_

Organization:
* SDX-ch6: The code files for the _SDX Ch.6_ activity (as downloaded directly from the book website, unmodified) 

## Team Members for Part 1
Luke Samuels, Zurain Zeeshan

## Team Roles for Part 1
Who will start out as
* DRIVER: Driver's name
* NAVIGATOR: Navigator's name

You will switch halfway through the _SDX Ch. 3_ activity.

## Part 1 Documentation

Write your answers to the questions below.

* What were the main ideas from SDX chapter 6?
SDX chapter 6 talks about creating a homebrew testing framework that allows the user to blanket-call all the test functions in the file.
* What questions did you have about the material in the chapters? What did you find confusing?
It seems like this is a lot of extra writing just to just call a set of functions. Why not just have a function for each test (or one function that has multiple tests) then one more driver function that runs all of the tests? That's basically exactly what the drivers do.

### Part A: Recreate the tests from SDX Ch. 6 in the unittest framework

Write a short description of what you did for Part A below. Some questions you might answer: 
* What was your experience putting the tests in unittest like? 

Using unittest was pretty easy, especially since we had the tutorial. The hardest part was picking an assert statement to check.

* How is this different from Greg Wilson's simple implementation?
Wilson's implementation was interesting in that as long as you named your tests appropriately, you didn't have to add them to any kind of driver class or function. Neat. 

* How is it similar? 
Both frameworks emphasized having one function per test, and then some way of running all the tests in a row.

* Why might you use pytest over unittest, or vice versa?
I have no idea what pytest actually does. It just seemed to give better error messages on assert statements, but included no new functionality unlike unittest.

### Part B: Exercises from the end of SDX Ch. 6

Write a short summary of what you did below, with answers to the questions embedded in the exercises.
