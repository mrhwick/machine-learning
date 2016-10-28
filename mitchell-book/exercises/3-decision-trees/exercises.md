# Chapter 3 Exercises

## 3.1

>Give decision trees to represent the following boolean functions: 
>(a)A AND -B
>(b)A OR [B AND C]
>(c) A XOR B
>(d)[A AND B] OR [C AND D]

(a)A AND -B

![image](https://cloud.githubusercontent.com/assets/865759/19780981/53724372-9c55-11e6-92c1-f3bff15f1db4.png)

(b)A OR [B AND C]

![image](https://cloud.githubusercontent.com/assets/865759/19780948/390a419c-9c55-11e6-8dcb-8371b3babcab.png)

(c) A XOR B

![image](https://cloud.githubusercontent.com/assets/865759/19780804/91f11af2-9c54-11e6-8a76-934ebabd3ec3.png)

(d)[A AND B] OR [C AND D]

![image](https://cloud.githubusercontent.com/assets/865759/19781012/73ac2806-9c55-11e6-853d-1de4cb4b7d99.png)

## 3.2

>Consider the following set of training examples:
![image](https://cloud.githubusercontent.com/assets/865759/19781077/b2bea03c-9c55-11e6-873e-0a5d98e2efb6.png)

> (a) What is the entropy of this collection of training examples with respect to the target function classification?
>(b) What is the information gain of a2 relative to these training examples?

#### (a)

One half of the examples is positive, and one half of the examples is negative, therefore these examples have split the classification equally and produce an entropy of 1.

#### (b)

The examples for which a2 has value 'T' are equally split between positive and negative examples, with 2 each. The examples for which a2 has value 'F' are also equally split between positive and negative eamples, with 1 each. This being the case, selecting over the attribute a2 will not create and additional amount of information gain, meaning that it will not reduce the entropy below the baseline entropy of 1 for these examples.

## 3.3

>True or false: If decision tree D2 is an elaboration of tree D1, then D1 is more-general-than D2. Assume D1 and D2 are decision trees representing arbitrary boolean functions, and that D2 is an elaboration of D1 if ID3 could extend D1 into D2. If true, give a proof; if false, a counterexample. (More-general-than is defined in Chapter 2.)

False.

Assume, for example, the decision trees D1 and D2 are representative of the corresponding boolean functions below:

D1. A AND -B
D2. A AND [B OR C]

In this case, a decision tree that represents D1 can be elaborated to create an alternative decision tree D2, but there exists an instance for which D1 will classify positive and D2 will classify negative.

A = T, B = F, C = F will be classified as positive by D1 and negative by D2.

## 3.4

>ID3 searches for just one consistent hypothesis, whereas the CANDIDATE- ELIMINATION algorithm finds all consistent hypotheses. Consider the correspondence between these two learning algorithms.
>
>(a) Show the decision tree that would be learned by ID3 assuming it is given the
four training examples for the Enjoy Sport? target concept shown in Table 2.1
of Chapter 2.
>
>(b) What is the relationship between the learned decision tree and the version space
(shown in Figure 2.3 of Chapter 2) that is learned from these same examples? Is the learned tree equivalent to one of the members of the version space?
>
>(c) Add the following training example, and compute the new decision tree. This time, show the value of the information gain for each candidate attribute at each
step in growing the tree.
>
>Sky Air-Temp Humidity Wind Water Forecast Enjoy-Sport? Sunny Warm Normal Weak Warm Same No
>
>(d) Suppose we wish to design a learner that (like ID3) searches a space of decision
tree hypotheses and (like CANDIDATE-ELIMINATION) finds all hypotheses consistent with the data. In short, we wish to apply the CANDIDATE-ELIMINATION algorithm to searching the space of decision tree hypotheses. Show the S and G sets that result from the first training example from Table 2.1. Note S must contain the most specific decision trees consistent with the data, whereas G must contain the most general. Show how the S and G sets are refined by thesecond training example (you may omit syntactically distinct trees that describe the same concept). What difficulties do you foresee in applying CANDIDATE-ELIMINATION to a decision tree hypothesis space?

#### (a)

![image](https://cloud.githubusercontent.com/assets/865759/19808196/9ea9cb70-9cf1-11e6-8304-3daf57c1b020.png)

#### (b)

TODO

#### (c)

TODO

#### (d)

TODO







































