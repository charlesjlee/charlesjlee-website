+++
title = "GPT-2 Twitter bot"
description = ""
tags = [
	"deep learning",
    "Twitter",
]
date = "2021-02-05"
categories = [
    "",
]
+++

## aitextgen
I've been loosely following developments in machine learning since the [AlexNet](https://en.wikipedia.org/wiki/AlexNet) days back in 2012. I was particularly excited by OpenAI's release of GPT-2 in 2019 because it seemed like "the solution for everything". But sadly, even with the help of the code-first deep learning course at [fast.ai](https://www.fast.ai/), using GPT-2 was beyond me. It required ops knowledge I did not have to configure AWS instances and CS knowledge I did not have to tune countless parameters. I settled for reading [gwern's monthly newsletters](https://www.gwern.net/tags/newsletter) for updates and his work on deep learning, and waiting for the day that GPT-2 would be plug-and-play. That day is here.

I was browsing HN one day and came across [this thread](https://news.ycombinator.com/item?id=25883791) that mentioned a new GPT-2 library: [aitextgen](https://github.com/minimaxir/aitextgen). This is exactly what I was waiting for! (actually, _that day_ had arrived earlier and the author of `aitextgen` had written previous versions).

I decided my first project would be creating a Twitter bot that took Joe Biden's tweets as prompts and responded as Donald Trump. I didn't have any success with fine-tuning on a dataset of Trump's tweets, so I "included" all the information I needed in the prompt via [magic sauce](https://github.com/charlesjlee/trump_gpt2_bot/blob/main/tweet.py#L70). It took a lot of fiddling, but I'm satisfied with the final output: https://twitter.com/donaldtrumpbot5/with_replies

{{<fluid_lightbox_imgs
    "pure-u-1-1|/img/20210205-gpt2-twitter-bot.png|Screenshot of Twitter profile"
>}}

Source code here:
https://github.com/charlesjlee/trump_gpt2_bot