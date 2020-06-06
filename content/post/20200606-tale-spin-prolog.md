+++
title = "TALE-SPIN in Prolog"
description = "story generation through search"
tags = [
    "Prolog",
    "story generation",
]
date = "2020-06-06"
categories = [
    "Development",
]
+++

## TALE-SPIN
TALE-SPIN[<sup>1</sup>][1] is an AI program developed in 1977 by James R. Meehan. It works by using a knowledge base of actions to solve and modify goals. As actions are performed, they output text that form a story. In the words of the author:
>TALE-SPIN is a problem solver, top-down and goal-directed. Its output may be regarded as a trace through problem-solving procedures.

Meehan rejected previous approaches with clean formulations that involved defining "one kind" of knowledge but sometimes resulted in bizarre stories. He instead defined and incorporated multiple kinds of knowledge to create more natural stories.

Similarly, the goal-tracking system started as simply a stack of goals, but gradually grew in complexity to account for:
- duplicate goals
- separate goals for each character
- permanent goal states, e.g. self-preservation, in the inference step
- recognizing when a goal
  - is superseded
  - can be safely abandoned
  - should be retired in light of new information

This is a high-level flowchart of TALE-SPIN. There are a few interesting points to note here:
1. every story starts with a single `sigma-state` -- hunger, thirst, rest, sex -- as a goal
2. Meehan uses the term "planbox" to refer to the list of pre-conditions, subgoals (aka actions), post-conditions, and post-actions that must be satisfied to complete a goal. With this in mind, we can see how solving the initial `sigma-state` goal leads to an explosion of subgoals.
3. the inference mechanism is responsible for capturing complex and cascading interactions, e.g. I'm hungry and ask Bobby for food. Bobby answers by telling me where to find a beehive. A beehive is not food, but can lead to food by scooping out the honey inside.

{{<fluid_lightbox_imgs
    "pure-u-1-2|/img/20200606-tale-spin-prolog-flow.svg|TALE-SPIN flowchart"
>}}

Meehan defines six types of goals. These goals encapsulate knowledge of the world by having "planbox" definitions that include other goals, e.g. a pre-condition for stealing is having a certain personality and relationship with the victim.
{{<pure_table
    "Name|Top-level goal|Pre-condition|Subgoal|Post-condition|Post-action|Primitives|Examples"
    "delta-act|✓|✓|✓|✓|✓|n/a|DELTA-CONTROL"
    "PERSUADE|✓|✓|✓|✓|✓|n/a|requesting, proposing, bargaining, threatening"
    "sigma-state|✓|✓||✓|✓|hunger, thirst, rest, sex|"
    "relationships||✓|✓|✓||competition, dominance, familiarity, affection, trust, deceit, indebtedness|"
    "personalities||✓||✓||kindess, vanity, honesty, intelligence|"
    "maps||✓||✓|||"
>}}

## TALE-SPIN in Prolog
Our final project for Advanced Prolog class was to write our own version of the TALE-SPIN story generator. To avoid spending years on this project, I chose to make many simplifications, the major ones being:
1. a simple stack of goals
2. only one kind of knowledge
3. no inference mechanism

The resulting flowchart looks like this:
<should always be able to generate a list of actions>
{{<fluid_lightbox_imgs
    "pure-u-1-2|/img/20200606-tale-spin-prolog-flow-mine.svg|My TALE-SPIN flowchart"
>}}

I defined a very narrow knowledge base focused on being hungry and trying to make a sandwich. Compared to the original TALE-SPIN, my scope is microscopic ([source code](https://github.com/charlesjlee/prolog/blob/master/talespin.pl), [run online](https://swish.swi-prolog.org/p/talespin.swinb)).

This is a sample run of `generate_story(_{name:"John",gender:male}, Story).`
>One day, John was in the kitchen and he was hungry. He decided to make a BLT sandwich. John took a tomato out of the fridge. John took some bacon out of the fridge. John took some lettuce out of the fridge, but it was moldy and spoiled. John took some lettuce out of the fridge. John took some bread out of the pantry. Then he used the tomato, bacon, lettuce, and bread to make a sandwich. John took a big bite out of his sandwich. Too big. It slipped out of his hand onto the floor. Great. Now he had to start all over. John took a tomato out of the fridge. John took some bacon out of the fridge. John took some lettuce out of the fridge. John took some bread out of the pantry. Then he used the tomato, bacon, lettuce, and bread to make a sandwich. Finally, careful not to drop anything on the floor, John ate his sandwich - the whole, entire thing. With a full belly, John could now get on with the rest of his day. THE END

## References
1. The original paper is fairly accessible and contains several examples of generated stories. You can find a copy [here](https://www.cs.utah.edu/nlp/papers/talespin-ijcai77.pdf). Unfortunately, the original code is lost forever, but a [simplified version is available](https://news.ycombinator.com/item?id=9948653).

[1]: #references
