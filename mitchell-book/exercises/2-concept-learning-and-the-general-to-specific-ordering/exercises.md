# Chapter 2 Exercises

## 2.1

>Explain why the size of the hypothesis space in the EnjoySport learning task is 973. How would the number of possible instances and possible hypotheses increase with the addition of the attribute Watercurrent, which can take on the values Light, Moderate, or Strong? More generally, how does the number of possible instances and hypotheses grow with the addition of a new attribute A that takes on k possible values?

The number of hypotheses in the hypothesis space in the EnjoySport learning task is a logically limited subset of the entire hypothesis space for learning any concept whatsoever. The first limitation on the hypothesis space is to calculate only those hypotheses which cover the possible values of each attribute as well as the special logical notions of "?" (which indicates any value of a given attribute is viable for the hypothesis to produce a positive classification) and "Ø" (which indicates that no value of a given attribute will relate to a positive classification). This limitation imposes a specific boundary of the number of hypotheses that actual describe the task, which is equivalent to (5 sky attributes) * (4 airtemp) * (4 humidity) * (4 wind) * (4 water) * (4 forecast) = 5120 possible hypotheses.

Although this is the total bounds of the hypothesis space, the only hypotheses that are pratically useful in applications is the space which produces hypotheses for positive classification. Therefore, we can impose an additional limitation to the hypothesis space which will remove any hypotheses that are logically certain to produce negative classification. This is easily achieved by removing the set of hypotheses which contain the "Ø" logical symbol, which indicates that no value of that attribute will enable that hypothesis to produce a positive classification. Removing that set of hypotheses imposes an additional boundary on the number of hypotheses that describe the task, now leaving (4 sky attributes) * (3 airtemp) * (3 humidity) * (3 wind) * (3 water) * (3 forecast) = 973.

If we were to introduce an additional attribute into the learning task with 3 possible observed values, it would increase the hypothesis space which produces positive classifications by an additional 4x multiplier, and the number of instances by a 3x multiplier. The hypothesis space increase results from multiplying the existing space by the three additional possibilities for new values, as well as adding all hypotheses which will take any value from this new attribute and still classify positively. In general, this increase for a generic attribute A (with k possible values) will be 

```
H' = H * (k + 1)

where:
H' is the new hypothesis space
H is the hypothesis space prior to introduction of the attribute A
k is the number of possible values for attribute A
and (k + 1) is the number of possible values for attribute A 
  which would result in positive classification, given that the logical 
  value "?" indicates any value for attribute A produces a positive.
```

## 2.2

>Give the sequence of S and G boundary sets computed by the CANDIDATE-ELIMINATION algorithm if it is given the sequence of training examples from Table 2.1 in reverse order. Although the final version space will be the same regardless of the sequence of examples (why?), the sets S and G computed at intermediate stages will, of course, depend on this sequence. Can you come up with ideas for ordering the training examples to minimize the sum of the sizes of these intermediate S and G sets for the H used in the EnjoySport example?

#### Running the examples in reverse order

*Initial*

```
S: (<Ø, Ø, Ø, Ø, Ø, Ø>)
G: (<?, ?, ?, ?, ?, ?>)
```

*First Example*

`<sunny, warm, high, strong, cool, change> = yes`

```
S: (<sunny, warm, high, strong, cool, change>)
G: (<?, ?, ?, ?, ?, ?>)
```

*Second Example*

`<rainy, cold, high, strong, warm, change> = no`

```
S: (<sunny, warm, high, strong, cool, change>)
G: (<sunny, ?, ?, ?, ?, ?>; <?, warm, ?, ?, ?, ?>; <?, ?, ?, ?, cool, ?>;)
```

*Third Example*

`<sunny, warm, high, strong, warm, same> = yes`

```
S: (<sunny, warm, high, strong, ?, ?>)
G: (<sunny, ?, ?, ?, ?, ?>; <?, warm, ?, ?, ?, ?>;)
```

*Fourth Example*

`<sunny, warm, normal, strong, warm, same> = yes`

```
S: (<sunny, warm, ?, strong, ?, ?>)
G: (<sunny, ?, ?, ?, ?, ?>; <?, warm, ?, ?, ?, ?>;)
```

The final hypothesis space will be the same because the information contained in the same examples (regardless of order) will create similar generalization and specialization actions over the space. The information eventually brings all hypotheses into consistency with the total known information held within the set of examples themselves. The ordering simply orders the actions taken to approximate that information.

Ordering the examples by using the positive examples to take generalization actions first will minimize the number of hypotheses that exist in each step of specialization when we begin iterating over the negative examples. I cannot think of any other ordering over the examples that would reduce the number of hypothesis further other than perhaps arranging them by sorting over the attributes with the smallest value spaces first. That might be an ordering that would eliminate more hypotheses in each step, given that the hypotheses necessary to cover the attribute's various values would be arranged in fewer sets.

## 2.3

TODO

## 2.4

TODO

## 2.5

TODO

## 2.6

TODO

## 2.7

TODO

## 2.8

TODO

## 2.9

TODO

## 2.10

TODO
































