# IT5016 Assessment 3 Readme

The purpose of this GitHub Repository is to analyse this code and how various programming practices are applied, and why these practices are important for programming.

I have added various comments to the code to give my thoughts on how the code is structured and how it adheres to good programming practices.

Incorporating good programming practices into your code is important, since it improves your code's efficiency, as well as makes it easier to read, understand, and test.

I have listed various programming principles below:
<br/>  <br/>

The K.I.S.S. (Keep It Simple, Stupid) principle is essential to keep in mind when programming. It suggests that you should keep the program as simple as you can possibly make it, instead of using an overly complicated solution that would achieve the same result. This principle helps keep the code that you write easier to read and understand, making it easier to edit and test in the future.

Another important principle is D.R.Y. (Don't Repeat Yourself). It states that keep repeating code to a minimum. Having multiple blocks of the same code over and over makes the code harder to understand, and more difficult to test. If the same code is being used many times, it is better to use it as a function and call upon it when it is needed.

Two big programming principles are S.T.U.P.I.D. and S.O.L.I.D., with S.T.U.P.I.D. containing principles that you should avoid using while programming, while S.O.L.I.D. containing principles that are good to use while programming.

Let's start with the bad S.T.U.P.I.D. principles:

**S**ingleton: The Singleton Pattern is when you only have a single function or instance within a class. This is not necessarily a bad thing, and can be optimal in certain cases, but it can become a problem if becomes a habit and is used everywhere, including places where other methods would be more suitable.

**T**ight Coupling: When two or more functions or modules become so interconnected that making changes to one function requires editing another function, that is called Tight Coupling. This adds unnecessary complexity when you need to change a single function, as well as makes it harder to identify issues during testing.

**U**ntestability: Writing code that is hard to test is obviously bad. There can be many factors as to why it can be the case, but a big factor is tight coupling between modules. Writing code that is easier to test helps saves time during development that is better spent elsewhere.

**P**remature Optimisation: Even though optimisation is important, it is not a good idea to optimise early. It is better to write simple code early to ensure it works, and then optimise it later once everything is complete. Advanced optimised code is harder to understand and to test.

**I**ndescriptive Naming: A class, variable, function, or other object should be given a descriptive name so that the reader can easily understand what it is used for. A non-descriptive name ruins the readability of the object, and it is an easy practice to implement that makes a significant improvement.

**D**uplication: This is the same as the D.R.Y. principle. Do not write the same code repeatedly when it can easily be converted into a single function. It improves readability and ease of testing since you don't have to figure out which block of identical code is causing the problem. It also makes it easier to make changes to a single function than it is to change multiple blocks of code.
<br/>  <br/>

Now let's cover the good S.O.L.I.D. principles:

**S**ingle Responsibility Principle: This states that every class should have a single responsibility, and you should not add unnecessary functions outside the class's scope. Each class should have a defined responsibility, and adding extra unrelated functions to an existing class adds unnecessary confusion.

**O**pen/Closed Principle: Software entities should be open to extension, but closed to modification. This means that you should avoid modifying an existing module once it has been fully implemented, and instead you should create an extension to the module if you need a different variant. You should also write your code so that it is open to extension. Closing off modules for modification and instead creating a new extension is important, as modifying a working, existing module can cause bugs with other modules already interacting with it. Creating an extension instead helps avoid this issue.

**L**iskov Substitution Principle:

**I**nterface Segregation Principle: It is better to have separate specific interfaces than one general purpose interface. This is basically an extension of the Single Responsibility principle, but applied to interfaces. This way, each interface will have access to only the functionality that they need, instead of loading loads of functions that the specific interface will never use.

**D**ependency Inversion Principle: This states that abstractions should not depend on details, and details should depend on abstractions



