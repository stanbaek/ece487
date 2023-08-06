# 🐍 Python Tutorial

```{note}
The only way to learn a new programming language is by writing programs in it. - Dennis Ritchie (inventor of C programming language)
```

## Running Python

### Running Python in Command Prompt (or Terminal for Mac)

Open Windows Terminal (or Terminal for Mac) and run `python` in Windows or `python3` in Mac. You can also use Terminal in VS Code.

```{image} ./figures/Terminal.png
:width: 540
:align: center
```
<br>

This will open the Python Shell. The Shell is where you can enter code and see the responses and output of code you have programmed into Python.  This is a kind of sandbox, where you're able to try out some simple code and processes. For example, in the Shell enter: `2+3`.  If you press enter, it will display the answer `5` on the next line. 

Try the following code in the Shell. 

```Python
2+3
"hello"+" world"
a = 2
print(a)
```

The Python Shell acts very much like a calculator since code is basically a series of mathematical interactions with the system.  Try the follownig code

```Python
2+2    # add two integers
2+2.0  # add an integer to a floating point number
2*3    # 2 times 3
2**2   # 2 squared
2**3   # 2 cubed
2**128 # Unlike C, integers in Python does not have a size limitation.    
2/3    # It returns 1 in C, but 0.6666666666666 in Pyton 
2/3.0  # Same as 2/3 in Python.
2//3   # modulo (remainder), same as 2%3 in C
4//3   # modulo (remainder), same as 4%3 in C
```

Now type `exit()` and hit `Enter` to leave the Python Shell.  You can also use `Ctrl+Z` to exti the Shell.

### Saving and Executing Your Code

While working in the Shell is perfectly fine for small code snippets, it is not desirable for longer program listings. In this section, we will save a code as a text file and execute it from Terminal. First, open a text editor such as notepad, notepad++, atom, sublime_text, etc.  Enter the following code

```Python
a = "Python"
b = "is"
c = "cool"
print(a,b,c)
print(a+b+c)
```

Save the file as `hello.py` and exit.  Execute the code with the following command in Terminal.  
```
python hello.py
```
