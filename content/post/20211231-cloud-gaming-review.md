+++
title = "Cloud gaming provider review"
description = ""
tags = [
	"cloud",
	"gaming",
]
date = "2021-12-31"
categories = [
    "",
]
+++

I first heard about [gaming-as-a-service aka cloud gaming](https://en.wikipedia.org/wiki/Cloud_gaming) (not to be confused with [games as a service aka GaaS](https://en.wikipedia.org/wiki/Games_as_a_service)) back in Wired magazine many years ago. The idea was new at the time and Wired talked about how the user experience was laggy and poor so I didn't give it much thought. Fast forward to today and lots of the screenshots I see in game reviews look incredible. I'm curious to see for myself what the latest games look like at max settings, but like most people, I don't have a computer that can play modern games nevermind play them at max settings. So, I decided to look at the three big PC cloud gaming providers: [Nvidia GeForce NOW](https://en.wikipedia.org/wiki/GeForce_Now), [Google Stadia](https://en.wikipedia.org/wiki/Google_Stadia), and [Amazon Luna](https://en.wikipedia.org/wiki/Amazon_Luna).

Some basic info about each service:
{{<pure_table
    "Service | Launch | Max resolution | Game model | Offers free tier | # games supported"
	"Nvidia GeForce NOW | public on Feb 4, 2020 | 4k | BYO games from Steam, Epic, etc  | yes | 1463"
	"Google Stadia | public on Nov 19, 2019 | 4k | buy games from Stadia store | yes | 266"
	"Amazon Luna | early access (US-only) on Oct 20, 2020 | 1080p | monthly subscriptions for access to games | no | 154"
>}}

## Nvidia GeForce NOW
Nvidia is the oldest contender of the three, with a previous cloud gaming offering ([Nvidia Grid](https://en.wikipedia.org/wiki/GeForce_Now)) dating back to 2013. Interestingly, even though subscription models were less prevalent back in 2013 compared to now, Nvidia's original offering was a subscription model and they discontinued that in favor of a BYOB game model. The current pricing scheme makes it clear that you are paying to rent a gaming server, and that the target users are serious gamers who know what "RTX ON" and "RTX 3080" mean and can appreciate the inside joke on why, out of all possible games, [Crysis](https://en.wikipedia.org/wiki/Crysis#Reception) is bundled with the paid tiers.

{{<fluid_lightbox_imgs
    "pure-u-1-1|/img/20211231-cloud-gaming-review-nvidia.png|Nvidia GeForce NOW pricing"
>}}

Since Nvidia offers both a free tier and free games, it is possible to use the service completely for free. This is not the case for Google Stadia, which offers a free tier but requires that you buy games from the Stadia store, and Amazon Luna, which requires that you purchase a monthly subscription to access games. There are 93 free games and they include all of today's and yesterday's popular multiplayer online games and MMORPG's. This is really neat because it means that even people with older laptops or only cellphones can play online games with their friends. I decided to try out a random free game (SkyForge) and my experience was very disappointing:

1. I register for an Nvidia account and choose to start a session in a Chrome browser instead of downloading the recommended desktop app
2. I choose SkyFordge and am placed in a queue with "229 gamers ahead of me". This dampens my enthusiasm a little bit and the tantalizing message "Priority members typically wait less than 30 seconds" dampens it further. The queue takes about 10 minutes
3. I'm presented with a lower resolution screen with a Steam login dialogue. This reminds me of RDP-ing into a remote machine and I feel like I'm at work. I don't want to feel that way
4. I'm unable to paste my Steam password and have to type 30 random characters. After logging in, I need to enter a security code because Steam does not recognize this strange computer I'm on
5. I finally see a page with Skyforge, but now I need to download the game. It's 3GB and takes about 2 minutes to finish downloading. Next I need to "update" the game and this will take 20 steps, which takes a total of 20 minutes
6. Finally, I'm ready to spend the remaining 30 minutes of my free tier session actually playing the game. I click "Play" and the screen de-maximizes and closes because it crashed? I click "Play" again, am re-queued for a free tier server, and give up

I was excited about Nvidia's approach of just offering game server rentals and allowing users to BYO games, but my experience above using the free tier was very unfun. I can understand now why Amazon Luna is [choosing to forego 4k support](https://www.amazon.com/luna/landing-page) in favor of improving the user experience. 

## Google Stadia
Google Stadia got off to a rough start: [efforts to develop content via Stadia Games failed](https://en.wikipedia.org/wiki/Google_Stadia#History_and_development) and [the beta release had mixed reviews regarding inconsistent performance and limited game selection](https://en.wikipedia.org/wiki/Google_Stadia#Reception). In recent years, Stadia has improved on both of these fronts. Stadia pivoted to [onboarding third-party games and developers](https://en.wikipedia.org/wiki/Google_Stadia#History_and_development) and now has many major games in its list of [266 titles](https://stadia.google.com/games).

In contrast with the platform-specific support provided by Nvidia and Amazon Luna, Stadia only requires the device to have an internet connection and Chromium support. This implies wide availability because Google Chrome is widely supported. Stadia is built on top of YouTube's streaming functionality and which allows it to offer [special features](https://en.wikipedia.org/wiki/Google_Stadia#Platform-exclusive_features) unavailable from other cloud gaming providers.

I had to read [Stadia's FAQ](https://stadia.google.com/) a few times before I understood their pricing model:
- Stadia is free but you have to buy games from the Stadia store to actually play anything
- Stadia Pro is $10/month and comes with three benefits
  - 4k resolution streams
  - periodic free games, only available to play if you are an active Pro member
  - discounts on purchasing games

The [Stadia Games webpage](https://stadia.google.com/games) advertises free trials without sign-up so I decided to try the [Control](https://en.wikipedia.org/wiki/Control_(video_game)) trial. After clicking "Play", I was asked to log into my Google account and then the game started! I was astonished at the lack of gimmicks. I got in 30 minutes of smooth gameplay, just as advertised, and finished feeling satisfied. There was even a nice 5 minute reminder before the trial ended. I was hesitant about Stadia's pricing model because it sounds like games purchased from the Stadia store are _only_ playable on Stadia, but I usually don't replay games anyway and the trial experience was so satisfying that I'm ready to become a customer.

{{<fluid_lightbox_imgs
    "pure-u-1-1|/img/20211231-cloud-gaming-review-stadia.png|Google Stadia trials"
>}}

## Amazon Luna
Amazon Luna is the newest player in the cloud gaming space. They are still in early access and only in the continental US. The pricing model is subscription-based and there are currently three choices:
- **luna+** - includes some big titles like Far Cry 6, Control, and Metro Exodus, but [selection is limited at 86 titles](https://en.wikipedia.org/wiki/List_of_Amazon_Luna_games)
- **Ubisoft+** - this is actually [a stand-alone subscription offered by Ubisoft](https://en.wikipedia.org/wiki/Ubisoft%2B) so this option is just an integration, and a partial one -- [only 28 games](https://www.amazon.com/b?ie=UTF8&node=21494096011) in the subscription are playable on Luna
- **family channel** - includes [40 games](https://amazonluna.blog/games-fb47b600e8ec)

**luna+** offers a 7-day free trial that I used to finish the [Control](https://en.wikipedia.org/wiki/Control_(video_game)) playthrough I started while trialing Google Stadia. I experienced lag a few times but they were usually preceded by slow Wifi warnings. The wait time for servers was just a few seconds. The $6/month **luna+** subscription is a great and temporary value. The plan is labeled "Early access price" so I expect this to eventually increase.

{{<fluid_lightbox_imgs
    "pure-u-1-1|/img/20211231-cloud-gaming-review-luna.png|Amazon Luna pricing"
>}}

## Conclusions
Neither Google Stadia nor Amazon Luna allowed me to change the display settings, so I wasn't able to accomplish my original goal of playing a game at max settings. To do that, I will need to give Nvidia another shot and use a paid plan.

As a casual on & off gamer, the pricing model and great user experience of both Stadia and Luna appealed to me. The next time I want to play a new PC game, I'll turn to one of these services, and it will be proably easy to choose which one because the game will probably only be supported on one of them.
