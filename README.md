![Banner Image](./markdown-image-files/PANDS_PROBLEM_SHEET.png)
---
---
![GitHub last commit](https://img.shields.io/github/last-commit/damienfarrell/pands-problem-sheet)
![GitHub contributors](https://img.shields.io/github/contributors/damienfarrell/pands-problem-sheet)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/damienfarrell/pands-problem-sheet)

# References
## Markdown 
1. [VS Code Markdown Tutorial](https://www.youtube.com/watch?v=Hgucu1ch3mo)
2. [Additional Markdown Tips](https://www.youtube.com/watch?v=a8CwpGARAsQ)
3. [Banner Creater](https://banner.godori.dev/)
4. [GitHub Metadata Badges](https://shields.io/)

## Topic 02 Task:
1. [Rounding Within A Formatted String](https://vlegalwaymayo.atu.ie/mod/forum/discuss.php?d=49560)

``` python
num = 3.14159
print(f"The value of pi is approximately {num:.2f}")
```

## Topic 03 Task:
1. [Replace First N Characters From A String In Python](https://thispointer.com/replace-first-n-characters-from-a-string-in-python/)


```python
strValue = 'Sample String'
n = 3
replacementStr = 'XXX'
# Replace First 3 characters in string with 'XXX'
strValue = replacementStr + strValue[n:]
print(strValue)
```

## Topic 05 Task:
1. [Basic Date And Time Types](https://docs.python.org/3/library/datetime.html)
2. [How To Get The Current Date and Time](https://www.programiz.com/python-programming/datetime/current-datetime)

``` python
from datetime import date

today = date.today()
print("Today's date:", today)
```

## Topic 06 Task:
1. [World's Fastest Square Root: Newton's Method](https://www.youtube.com/watch?v=FpOEx6zFf1o)
2. [Square Roots via Newton’s Method](https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf)
3. [Python math.isclose() Method](https://www.w3schools.com/python/ref_math_isclose.asp)

![Newton's Method](./markdown-image-files/Newton's%20Method.PNG)

## Topic 07 Task:
1. [Count The Number of Occurrences In A String](https://stackoverflow.com/questions/1155617/count-the-number-of-occurrences-of-a-character-in-a-string)
2. [How To Use sys.argv In Python With Examples](https://www.knowledgehut.com/blog/programming/sys-argv-python-examples)

## Topic 08 Task:
1. [Using The 'numpy.random.normal' Method](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html)
2. [Using The 'numpy.arange' Method](https://numpy.org/doc/stable/reference/generated/numpy.arange.html)
3. [Matplotlib Formatting](https://www.w3schools.com/python/matplotlib_pyplot.asp)
4. [Matplotlib.axes.Axes.twinx() in Python](https://www.geeksforgeeks.org/matplotlib-axes-axes-twinx-in-python/)
5. [Secondary axis with twinx(): how to add to legend?](https://stackoverflow.com/questions/5484922/secondary-axis-with-twinx-how-to-add-to-legend)