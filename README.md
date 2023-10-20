# Timer Bar

A class to help you display progress for a discrete process

```python
|▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊▊---------------|
```

## Quick Start

Download the package:

**MacOS**:

```
pip install timer_bar
```

**Windows**:

```
py -m pip install timer_bar
```

Single, simple implementation:

```python
from timer_bar import TimerBar
import time

n = 10
timer_bar = TimerBar(n)

print('Initializing process...')
for i in range(n):
    print(timer_bar.text_at_step(i), end='\r')
    time.sleep(0.2) # represents process; expected after since print_after = False
print(timer_bar.text_at_step(n)) # because print_after = False, the last step should be printed 'manually'
print('Process complete!')
```

Mutliple processes (**only works in Jupyter notebook**):

```python
from timer_bar import TimerBar
from IPython.display import clear_output
import time

m = 4
n = 10

timer_bar_1 = TimerBar(
    steps = m,
    suffix_text=' tb #1'
)
timer_bar_2 = TimerBar(
    steps = n,
    suffix_text=' tb #2'
)

for i in range(m):
    for j in range(n):
        clear_output(wait=True)
        print(timer_bar_1.text_at_step(i))
        print(timer_bar_2.text_at_step(j))
        time.sleep(0.1)
clear_output(wait=True)

print(timer_bar_1.text_at_step(m))
print(timer_bar_2.text_at_step(n))
```

## In this README

- [Quick Start (above)](#quick-start)
- [Features](#features)
- [Usage](#usage)
  - [Initial Setup](#initial-setup)
  - [Implementation](#implementation)
  - [Modifications](#modifications)
    - [steps](#steps)
    - [total_length](#total_length)
    - [blank](#blank)
    - [filled](#filled)
    - [left_border](#left_border)
    - [right_border](#right_border)
    - [prefix_text](#prefix_text)
    - [suffix_text](#suffix_text)
    - [print_after](#print_after)

## Features

The TimerBar class creates an object that takes the number of steps in process as an input, and then for each step in the process will output a string that includes a bar filled to represent what percentage of the process is complete. This can be implemented in a python script using a line to create the object, and then a print line for each set in the process.

## Usage

### Initial Setup

The package **timer_bar** can be downloaded using pip or any other means of obtaining packages from PyPI

### Implementation

At the top of your file import the _TimerBar_ object from **timer_bar**:

```python
from timer_bar import TimerBar
```

You can then initialize the timer_bar object using the number of steps (**n** below) in the process as follows:

```python
timer_bar = TimerBar(n)
```

To then print the timer bar at a specific iteration (**i** below) do the following:

```python
print(timer_bar.text_at_step(i))
```

Various methods can be used to clear the console output depending on what platform you're using to run Python. Clearing the console will create for a better visual. The console can be cleared for IDLE and Jupyter Notebook as follows (these are examples, there are other ways of doing clearing the console, and clearing the console isn't required):

**IDLE** (only works for a single line timer bar)

```python
print(timer_bar.text_at_step(i), end='\r')
```

**Jupyter Notebook** (need to import `clear_output` from `IPython.display`)

```python
from IPython.display import clear_output
clear_output(wait=True)
print(timer_bar.text_at_step(i))
```

### Modifications

The following characteristics can be input when the object is initialized or updated later using the `update_attribute` method (or `prefix_update` or `suffix_update` for those specific attributes since they might be updated throughout your script's process). Do not attempt to change the attributes directly as this might throw off some of the dependency attributes of the object.

#### steps (int)

This is the number of steps of the process. For example if your process takes 4 steps to complete than you should input this value as 4. This is the only required value when initializing the object

#### total_length (int)

This is the total number of characters long that the actual bar of your timer bar will be (excluding prefix or suffix texts and borders). E.g., a value of 40 will produce 40 characters that will be proportionally blank or filled according to the progress of your process.

Default value: 50

#### blank (str)

This is the character that will be used to represent remaining progress in your process. This can be a single character or multiple characters. If it is multiple characters, the length of the progress bar will remain as `total_length`, the blank character will just fill the total length until that `total_length` is attained (e.g., a timer bar at the start of the process with `total_length = 9` and `blank = '<>'` would look like: `|<><><><><|`

Default value: '-'

#### filled (str)

This is the character that will be used to represent complete progress in your process. This can be a single character or multiple characters. If it is multiple characters, the length of the progress bar will remain as `total_length`, the filled character will just fill the total length until that `total_length` is attained (e.g., a timer bar at the end of the process with `total_length = 9` and `filled = '/\'` would look like: `|/\/\/\/\/|`

Default value: '▊'

#### left_border (str)

This is the character ths will be used as the left border of the timer bar. It can be a single character or multiple characters (e.g., a timer bar at the start of the process with `total_length = 9` and `left_border = '>>>'` would look like: `>>>---------|`)

Default value: '|'

#### right_border (str)

This is the character ths will be used as the right border of the timer bar. It can be a single character or multiple characters (e.g., a timer bar at the start of the process with `total_length = 9` and `right_border = '<<<'` would look like: `|---------<<<`)

Default value: '|'

#### prefix_text (str)

This is the text that will be displayed before the timer bar. If there is text that is short and stays a consistent length through the process that would add valueable context, adding it as the `prefix_text` and updating as the process continues works well (prefixes that shift in length cause the start of the timer bar to shift causing it to be more difficult to follow the progress). The `update_prefix` method can be used to update the `prefix_text`; it takes a string of the new prefix as an argument.

Default value: '' (blank)

#### suffix_text (str)

This is the text that will be displayed after the timer bar. Because this text won't shift the start of the bar, using the `suffix_text` to display dynamic information (e.g., '3/8 processed') is recommended over using the `prefix_text`. The `update_suffix` method can be used to update the `prefix_text`; it takes a string of the new prefix as an argument.

Default value: '' (blank)

#### print_after (bool)

This is used to determine whether the bar will be printed before (False) or after (True) action is taken (i.e., if printing before (`print_after=False`), then the `print(timer_bar.text_at_step(i))` should be used before a part of the process is ran; this means it will print with no progress showing before the first step (index = 0). Otherwise, if the timer bar is intended to print after the part of the process is ran (`print_after=True`), then the first step (index=0) will show some progress.

Default value: False
