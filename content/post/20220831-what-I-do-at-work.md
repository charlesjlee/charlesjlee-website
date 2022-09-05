+++
title = "What I do at work"
description = ""
tags = [
  "data visualization",
  "timeline",
  "d3",
  "career",
]
date = "2022-08-31"
categories = [
    "",
]
+++

A few years ago, I participated in my high school’s career day. I talked about my work at a blockchain start-up and preached the gospel of Bitcoin. It felt like a waste of everyone's time because I don’t think the students understood what I was saying. How could they understand what it means to “improve API performance” when they don't understand what an API is? I was certainly lost when I was in their shoes and attended my career day. This series of posts tells the story of each of my jobs and explains concepts and situations so that people without prior experience can follow along.

I was inspired by this post on the Effective Altruism forums: [You should write about your job](https://forum.effectivealtruism.org/posts/nf72oiJddwDhoJ4QH/you-should-write-about-your-job) ([archive](https://web.archive.org/web/20211220170903/https://forum.effectivealtruism.org/posts/nf72oiJddwDhoJ4QH/you-should-write-about-your-job)). For anonymity and in [cryptographic tradition](https://en.wikipedia.org/wiki/Alice_and_Bob), each story uses the same names based on order of appearance: Alice, Bob, Carol, Dave, Erin, Frank, Grace, Heidi, Ivan, and Judy.

<script src="https://d3js.org/d3.v7.min.js"></script>
<script src="/js/d3-timeline/dist/d3-timelines.js"></script>

### Timeline view
_(hover for links)_
<!-- svg.scrollable is too tall at 150px and I don't know why, so I hard-coded height here -->
<div class="timeline" style="height:100px"></div>

### Table view
{{<pure_table
  "Company | Role | Dates worked | Link to Post"
  "GAL Inc | Web Developer Intern | July - Aug 2008 | <a href=/post/20220901-gal-inc/>link</a>"
  "LMI | Co-op | Jan - May 2010<br>Sep - Dec 2010 | <a href=/post/20220902-lmi/>link</a>"
  "JPMorgan Chase | Application Developer | July 2011 - Sept 2013 | <a href=/post/20220903-jpmorgan-chase/>link</a>"
  "Novantas | Database Developer | June 2014 - Aug 2016<br>Sept 2016 - March 2017 | <a href=/post/20220904-novantas/>link</a>"
  "Axoni | Software Developer | Dec 2017 - March 2020 | <a href=/post/20220905-axoni/>link</a>"
  "Amazon | Software Developer| Sept 2020 - now | <i>coming later</i>"
>}}

<script type="text/javascript">
    var data = [
      // GAL Inc: July-Aug 2008
      {
        name: "GAL Inc",
        times: [{"starting_time": 1214870400000, "ending_time": 1217548800000}],
        post: "/post/20220901-gal-inc/",
      },
      // LMI: Jan-May 2010, Sep-Dec 2010
      {
        name: "LMI",
        times: [
          {"starting_time": 1262304000000, "ending_time": 1272672000000},
          {"starting_time": 1283299200000, "ending_time": 1291161600000},
        ],
        post: "/post/20220902-lmi/",
      },
      // JPMC: July 2011 - Sept 2013
      {
        name: "JPMorgan Chase",
        times: [{"starting_time": 1309478400000, "ending_time": 1377993600000}],
        post: "/post/20220903-jpmorgan-chase/",
      },
      // Novantas: June 2014 - Aug 2016, Sept 2016 - March 2017
      {
        name: "Novantas",
        times: [
          {"starting_time": 1401580800000, "ending_time": 1470009600000},
          {"starting_time": 1472688000000, "ending_time": 1488326400000},
        ],
        post: "/post/20220904-novantas/",
      },
      // Axoni: Dec 2017 - March 2020
      {
        name: "Axoni",
        times: [{"starting_time": 1512086400000, "ending_time": 1583020800000}],
        post: "/post/20220905-axoni/",
      },
      // Amazon: Sept 2020
      {
        name: "Amazon",
        times: [{"starting_time": 1598918400000, "ending_time": Date.now()}],
        // post: "",
      },
    ];
    var width = '100%';
    var tooltip = d3.select("body")
      .append("div") 
      .attr("id", "tooltip")
      .style("opacity", 0)
      .style("position", "absolute")
      .style("text-align", "center")
      .style("width", "120px")
      .style("height", "40px")
      .style("padding", "2px")
      .style("font: 12px san",-"serif")
      .style("background", "lightsteelblue")
      .style("border", "0px")
      .style("border-radius", "8px");
    var chart = d3.timelines()
      .tickFormat({format: d3.timeFormat("%Y"), tickSize: 10})
      .mouseover(function (event, d) {
        tooltip
            .transition()
            .duration(200)
            .style("opacity", .9)
        tooltip
            .html([d.name, "<br><a href=\"", d.post, "\">", "(click for post)", "</a>"].join(""))
            .style("width", 8 * Math.max("(click for post)".length, d.name.length) + "px")
            .style("left", (event.pageX + 10) + "px")
            .style("top", (event.pageY - 15) + "px");
      })
      .mouseout(function (event, d) {
            tooltip
                .transition()
                .delay(1000)
                .duration(200)
                .style("opacity", 0);
      });
    var svg = d3.select(".timeline")
      .append("svg").attr("width", width)
      .datum(data).call(chart)
</script>
