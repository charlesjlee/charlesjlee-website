+++
title = "Bitcoin beacon: using the blockchain to generate random bits"
description = 'a Python implementation of the paper "On Bitcoin as a public randomness source"'
tags = [
    "Bitcoin",
    "blockchain",
    "Python",
]
date = "2017-07-16"
categories = [
    "Development",
    "blockchain",
]
+++

## Random beacons
A random beacon is "a trusted service that broadcasts fresh random numbers at regular intervals". Random beacons are useful in situations that demand security against manipulation, e.g. choosing precincts to audit after an election. Several beacon services currently exist, notably Random.org and the NIST beacon, however there are several advantages to using the Bitcoin blockchain as a source of randomness:

* Publicly verifiable
  - Bitcoin blocks are public as soon as they are mined so anyone can perform and verify the beacon computations.
* No trusted parties
  - Using proprietary services requires that you trust the operator of that service. In the case of [random.org](https://www.random.org/), they publicly state that they buffer their random numbers[<sup>1</sup>][1], i.e. they generate the numbers before they are requested. This means that they could be in a position to profit from advance knowledge of the beacon output. Analogously, [NIST](https://www.nist.gov/programs-projects/nist-randomness-beacon) previously promoted the Dual_EC_DRBG standard, which it has now admitted contained a backdoor for the NSA to exploit. Additionally, the NIST beacon was offline during the 2013 US Government shutdown.
* Precise security guarantees
  - Due to the cryptographic structure of the Bitcoin blockchain and its use as a currency, it is possible to concretely analyze the entropy generated and the the monetary cost of compromising the beacon output.

In their paper, _On Bitcoin as a public randomness source_[<sup>2</sup>][2], Joseph Bonneau, Jeremy Clark, and Steven Goldfeder provide such a construction and analysis. Specifically, they conclude that

>> at least 68 bits of min-entropy are produced every 10 minutes [the average Bitcoin block time], from which one can derive over 32 near-uniform bits using standard extractor techniques

>> a lottery producing a single unbiased bit is manipulation-resistant against an attacker with a stake of less than 50 bitcoins

## Summary of beacon construction
The beacon construction provided in the paper is a single computation with three components: $$ Beacon(t) = Ext_k (B_t || H(B_t)) $$

* $Ext_k$
    - This is an extractor function that takes in $n$ bits with sufficient entropy and returns $m$ bits with high entropy, i.e. uniform distribution. The extractors discussed (HMAC's and block ciphers in CBC-MAC mode) work best when the input has at least $2m$ bits of min-entropy; this is why our output $m$ is roughly $n \over 2$ bits.
* $B_t$
    - The 640-bit block header. A valid block must have a hash value starting with $d$ (68 at the time of writing) consecutive zeros. This is the source of the $d$ bits of min-entropy, or inherent randomness, that powers the beacon. The $d$ bits are actually spread across two fields (Merkle hash of transactions and nonce) in the header, but we capture both by using the entire header.
* $H(B_t)$
    - By including the hash of the header, we make it impossible for malicious miners to exclusively trying hash solutions that produce a certain beacon output. Since the hash of the header is unpredictable, malicious miners must mine normally: finding valid hash solutions, computing the beacon output, then deciding whether to withhold the block.

## Beacon construction in Python
<iframe src="/files/20170716-Bitcoin-beacon.html" width="100%" height="2475" scrolling="yes" frameBorder="0" seamless="seamless"></iframe> 

## Cost of manipulation
The paper begins by considering the simplest case of a single-stage lottery (multi-stage lotteries are discussed in Appendix A), where the attacker stands to win reward $W$ with probability $p$ and the lottery outcome is decided on a single beacon output. The paper models a strong _bribing attacker_ "who is able to [successfully] pay any miner exactly $B$ [the block reward] to suppress a valid block whenever the attacker desires". This bribing attacker's power to manipulate the beacon is equivalent to that of a mining pool with 100% of the network's hashing power.

The authors conclude that "a single stage lottery is manipulation-resistant [it would cost more than the bribing attacker's expected winnings] against any binary [do nothing or attack the beacon] attacker who has a stake less than $1 \over p$ in an event with probability $p$". Thus if we use a single bit generated from the beacon to decide the lottery outcome, then the lottery is manipulation-resistant against an attacker who has less than $2B$ at stake.

Intuitively, the bribing attacker expects to win $pW$ without doing anything. To incentive him to attack the beacon by withholding blocks until he finds a winning one (Appendix B.1 shows that "it is always in the attackers' interest to prune completely or not at all), the reward $W$ must be high enough.

If he decides to attack, then he is presented with future block candidates, where each block candidate has probability $1 \over 2$ of winning the lottery and costs $B$ to reject (if it doesn't win). This is a geometric distribution where the expected number of failures before the first success is $(1-p) \over p$[<sup>3</sup>][3].

So we have  
$$(earnings\ from\ manipulating\ beacon) > (expected\ earnings\ if\ do\ nothing)$$
$$(lottery\ stake) - (cost\ to\ manipulate\ beacon) > (expected\ earnings\ if\ do\ nothing)$$
$$W - {(1-p) \over p} > pW$$
$$W > {1 \over p}$$

In our case, $p={1 \over 2}$, so $W$ must be greater than $2B$ and we arrive at our conclusion. To give some context, the block reward on July 10, 2017 is <i class="fa fa-btc"></i>12.5 or $30,000.

## Extensions and further work
We covered one implementation of a beacon based on the Bitcoin blockchain. Here are some ways to take this idea of a blockchain-based beacon further:

* Use an asymmetric slow hash function to make the beacon slow to compute but fast to verify. This will prevent the bribing attacker from quickly deciding whether to withhold blocks, but still allow anyone to verify that the beacon was computed correctly. This is discussed further in Section 6.1.

* Revisit the beacon construction to provide higher (or even adjustable) levels of randomness. In _Bitcoin Beacon_[<sup>4</sup>][4], Bentov, Gabizon, and Zuckerman provide a construction that outputs only a single random bit per block but with much stronger guarantees than we discussed here. Their key idea is to take the headers from the last $n$ blocks.

* Compute and analyze the observed beacon values to validate the theoretical results, i.e. that the beacon is indeed random.

* Turn the Jupyter notebook into an API.

* Apply similar analysis to altcoins, e.g. Ethereum, Steem, Monero. Due to their difference in complexity and implementation, they may provide different security and manipulation cost results.

## References
1. https://www.random.org/faq/
2. https://eprint.iacr.org/2015/1015
3. https://en.wikipedia.org/wiki/Geometric_distribution
4. https://arxiv.org/abs/1605.04559

[1]: https://www.random.org/faq/
[2]: https://eprint.iacr.org/2015/1015
[3]: https://en.wikipedia.org/wiki/Geometric_distribution
[4]: https://arxiv.org/abs/1605.04559