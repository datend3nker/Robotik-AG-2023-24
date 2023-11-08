**What Are Functions?**

In programming, functions are like little helpers that do tasks. They're like magic tricks you teach your computer. When you give your computer a task, the function says, "I'll do it for you!"

**How to Create a Function?**

To create a function in Python, follow these steps:

1. **Name the Function:** Give the function a name that describes what it will do. For example, if your function should say "Hello," you can name it `say_hello`.

2. **Write the Instructions:** Write what the function should do. For instance, if you want the function to say "Hello, World!" you write `print("Hello, World!")`.

3. **End the Function:** You can start the function with `def`, followed by the function name and parentheses where you can store possible information called "parameters." Then, use a colon (`:`) to start the instructions.

Here's an example of creating a simple function:

```python
def say_hello():
    print("Hello, World!")
```

**How Does a Function Work?**

A function is like a small command. When you want the function to do something, you call it. You say, "Hey function, please do this for me!" Here's how you call the function:

```python
say_hello()
```

When you run this command, the `say_hello` function starts, and it displays "Hello, World!" on the screen.

**Parameters and Return Values:**

Sometimes, the function wants specific information to work better. You can give this information to the function as "parameters." When the function is done, it can also give you an answer; that's called a "return value."

For example:

```python
def greet(name):
    print("Hello,", name)

def add(a, b):
    result = a + b
    return result
```

In the `greet` function, it expects a parameter called `name. When you call the function and give it a name, it uses that name to say "Hello, [Name]."

In the `add` function, we expect two parameters, `a` and `b`. It adds these numbers and returns the result.

**Conclusion:**

Functions in Python are like little helpers that do tasks. You create a function by giving it a name and telling it what to do. When you call the function, it completes the task for you. You can also add parameters to pass special information and use return values to get answers.

That's why functions are so useful in programming. They help us organize our code and make tasks easier to complete.

**Week 7 - Functions:**

**Task 1: Create a Simple Function**
In this task, we will learn how to create a function that displays something on the computer screen. A function is like a little helper that we call when we want to do something specific.

Create a function called `greet()`, which displays "Hello, World!" on the screen. It's like saying "Hello" to your computer, and it responds with "World!"

**Task 2: Function with Parameters**
Now, we want to tell our function what to display on the screen. This is called a "parameter." A parameter is like a message you give to the function so it knows what to do.

Create a function called `show_message(message)` that displays a message on the screen. The message you give will be passed as a parameter. Try giving different messages to the function and see what happens.

**Task 3: Function with a Return Value**
Sometimes, we don't just want the function to display something; we also want it to give us an answer. This is called a "return value." We give the function a task, and it gives us an answer.

Write a function called `add(number1, number2)` that adds two numbers and returns the result. You can call the function and print the result.

**Week 8 - Recursion:**

**Task 4: Simple Recursion**
Recursion is like a magic spell in programming. It means a function calls itself. In this task, we'll create a function that shows us numbers in reverse order.

Create a recursive function called `recursive_function(n)` that displays numbers from `n` to 1 on the screen. It's as if the function says, "Show me the numbers from `n` to 1," and then it does it by itself!

**Task 5: Calculate Factorial**
Factorial is like a math puzzle. It means we calculate the products of many numbers. In this task, we'll learn how to do that using recursion.

Write a recursive function `factorial(n)` that calculates the factorial of `n`. It's like asking, "How many ways are there to arrange `n` things in a specific order?" The function helps us answer this question.

**Task 6: Fibonacci Sequence**
The Fibonacci sequence is like a magical number series. It starts with the numbers 0 and 1, and each subsequent number in the series is the sum of the two previous numbers.

Create a recursive function `fibonacci(n)` that calculates the `n`-th element of the Fibonacci sequence. This means we want to know which magical Fibonacci number is at the `n`-th position. The function helps us figure that out.