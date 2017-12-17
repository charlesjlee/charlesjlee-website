+++
title = "Coursera review: Bitcoin and Cryptocurrency Technologies"
description = ""
tags = [
    "Bitcoin",
    "Coursera",
]
date = "2017-03-01"
categories = [
    "Development",
    "Bitcoin",
]
+++

The [Bitcoin and Cryptocurrency Technologies](https://www.coursera.org/learn/cryptocurrency) Coursera is an 11-week, 4-lecturer collaboration that gives the student an overview of the existing cryptocurrency environment and how it came to be. It begins with a history of cryptocurrency advancements leading up to Bitcoin, then goes into the technical details of how Bitcoin works, moves on to the societal impact of cryptocurrencies, and finally ends with a discussion of future developments and their feasibility.

I took this course during the 12/26/2016 - 03/20/2016 offering and was thoroughly impressed by its quality. I learned a lot from taking the course -- enough to pass the [Certified Bitcoin Professional](https://cryptoconsortium.org/certifications/CBP) exam (see [this post](http://charlesjlee.com/post/C4-Bitcoin-Certified-Professional) for my thoughts on Bitcoin certification). On each topic, the instructors first discuss a motivating problem, then examine a technical solution to the problem, and finally explore the real-world practicality and adoption of this solution. Far from feeding the hype, the lecturers instead examine it to produce nuggets of insights, such as:

* It has been very difficult to make money mining Bitcoin because of the fast pace of hardware evolution. Historically, miners would have been better off investing in the price of Bitcoin instead of their mining rigs.
* Just because something can be decentralized doesn't mean it ever will be. There has to be a compelling use case for decentralization -- usually a financial one.
* Many problems that people are trying to address with new cryptocurrency ideas are fundamentally social problems not technical ones.

The Coursera includes three optional homeworks. The first is to implement part of a simple cryptocurrency called Scrooge Coin. I found this exercise to be challenging and hugely rewarding. The inner-mechanics of Scrooge Coin are mostly the same as Bitcoin's and filling in how transaction inputs and outputs function and interact cemented my understanding of how they work. I had a particularly hard time understanding what an Unspent Transaction Output (UTXO) was and actually having to use one gave me an "aha" moment. That said, some parts of the assignment could have used further explanation and I had to turn to the forums for help. Unfortunately, the instructors were not active on the forums to assist with this.

Sadly, the last two assignments were not as instructive as the first was. Homework #2 has you implementing a distributed consensus algorithm on a random graph with malicious nodes. Though interesting, this exercise has strangely little to do with the lectures. It was also disappointing that the simplest heuristic is sufficient to pass 80% of the test cases. Homework #3 has you revisiting the code used in #1 to implement a node to receive incoming transactions and blocks and maintain an updated block chain. Again, this exercise was only tangentially related to the lectures. I didn't have any revelations this time around and revisiting the same code made this exercise feel like house-keeping.

The course ends with a lecture on the "Future of Bitcoin". Here, the lecturer doesn't speculate about how popular Bitcoin will become but rather offers a technical discussion of what is currently possible, what may become possible, and the societal impact of and resistance to adopting these ideas. With tempered enthusiasm, the lecturer explains how it's possible to use block chains to de-centralize property ownership, betting, file storage, etc. but that often the primary barrier to adoption is social not technical. See [here](http://bitcoin.stanford.edu) and [here](https://crypto.stanford.edu/cs251) for courses on these forward-looking applications.

My only reservation in recommending this course is that it's a bit dated. The majority of lectures were recorded in 2014 and some references are outdated, e.g. global hash rate, price of BTC, status of NY BitLicense, and the status of Ethereum. My lament here is not that the information is no longer up-to-date but that the authors missed an opportunity to discuss recent developments, such as the approval of the NY BitLicense and what kind of precedent it set, the current state of international regulation and its effect on block chain adoption, the proliferation of Bitcoin ATM's and the effect of readily available BTC to physical fiat conversation, the rise of Ethereum and other altcoins, etc. Since it's unlikely that the lecturers will record new videos that discuss these recent developments, you can instead find more up-to-date material in their [book](http://bitcoinbook.cs.princeton.edu).