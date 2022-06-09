#!/usr/bin/env python
# coding: utf-8

# # Day 10: Elves Look, Elves Say
# 
# ## Part 1
# 
# Today, the Elves are playing a game called *look-and-say*. They take turns making sequences by reading aloud the previous sequence and using that reading as the next sequence. For example, ```211``` is read as "one two, two ones", which becomes ```1221``` (```1``` ```2```, ```2``` ```1```s).
# 
# Look-and-say sequences are generated iteratively, using the previous value as input for the next step. For each step, take the previous value, and replace each run of digits (like ```111```) with the number of digits (```3```) followed by the digit itself (```1```).
# 
# For example:
# 
# - ```1``` becomes ``11`` (1 copy of digit ```1```).
# - ```11``` becomes ```21``` (```2``` copies of digit ```1```).
# - ```21``` becomes ```1211``` (one ```2``` followed by one ```1```).
# - ```1211``` becomes ```111221``` (one ```1```, one ```2```, and two ```1```s).
# - ```111221``` becomes ```312211``` (three ```1```s, two ```2```s, and one ```1```).
# 
# Starting with the digits in your puzzle input, apply this process 40 times. What is the **length of the result**?

# In[9]:


def look_and_say(num, iters, verbose=True):
    
    if verbose:
        print(num)

    for i in range(iters):
        new_num = list()
        ctr = 1
        val = 0
        reps = 0
        for j in range(len(num)):
            if j != len(num)-1:
                if num[j] == num[j+1]:
                    ctr = ctr + 1
                    val = num[j]
                    reps = ctr

                elif num[j] != num[j+1]:
                    val = num[j]
                    reps = ctr
                    new_num.append(str(reps))
                    new_num.append(str(val))
                    ctr = 1
        
            else:
                val = num[j]
                reps = ctr
                new_num.append(str(reps))
                new_num.append(str(val))

        if verbose:
            print(new_num)

        num = new_num
    return len(num)


# In[10]:


num = ['1']
iters = 5

print("Example Length:", look_and_say(num, iters))


# In[11]:


num = open("day10_data.txt").readlines()
num = list(num[0])

iters = 40

print("Part 1 Length:", look_and_say(num, iters, False))


# In[12]:


num = open("day10_data.txt").readlines()
num = list(num[0])

iters = 50

print("Part 2 Length:", look_and_say(num, iters, False))


# In[15]:


get_ipython().system('jupyter nbconvert --to script day10.ipynb')

