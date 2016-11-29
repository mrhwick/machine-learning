# Chapter 10 Exercises

## 10.1

> Consider a sequential covering algorithm such as CN2 and a simultaneous covering algorithm such as ID3. Both algorithms are to be used to learn a target concept defined over instances represented by conjunctions of n boolean attributes. If ID3 learns a balanced decision tree of depth d, it will contain 2^d - 1 distinct decision nodes, and therefore will have made 2^d - 1 distinct choices while constructing its output hypothesis. How many rules will be formed if this tree is re-expressed as a disjunctive set of rules? How many preconditions will each rule possess? How many distinct choices would a sequential covering algorithm have to make to learn this same set of rules? Which system do you suspect would be more prone to overfitting if both were given the same training data?

There will be `2^d` paths through the tree, and each path can be directly converted into a rule, with each decision node along the path representing a distinct precondition of the rule. We can remove all paths which result in a negative classification, as we are only interested in exercising rules that will positively classify new examples and can default to a negative classification if no rule applies to the example. Alternatively, we can use these assumptions in reverse for problems that generally have positive classifications and for which the negative classifications are of interest. Therefore, there will be `(2^d)/2` rules learned.

The rules so converted out of the distinct paths within the tree will each contain `d+1` preconditions, because each path will be of depth `d`, with a root node at the beginning of each path adding a single additional precondition that all paths hold in common. 

In order to learn the rules, a sequential covering algorithm would make `((2^d)/2)*(d+1)` choices.

I suspect that the decision tree will be less likely to overfit the training data, though it will contain information about the negative classifications present in the training data which the rule-based representation will not contain. The rule-base representation will contain replications of the example values of each attribute within the preconditions of various rules. This means that these algorithms will be more tightly fit to a limited amount of data by generating rulesets that concisely describe the example values available.

## 10.2

>Refine the LEARN-ONE-RULE algorithm of Table 10.2 so that it can learn rules whose preconditions include thresholds on real-valued attributes (e.g., temperature > 42). Specify your new algorithm as a set of editing changes to the algorithm of Table 10.2. Hint: Consider how this is accomplished for decision tree learning.

![image](https://cloud.githubusercontent.com/assets/865759/20673692/1e899166-b554-11e6-8cf3-dd2e8ead141b.png)

I would adjust the portion of this algorithm related to creating the `All_constraints` set to include additional steps for generating additional discrete-valued attributes from the real-valued attributes. Such steps would do the following for all real-valued attributes:

1. Sort the examples which contain each attribute over the attribute.
2. Search for values at which adjacent examples have different classifications, and find the midpoints between each pair of adjacent example values. These will be the candidate thresholds.
3. Calculate the information gain which would result from using each candidate threshold as the threshold for the new discrete-valued attribute, and select the candidate threshold with the highest information gain.
4. Create a discrete-valued attribute constraint.

Using these adjustments, real-valued attributes can be used alongside discrete-valued attributes by way of converting real-valued atributes into discrete-valued attributes using thresholds over the range of real values in the observed examples.

## 10.3

>Refine the LEARN-ONE-RULE algorithm of Table 10.2 so that it can learn rules whose preconditions include constraints such as nationality is one of {Canadian,Brazilian}, where a discrete-valued attribute is allowed to take on any value in some specified set. Your modified program should explore the hypothesis space containing all such subsets. Specify your new algorithm as a set of editing changes to the algorithm of Table 10.2.

![image](https://cloud.githubusercontent.com/assets/865759/20673692/1e899166-b554-11e6-8cf3-dd2e8ead141b.png)

I would again adjust the portion of the algorithm related to create the `All_constraints` set to include an additional step for generating a discrete-valued attribute related to each value from the avaiable values for the attributes of this type. This expansion operation would make the set of candidate constraints larger by "the number of possible values for the given attribute - 1".

## 10.4

>Consider the options for implementing LEARN-ONE-RULE in terms of the possible strategies for searching the hypothesis space. In particular, consider the following attributes of the search:
>
>(a) generate-and-test versus data-driven
>(b) general-to-specific versus specific-to-general
>(c) sequential cover versus simultaneous cover
>
>Discuss the benefits of the choice made by the algorithm in Tables 10.1 and 10.2. For each of these three attributes of the search strategy, discuss the (positive and negative) impact of choosing the alternative option.

![image](https://cloud.githubusercontent.com/assets/865759/20676232/1989cc90-b55d-11e6-9801-4fe3633cb51c.png)


![image](https://cloud.githubusercontent.com/assets/865759/20673692/1e899166-b554-11e6-8cf3-dd2e8ead141b.png)

(a) Generate-and-test versus example-driven

Table 10.2 uses the generate-and-test strategy for hypothesis consideration. This has the benefit of testing each addition to the hypothesis is tested for performance over all of the training data available, which will reduce the amount of overfitting to erroneous data that occurs. In the alternative option of example-driven, each example is taken in turn and used to refine the hypothesis, which will create hypotheses that are more easily overfit to bad training examples. Using algorithms which are example-driven will result in fewer necessary calculations to generate the hypothesis, so faster learning times, but perhaps faulty hypotheses.

(b) general-to-specific versus specific-to-general

The main advantage of the general-to-specific search present in Table 10.2 is that we have a clear origin from which to begin our search, the maximally general hypothesis that classifies all examples as positive. The alternative of specific-to-general has the advantage that while there is not a clear origin for the search, the generalization of the hypothesis follows the natural progression of accounting for all negative examples in the training data.

(c) sequential cover versus simultaneous cover

Table 10.1 uses the sequential covering strategy, which has the benefit of generating a very precise representation of the hypothesis, although it does more operations to generate that hypothesis representation. In the presence of abundant data, the sequential covering algorithm will make more precise predictions based on the available values for each attribute. The alternative of simultaneous cover strategies would likely be more useful in a situation with less data, since the decisions made will be more generalized for the unknown values, but in a data-abundant environment will stop short in specializing the hypothesis.

## 10.5

>Apply inverse resolution in propositional form to the clauses `C = A v B`, `C1 = A v B v G`. Give at least two possible results for C2.

```
C2 = A v B v ¬G
```

```
C2 = A v ¬G
```

## 10.6

>Apply inverse resolution to the clauses `C=R(B, x) v P(x, A)` and `C1=S(B, y) v R(z, x)` . Give at least four possible results for C2. Here A and B are constants, x and y are variables.

```
L_1 = S(B, y)
θ_1 = {}
θ_2 = {B/t}

C_2 = R(t, x) v P(x, A) - R(z, x) v ¬S(t, y)
```

```
L_1 = S(B, y)
θ_1 = {z/C}
θ_2 = {A/t}

C_2 = R(B, x) v P(x, t) - R(C, x) v ¬S(B, y)
```

```
L_1 = R(z, x)
θ_1 = {}
θ_2 = {B/t}

C_2 = R(t, x) v P(x, A) - S(t, y) v ¬R(z, x)
```

```
L_1 = R(z, x)
θ_1 = {z/C}
θ_2 = {A/t}

C_2 = R(B, x) v P(x, t) - S(B, y) v ¬R(C, x)
```

## 10.7

>Consider the bottom-most inverse resolution step in Figure 10.3. Derive at least two different outcomes that could result given different choices for the substitutions θ1 and θ2. Derive a result for the inverse resolution step if the clause `Father(Tom, Bob)` is used in place of `Father(Shannon, Tom)`.

```
θ_1 = {}
θ_2 inverse = {Bob/x}
C = GrandChild(Bob, Shannon)
C_1 = Father(Shannon, Tom)

C_2 = GrandChild(x, Shannon) v ¬Father(Shannon, Tom)

θ_1 = {}
θ_2 inverse = {Bob/x, Tom/y, Shannon/z}
C = GrandChild(x, Shannon) v ¬Father(Shannon, Tom)
C_1 = Father(Tom, Bob)

C_2 = GrandChild(x, z) v ¬Father(z, y) v ¬Father(y, x)
```

```
θ_1 = {}
θ_2 inverse = {Tom/x}
C = GrandChild(Bob, Shannon)
C_1 = Father(Shannon, Tom)

C_2 = GrandChild(Bob, Shannon) v ¬Father(Shannon, x)

θ_1 = {}
θ_2 inverse = {Tom/x, Bob/y, Shannon/z}
C = GrandChild(Bob, Shannon) v ¬Father(Shannon, x)
C_1 = Father(Tom, Bob)

C_2 = GrandChild(y, z) v ¬Father(z, x) v ¬Father(x, z)
```

```
θ_1 = {}
θ_2 inverse = {Shannon/x}
C = GrandChild(Bob, Shannon)
C_1 = Father(Tom, Bob)

C_2 = GrandChild(Bob, x) v ¬Father(Tom, Bob)

θ_1 = {}
θ_2 inverse = {Shannon/x, Tom/y, Bob/z}
C = GrandChild(Bob, x) v ¬Father(Tom, Bob)
C_1 = Father(Shannon, Tom)

C_2 = GrandChild(z, x) v ¬Father(y, z) v ¬Father(x, y)
```

## 10.8

>Consider the relationship between the definition of the induction problem in this chapter:
>
>![image](https://cloud.githubusercontent.com/assets/865759/20684158/cb177c04-b57c-11e6-84fb-ea776998bfc3.png)
>
>
>and our earlier definition of inductive bias from Chapter 2, Equation 2.1. There we defined the inductive bias, B_bias,by the expression
>
>![image](https://cloud.githubusercontent.com/assets/865759/20684180/d73cd2c2-b57c-11e6-9c2c-372f8510d171.png)
>
>where `L(x_i, D)` is the classification that the learner assigns to the new instance `x_i` after learning from the training data `D`, and where `X` is the entire instance space. Note the first expression is intended to describe the hypothesis we wish the learner to output, whereas the second expression is intended to describe the learner's policy for generalizing beyond the training data. Invent a learner for which the inductive bias `B_bias` of the learner is identical to the background knowledge `B` that it is provided.

TODO
















