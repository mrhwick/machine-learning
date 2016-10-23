# Chapter 1 Exercises

## 1.1

>Give three computer applications for which machine learning approaches seem appropriate and three for which they seem inappropriate. Pick applications that are not already mentioned in this chapter, and include a one-sentence justification for each.

*Appropriate Applications*

1. Dining Experience Recommendations
  - The problem of recommending a specific dining experience to a specific individual is difficult to evaluate at runtime, as it is a unique-to-the-individual characterization of performance.
2. Discerning the expected time taken to read an article
  - This is a natural language processing problem which humans are able to intuitively solve, given a small amount of meta-data about a given piece of literature.
3. Suggesting an ideal room configuration / decoration scheme
  - The problem space is enormous, yet humans can intuitively optimize for particular measures of effective layouts. A machine learning algorithm may outperform humans on balancing the various quality attributes.

*Inappropriate Applications*

1. Decide the best route for a-to-b driving directions
  - This is a problem that has an optimal solution that can be effectively calculated at runtime.
2. Calculate wait time at a counter-service restaurant
  - This is a bounded problem space, given the number of individuals in line ahead of the user and an upper bound of the time taken per customer for ordering.
3. Automated email response system with away message
  - Simply sending the same response email alerting the recipient that the individual is not available for communication requires no decision making capability.

## 1.2

>Pick some learning task not mentioned in this chapter. Describe it informally in a paragraph in English. Now describe it by stating as precisely as possible the task, performance measure, and training experience. Finally, propose a target function to be learned and a target representation. Discuss the main tradeoffs you considered in formulating this learning task.

*Informal Description*

Each time I arrive home, it would be beneficial to me for my garage door to be open before I arrive so that I do not waste time waiting for the door to open. The benefit in time not wasted is heavily offset by an extreme preference that my garage not be opened when I am not arriving, as that would leave my belongings open to theft. A machine learning algorithm for this task would likely attempt to predict my likelihood of arrival based on a number of factors, including my GPS position, the current datetime, and the time which I previously left the garage last, among other data points.

*Formalization*

Task T: Opening the garage door when I am about to arrive at home

Performance Measure P: Length of time between opening the door and my arrival

Training Experience E: A series of controlled experimental arrivals

*Target Function*

Informally, we want to calculate the time at which I will be arriving, such that I do not need to wait for the garage door to fully open before pulling into the garage upon arrival. We actually need both a function that will predict when I am to arrive (regression) and whether I am arriving at home when I leave (classification), but I'll just propose a concept for the regression problem.

Estimate the function f which determines time after departure to begin opening the garage door:

f(x1, x2, ..., xn) = w0 + w1 * x1 + w2 * x2 + ... + wn * xn

where x1 ... xn are the variables accumulated such as day of week, time of day, time taken to wait on the garage door, driving time and time / location of departure from origin prior to arrival, etc.

The weights w0 ... wn will modulate the influence of the various data points so that at any given time in the future we may reasonably predict the likelihood that I am departing for home and attempt to open the door prior to my arrival so that I do not need to wait for the door to finish opening. w0 in particular is a constant weight which will most likely be related to the amount of time it generally takes for the garage door to open on average.

The learning algorithm will need to be shown the effectiveness of various amounts of time to open prior to my arrival. The most negative would be opening immediately upon departure, and will be correlated with the amount of driving time I must complete before arriving home. The more time the door lies open while I am en route, the more likely it is that some ne'er-do-well attempts to steal some item from my garage without my knowledge, and thus the more negative the experience would become in those cases. There is another patch of negatively effective cases, which are all of the times at which I arrive home and must wait for the door to even begin opening (when the algorithm predicts my arrival time as much later than actually occurs). Therefore, the distance (absolute value of the length of time between opening the door and my arrival) is a good measure for performance on this task, since it will capture both the various positive effectiveness scores as well as the overwhelmingly negative effectiveness scores at both ends of the spectrum.

## 1.3

>Prove that the LMS weight update rule described in this chapter performs a gradient descent to minimize the squared error. In particular, define the squared error E as in the text. Now calculate the derivative of E with respect to the weight w_i , assuming that V(b) is a linear function as defined in the text. Gradient descent is achieved by updating each weight in proportion to -d(E)/d(w_i). Therefore, you must show that the LMS training rule alters weights in this proportion for each training example it encounters.

TODO

## 1.4

>Consider alternative strategies for the Experiment Generator module of Figure 1.2. In particular, consider strategies in which the Experiment Generator suggests new board positions by
> * Generating random legal board positions
> * Generating a position by picking a board state from the previous game, then applying one of the moves that was not executed
> * A strategy of your own design
>
>Discuss tradeoffs among these strategies. Which do you feel would work best if the number of training examples was held constant, given the performance measure of winning the most games at the world championships?

First of all, I would propose generating all of the ending states, and then generating the states backwards from there, declining to generate any states which are equivalent to those already generated.

Now, in terms of tradeoffs, generating random legal board positions will likely expose the algorithm to the most individual board layouts, but will be likely to generate many records which are near enough in measured value to be indistinguishable. The distribution of value for board positions is not uniform, so randomly picking board positions would inevitably generate many positions which are not highly useful for establishing the most valuable moves. 

Generating positions by picking previously observed board states and choosing alternative mutations would probably generate a few highly effective strategies, but will neglect to discover other potential maxima that may exist in the search space. Therefore, I would expect such an algorithm to be difficult to defeat at first, but once a trick was discovered to defeat it, the limited strategies which it discovered would be overcome.

Finally, my own strategy would likely create a series of "final play" strategies, which would be unlikely to play well at the beginning of each game, but perform well in a variety of end-game configurations. In the cases where it encountered less skilled human players, which are more prone to possibly making mistakes, this algorithm would generate strategies that would take advantage of late-game ineffectiveness in the humans' strategies. A human would likely discover a strategy which would lure this system into moves which are ineffective in the earliest portions of the game, thus overcoming the relative late-game strength of the system.

# 1.5

>Implement an algorithm similar to that discussed for the checkers problem, but use the simpler game of tic-tac-toe. Represent the learned function V as a linear combination of board features of your choice. To train your program, play it repeatedly against a second copy of the program that uses a fixed evaluation function you create by hand. Plot the percent of games won by your system, versus the number of training games played.

See 1.5 directory.






























