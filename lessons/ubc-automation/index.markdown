---
layout: lesson
root: ../..
title: Automation
---

## Planning Notes
<ul>
  <li>If it has been covered yet, this lesson should include the transition from coding in ipython notebook to coding in an editor and running at the command line, or in the python or ipython interpreter</li>
  <li>Use requests library to replace manual CSV file downloading</li>
  <li>Use sys.argv to bring command line arguments into a script; mention argparse library for fancier tools</li>
  <li>Use a bash script to run the requests download script</li>
  <li>Introduce <code>at</code> and cron to run jobs in the future, and on a schedule</li>
  <li>Introduce looping and regular expressions in <code>bash</code> to process collections of files</li>
</ul>


## Learning Goals
{% include ubc-automation/goals.markdown %}


## Automation Notebooks

Create and switch to a new `automation` branch in your repo.
Create an `automation` directory and copy the `climate_data.py` file into it.
Start `ipython notebook` in your `automation` directory.

The notebooks we're going to work through are:

- [automation-0-requests](http://nbviewer.ipython.org/url/douglatornell.github.io/2013-09-26-ubc/lessons/ubc-automation/automation-0-requests.ipynb):
using the [requests library](http://docs.python-requests.org/) to get data from web sites


## References
{% include ubc-automation/references.markdown %}


[Back to Topics](../../index.html#topics)
