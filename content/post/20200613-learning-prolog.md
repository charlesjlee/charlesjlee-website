+++
title = "My Experience Learning Prolog"
description = "a journey in PROgramming in LOGic"
tags = [
    "Prolog",
]
date = "2020-06-13"
categories = [
    "Development",
]
+++

I first heard about the Prolog programming language in the book [Seven Languages in Seven Weeks](https://www.amazon.com/Seven-Languages-Weeks-Programming-Programmers/dp/193435659X). The book, as promised, introduces the reader to the syntax and paradigms of seven different languages. What attracted me to Prolog was its similarity to constraint programming (programs are defined by and solved using their constraints), its similarity to SQL (data-focused and declarative), and its recursive nature.

Normally, I would learn a new language by playing with it, but Prolog was too foreign and intimidating, so I looked for a more structured learning approach. I did some research on recommended first textbooks to work through and settled on [The Art of Prolog](https://mitpress.mit.edu/books/art-prolog-second-edition) (AoP). This was a terrible decision. AoP is structured in four parts: logic programming, Prolog, advanced Prolog, and applications. Over two weeks, I completed Part I and worked through all the exercises using pen and paper. I was inspired by the beauty and simplicity of logic programs, and was excited to start Part II, which introduces the Prolog language and its shortcomings as a logic programming language. The exercises in Part II were essentially the same as in Part I, except using Prolog instead of pure logic. The solutions were ugly. I felt disillusioned at being introduced to beauty and then being denied it. I put AoP away and gave up on Prolog.

(Note: having learned basic Prolog, I can see now that AoP is a great book and plan to revisit it; it's just not for beginners not interested in theory.)

About a year and a half later, I was browsing HN and came upon [this](https://news.ycombinator.com/item?id=22790850) thread, where people were talking about what projects they were working on during the COVID-19 lockdown. Someone said that a Prolog class was starting ... next week! I signed up for both the Beginner and Advanced courses, which were taught by by Anne Ogborn, a long-time contributer to and speaker on SWI-Prolog. I very much enjoyed Anne's and the course textbook's ([Programming in Prolog](https://www.amazon.com/Programming-Prolog-Using-ISO-Standard/dp/3540006788)) practical learning approach, which focused on coding in Prolog with a sprinkling of logic programming theory.

I walked away from the beginner course (into the advanced course) comfortable writing basic Prolog. I used my new skills to [rewrite a program](https://www.charlesjlee.com/post/20200605-prolog-chopsticks/) I had started and abandoned using Python several years ago. The advanced course was a survey of several extensions and libraries plus [a capstone project](https://www.charlesjlee.com/post/20200606-tale-spin-prolog/). After the advanced course, I felt like I could use Prolog for anything! To my surprise, SWI-Prolog supports [distributed computing](https://www.swi-prolog.org/pldoc/man?section=pengine-overview), [web services](https://www.swi-prolog.org/howto/http/), [identity management](https://www.swi-prolog.org/pack/list?p=identity), and other modern features. Not coincidentally, [powering application development](https://www.swi-prolog.org/features.html) is the direction that Jan Wielemaker, the primary developer and maintainer of SWI-Prolog, is taking the language.

We were fortunate to have Jan give a [guest lecture](https://www.youtube.com/watch?v=oX01oI1K2VA) to close out the beginner course. I really liked how he summarized the positioning of Prolog in his final slide, so I'm reproducing it here in graphical form:

{{<fluid_lightbox_imgs
    "pure-u-1-2|/img/20200613-learning-prolog.png|Positioning of Prolog" 
>}}

So what's next? I plan to continue using Prolog for small projects. Maybe I'll work my way up to creating my own library or submitting a PR to improve some predicates. I can see Prolog becoming my primary hobby language.