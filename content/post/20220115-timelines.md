+++
title = "d3-milestones timeline library"
description = ""
tags = [
	"data visualization",
	"timeline",
    "Wikidata",
    "d3",
]
date = "2022-01-15"
categories = [
    "",
]
+++

While working on a d3 timeline for another post, I came across a beautiful timeline library, [d3-milestones](https://github.com/walterra/d3-milestones), and knew that I wanted to use it. I’ve also wanted to play with [WikiData](https://en.wikipedia.org/wiki/Wikidata) for a long time, so I combined these two interests by grabbing data from Wikidata and visualizing it using [d3-milestones](https://github.com/walterra/d3-milestones). There's another chart that I want to try out later in this post, so this first example will be straightforward: Stephen King novels by publication date.

After scrolling through [this tutorial](https://www.wikidata.org/wiki/Wikidata:SPARQL_tutorial), I was able to modify [this sample query](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/queries/examples#Books_by_a_given_Author_including_genres_and_year_of_first_publication) to get what I wanted:

```
SELECT DISTINCT
  ?book
  ?bookLabel
  ?authorLabel
  (GROUP_CONCAT(?genre_label; SEPARATOR = ", ") AS ?genres)
  (MIN(?publicationDate) AS ?firstPublication)
WHERE {
  ?author rdfs:label "Stephen King"@en.
  ?book wdt:P50 ?author.
  OPTIONAL {
    ?book wdt:P136 ?genre.
    ?genre rdfs:label ?genre_label.
    FILTER((LANG(?genre_label)) = "en")
  }
  ?book wdt:P7937 wd:Q8261;
    wdt:P577 ?publicationDate.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}
GROUP BY ?book ?bookLabel ?authorLabel
ORDER BY ?firstPublication
```
[(interactive link)](https://query.wikidata.org/#SELECT%20DISTINCT%0A%20%20%3Fbook%0A%20%20%3FbookLabel%0A%20%20%3FauthorLabel%0A%20%20%28GROUP_CONCAT%28%3Fgenre_label%3B%20SEPARATOR%20%3D%20%22%2C%20%22%29%20AS%20%3Fgenres%29%0A%20%20%28MIN%28%3FpublicationDate%29%20AS%20%3FfirstPublication%29%0AWHERE%20%7B%0A%20%20%3Fauthor%20rdfs%3Alabel%20%22Stephen%20King%22%40en.%0A%20%20%3Fbook%20wdt%3AP50%20%3Fauthor.%0A%20%20OPTIONAL%20%7B%0A%20%20%20%20%3Fbook%20wdt%3AP136%20%3Fgenre.%0A%20%20%20%20%3Fgenre%20rdfs%3Alabel%20%3Fgenre_label.%0A%20%20%20%20FILTER%28%28LANG%28%3Fgenre_label%29%29%20%3D%20%22en%22%29%0A%20%20%7D%0A%20%20%3Fbook%20wdt%3AP7937%20wd%3AQ8261%3B%0A%20%20%20%20wdt%3AP577%20%3FpublicationDate.%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22en%22.%20%7D%0A%7D%0AGROUP%20BY%20%3Fbook%20%3FbookLabel%20%3FauthorLabel%0AORDER%20BY%20%3FfirstPublication)

Cross-referencing the Wikidata query results with [Stephen King's novels bibliography on Wikipedia](https://en.wikipedia.org/wiki/Stephen_King_bibliography#Novels), I see several errors on the Wikidata side:
1. includes six additional entries for novellas
1. includes a short story collection (mis-categorization)
1. includes a duplicate Spanish title for an existing novel
1. is missing five novels that Wikipedia has
1. is missing three novels by Richard Bachman, King's pen name
1. has different publication dates for two novels

Most of these data issues can be addressed by modifying the query, but I'm lazy so we'll move on. Exporting, transforming, and feeding this data to [d3-milestones](https://github.com/walterra/d3-milestones) gives this nice chart:

{{<fluid_lightbox_imgs
    "pure-u-1-1|/img/20220115-timelines-stephen-king-timeline.png|Stephen King novels published timeline"
>}}
(raw version [here](/img/20220115-timelines-stephen-king-timeline.png))

I also learned that Wikidata offers _nice_ built-in and interactive visualizations. The view in the iframe below starts off narrow, but you can CTRL+SCROLL to zoom-in.
<iframe style="width: 100%; height: 70vh; border: none;" src="https://query.wikidata.org/embed.html#%23defaultView%3ATimeline%0ASELECT%20DISTINCT%0A%20%20%3Fbook%0A%20%20%3FbookLabel%0A%20%20%3FauthorLabel%0A%20%20%28GROUP_CONCAT%28%3Fgenre_label%3B%20SEPARATOR%20%3D%20%22%2C%20%22%29%20AS%20%3Fgenres%29%0A%20%20%28MIN%28%3FpublicationDate%29%20AS%20%3FfirstPublication%29%0AWHERE%20%7B%0A%20%20%3Fauthor%20rdfs%3Alabel%20%22Stephen%20King%22%40en.%0A%20%20%3Fbook%20wdt%3AP50%20%3Fauthor.%0A%20%20OPTIONAL%20%7B%0A%20%20%20%20%3Fbook%20wdt%3AP136%20%3Fgenre.%0A%20%20%20%20%3Fgenre%20rdfs%3Alabel%20%3Fgenre_label.%0A%20%20%20%20FILTER%28%28LANG%28%3Fgenre_label%29%29%20%3D%20%22en%22%29%0A%20%20%7D%0A%20%20%3Fbook%20wdt%3AP7937%20wd%3AQ8261%3B%0A%20%20%20%20wdt%3AP577%20%3FpublicationDate.%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22en%22.%20%7D%0A%7D%0AGROUP%20BY%20%3Fbook%20%3FbookLabel%20%3FauthorLabel%0AORDER%20BY%20%3FfirstPublication" referrerpolicy="origin" sandbox="allow-scripts allow-same-origin allow-popups" ></iframe>

---

Last year, [I manually created a timeline for the events in the book _Sandworm_](https://charlesjlee.com/post/20200707-sandworm-timeline/) by dragging and dropping in LibreOffice Draw. I was enamoured with the timeline style in the Economist and wanted to replicate it:
- first year is four digits and subsequent year are two digits
- color-coded events
- utilizing both sides of the timeline, i.e. top tracks events and bottom tracks milestones
- bending the event stems to create rectangular nooks for long text

This is what the final product looked like:
{{<fluid_lightbox_imgs
    "pure-u-1-1|/img/20220115-timelines-sandworm-timeline.svg|Sandworm timeline"
>}}
(raw version [here](/img/20220115-timelines-sandworm-timeline.svg))

And this is what the same data looks like using [d3-milestones](https://github.com/walterra/d3-milestones):
{{<fluid_lightbox_imgs
    "pure-u-1-1|/img/20220115-timelines-sandworm-timeline-d3-milestones.png|Sandworm timeline (d3-milestones)"
>}}
(raw version [here](/img/20220115-timelines-sandworm-timeline-d3-milestones.png))

*ouch*. Not too good. I should have suspected that all the text on the right side would get squished because [d3-milestones](https://github.com/walterra/d3-milestones) doesn't support elbow bends. 🤷
