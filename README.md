# sp24-lab4
Materials for Week 4 Lab, which includes "Running Tests adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson.

_February 6, 2024_

Organization:
* SDX-ch6: The code files for the _SDX Ch.6_ activity (as downloaded directly from the book website, unmodified) 

## Team Members for Part 1
John Leeds, Jacob Burrill

## Team Roles for Part 1
Who will start out as
* DRIVER: John
* NAVIGATOR: Jacob

You will switch halfway through the _SDX Ch. 3_ activity.

## Part 1 Documentation

Write your answers to the questions below.

* What were the main ideas from SDX chapter 6?
Using globals() to discover tests. Writing a run_tests() function to run all of your tests at once. 
* What questions did you have about the material in the chapters? What did you find confusing?
What is the '__annotations__' default variable in globals()?
### Part A: Recreate the tests from SDX Ch. 6 in the unittest framework

Write a short description of what you did for Part A below. Some questions you might answer: 
* What was your experience putting the tests in unittest like? 
It was very similar to the other tests we had made in the chapter. Defining a class felt a little bulky. 
* How is this different from Greg Wilson's simple implementation? 
It was different because you had to define a class and didn't have to write a run_tests function. It also included the runtime for the tests as part of the unittest library. 
* How is it similar? 
Writing the testcases was very similar. We came up with test cases and the values we thought they should return. 
* Why might you use pytest over unittest, or vice versa?
We liked unittest because you don't need to install anything extra. However, you do have write more boilerplate code, which can be tedious. 

### Part B: Exercises from the end of SDX Ch. 6

Write a short summary of what you did below, with answers to the questions embedded in the exercises.

We completed all the exercises.  Here are our notes:

1. We get an error if we don't define name before looping through globals.  The second example works because you define "name" before 
creating looping through the globals dictionary so you don't modify it during iteration.

2. Run the testing unit test with `python3 runner.py -t`

4. Timing tests can be helpful so you can evaluate your code's efficiency and you can identify long runtimes.