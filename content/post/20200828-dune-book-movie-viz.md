+++
title = "Dune book vs movies data viz"
description = ""
tags = [
	"Dune",
    "data viz",
]
date = "2020-08-28"
categories = [
    "",
]
+++

In anticipation of the new movie interpretation of *Dune* -- "Science Fiction's Supreme Masterpiece" (says so [right on the cover](https://www.amazon.com/Dune-Frank-Herbert/dp/B004S7CF54)) -- coming out this December, I created a visualization to compare the book to the previous two movies: the [1984 version](https://en.wikipedia.org/wiki/Dune_(1984_film)) and [Frank Herbert's Dune](https://en.wikipedia.org/wiki/Frank_Herbert%27s_Dune), a 3-part mini-series broadcast in 2000.

## Dune (1984) review
To a fan looking for a fan-movie, 1984 *Dune* disappoints and feels dumbed-down. Part of the problem is the editing that brought the runtime from four hours down to two by using extensive voice-over narration, casually explaining secrets that characters originally never revealed (e.g. Reverend Mother Gaius explains the Water of Life and the Kwisatz Haderach to Paul), action without explanation (e.g. Stilgar immediately accepts and names Paul minutes after meeting him), and other forms of plot compression. However, even had I viewed the original pre-cut version so that forced editing wasn't an issue, the creators made many decisions that I found distasteful. Some decisions were probably relics of the times:
- heavy emphasis on terrible visual effects and action scenes, which [people actually praised](https://en.wikipedia.org/wiki/Dune_(1984_film)) when the movie was released
- gratuitous scenes of gore and violence
- a weak, helpless Jessica who gives no lessons or trainings to Paul, gives no advice to the Duke, and gets mansplained simple things by Paul
- physical "weirding modules" instead of Bene Gesserit training because the director didn't want to see ["Kung-fu on sand dunes"](https://www.denofgeek.com/movies/top-ten-screen-screams/)

Some decisions were probably an attempt to simplify the plot to make it more accessible:
- Harkonnens are gross, demonic creatures with pustules and who frequently go "AH HA HA HAHAHA!!!"
- Paul and Jessica use and distribute physical "weirding modules"
- a "forbidden area" of Arrakis that Paul obviously goes to
- Paul is excited about his powers and eager to "awaken the sleeper"
- an alternative explanation for the destruction of House Atreides: they have "weirding modules" and "weirding modules" are too strong

Wikipedia says that this movie has developed a cult following, but I can't see why any modern viewer would like this movie.

## Frank Herbert's Dune review
This mini-series, split into three parts, closely follows the book, also in three parts. There are numerous, minor plot changes (e.g. missing subplot of Jessica being the suspected traitor) with some major plot changes that bring Princess Irulan earlier and more prominently into the story. Just like in the books, the pacing is smooth and the plot advances primarily through conversations. The special effects, reminiscent of early computer games, are tastefully limited. I really enjoyed this series and am looking forward to seeing how it compares with the upcoming *Dune* movie.

## Viz methodology
I read the book and recorded the length and contents of each section, noting that in place of chapters, *Dune* uses epigraphs, or short quotations, to partition the text. I then watched both movies and analogously recorded the length and contents of each scene, which I defined as delimited by cuts. Finally, I matched book scenes and movie scenes in the rotated, Sankey-like chart you see below. My goal was to capture the pacing of and how faithfully each movie followed its source material, so scenes were matched even if their plot contents differed drastically.

{{<fluid_lightbox_imgs
    "pure-u-1-1|/img/20200828-dune-book-movie-viz-annotated.svg|Dune book vs movies scene matchings"
>}}

**Observations**
- this data representation makes
  - the 1984 movie seem more faithful than it actually is because the majority of scenes are matched and in the same order too, but the actual scene contents are grossly unfaithful
  - the 2000 mini-series seem less faithful than it actually is because of the large patches of non-matched scenes, but these scenes are actually mostly canon. These non-matched scenes depict action, sex, conversations, and other events that take place between scenes in the book.
- the eight non-matched scenes in the book's timeline cover minor character's stories: Yueh, Hawat, Gurney, Feyd-Rautha, Lady Fenring, and Jessica's betrayal subplot

## Source code
- [raw data in LibreOffice Calc](/files/20200828_dune_book_movie_viz_Dune_chapters.ods)
- [annotated viz](/img/20200828-dune-book-movie-viz-annotated.svg) with [source code](/files/20200828_dune_book_movie_viz_with_annotations.py)
- [un-annotated viz](/img/20200828-dune-book-movie-viz.svg) with [source code](/files/20200828_dune_book_movie_viz.py)