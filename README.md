# sp24-lab4
Materials for Week 4 Lab, which includes "Running Tests adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson.

_February 6, 2024_

Organization:
* SDX-ch6: The code files for the _SDX Ch.6_ activity (as downloaded directly from the book website, unmodified) 

## Team Members for Part 1
Andrew Tate
Jack Allard
Steven Lin

## Team Roles for Part 1
Who will start out as
* DRIVER: Andrew
* NAVIGATOR: Jack, Steven

You will switch halfway through the _SDX Ch. 3_ activity.

## Part 1 Documentation

Write your answers to the questions below.

* What were the main ideas from SDX chapter 6?
  
  The normal ways of testing using defined testing functions is usually inefficient, the chapter discussed clever, alternative      ways of testing.
  
* What questions did you have about the material in the chapters? What did you find confusing?

  We found the finding functions bit really confusing, we've never encountered that syntax.

### Part A: Recreate the tests from SDX Ch. 6 in the unittest framework

Write a short description of what you did for Part A below. Some questions you might answer: 
* What was your experience putting the tests in unittest like? 
* How is this different from Greg Wilson's simple implementation? 
* How is it similar? 
* Why might you use pytest over unittest, or vice versa?

We thought that the experience of using the unittest framework was pretty seamless. One thing that confused us was how to get the test methods to run, but we figured it out pretty quickly (the __main__ test runner needed to be un-indented.) One difference from Wilson's test implementation is that calling unittest.main() runs all the tests in a given test class, while his testing system iterates over all the tests manually via a run_tests method.

### Part B: Exercises from the end of SDX Ch. 6
We get an error from running the loop without setting name to None, saying that the dictionary size changes.
Otherwise we get a list of stuff that is accesible at the given level the loop was ran.

Write a short summary of what you did below, with answers to the questions embedded in the exercises.

We added the same tests that were in the chapter, along with an additional test to make sure the user wasn't putting in any funky string values. If a string was passed and the function didn't raise an error, it would tell the test class that something was wrong. This took a little while to figure out. 
