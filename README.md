# PowerPoint Time Referee
While giving a presentation, do you ever wonder if you are behind? Are you ahead? Do you need to talk slower? Do you need to talk faster? Even if you've rehearsed it a thousand times, you can't fully prepare for technical failures, questions, interruptions. At any point in a presentation, you should know immediately where you are in relation to the expected timings.

`PowerPoint Time Referee` lets you set the number of seconds per slide you want to spend and then automatically populates the notes on each slide with the timings so that while you're presenting, you can always see how much time you have left.

This allows you as the presenter to make real-time decisions when it comes to discussion, interruptions or questions to potentially spend more or less time on certain topics.

Typically you should know how much time you want to spend per slide--and with `PowerPoint Time Referee` that's all you need to do. In the Notes section of each slide, you simply have to add a single line with the number of seconds you want to spend on that slide ('##120' = 2 minutes). When you have a time on all the slides, just run `PowerPoint Time Referee` and it will update the Notes field on all slides with timings.

## Installing
`pip install powerpoint-time-referee`

## QuickStart
This is one of the easiest tools you'll ever use.

BACKUP YOUR POWERPOINT FILE BEFORE 

1. All you need to do is open your presentation and in the notes section for each slide, add a line that reads `##<number of seconds>`. In the screenshot below, we want to spend two minutes on `Section 2`, so the note reads `##120`. 

![](http://i.imgur.com/X2yCill.png)
2. After you've provided a number for each slide, run the referee:

	ppt-ref ./myfile.pptx

In an instant, the referee does a couple things:

1. Calculates how long the total presentation should be based on your timings
2. Adds two lines to each slide note:
	* **START OF SLIDE**: *The time that you should be starting this slide*
	* **REMAINING TIME**: *How much time is remaining, as of the start of this slide*

In this screenshot, the first two slides are planned to be 2 minutes, 30 seconds. So by the time you get to the third slide, you should be 2:30 into the presentation. And since the last slide is planned for two minutes, you have only two minutes left.  
![](http://i.imgur.com/DRduYVv.png)

## Additional Features
### Start Timing from Specific Time
Instead of starting the first slide from 00:00:00, you can pass in an actual time so that you can see the timings against actual time:

	ppt-ref ./myfile.pptx --start_time 11:00

This command will show all the times relative to starting at 11 a.m.

### Start Timing from Now
If you are literally just starting the presentation and want to quickly update the numbers based on the current time, you can do that as well.

	ppt-ref ./myfile.pptx --start_now

This command will show all the times relative to starting at this moment.