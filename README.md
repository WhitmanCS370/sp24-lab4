# sp24-lab4

Materials for Week 4 Lab, which includes "Running Tests adapted from [Software Design by Example](https://third-bit.com/sdxpy/) by Greg Wilson.

_February 6, 2024_

Organization:

- SDX-ch6: The code files for the _SDX Ch.6_ activity (as downloaded directly from the book website, unmodified)

## Team Members for Part 1

Fabian, Uli, Jas

## Team Roles for Part 1

Who will start out as

- DRIVER: Fabian
- NAVIGATOR: Uli, Jas

You will switch halfway through the _SDX Ch. 3_ activity.

## Part 1 Documentation

Write your answers to the questions below.

- What were the main ideas from SDX chapter 6?
  Writing the testcases and how to go about testing

- What questions did you have about the material in the chapters? What did you find confusing?
  N/A

### Part A: Recreate the tests from SDX Ch. 6 in the unittest framework

Write a short description of what you did for Part A below. Some questions you might answer:

- What was your experience putting the tests in unittest like?
  Very straighforward and easy to use. Made our tests simpler and faster
- How is this different from Greg Wilson's simple implementation?
  It gives us a structure to easily test lots of test cases at once
- How is it similar?
  We are still writing a new function/method for each test case
- Why might you use pytest over unittest, or vice versa?
  We can use pytest for a more simple code using decoraters while unittest we would have to manually write each testcase.

### Part B: Exercises from the end of SDX Ch. 6

Write a short summary of what you did below, with answers to the questions embedded in the exercises.

We created code that would look for setup and teardown function and just call setup once before tests are run and call teardown once tests are done running. We then created code to test the run time of the test functions. Then created code that would take user input from the CLI and run test with the prefix given by the user.
