# Regex help

This file is going to be a reference to future software developers that focus on regular expressions or Regex, which is an important part of our programing journey. There are going to be something when this topic come across and, it is essential for you as a junior developer to understand this subject. 

## Summary

what is Regex you might ask?1
This term is not just used in and specific programming language (java, python or C++), you can find a find this term in all the languages and is basically used to search for a specific pattern. If you are looking for this string with any special character lie a (! @#$%^&*) or a number, we can use a Regex to find it and replace it. Next, we are going to see some of the most important concepts in Regex.
![image](https://user-images.githubusercontent.com/34308684/184455047-6b768b7a-ebda-41ef-96cd-c5459c832f6f.png)

## Table of Contents

- [Anchors](#anchors)
- [Quantifiers](#quantifiers)
- [Grouping Constructs](#grouping-constructs)
- [Bracket Expressions](#bracket-expressions)
- [Character Classes](#character-classes)
- [The OR Operator](#the-or-operator)
- [Flags](#flags)
- [Character Escapes](#character-escapes)

## Regex Components

### Anchors

The anchors section is more used to create a starting point where our regex is going to begin and where can end. They basically do not match a character. 
They could use the following syntax: 
To start they use (^) this character. And to end ($):
Regex = ^Hola     “H” at the beginning of a line
Regex= Hola$      “a” at the end of the line


### Quantifiers

There are some quantifiers, but the must common that you will find are:
Quantity: Which is going to indicate how many characters you want to match, and you would express that with this symbol {n}. Example:
/\d{4}/ , The following code is written in python language:
 ![image](https://user-images.githubusercontent.com/34308684/184455119-09c725a8-92cf-441c-a9ab-cb9a6abf8103.png)

Output:

 ![image](https://user-images.githubusercontent.com/34308684/184455136-7b94e855-92b2-4a3a-ad2e-bddccfd78050.png)


### Grouping Constructs

This method consists of grouping a specific expression to match the needs of the user. We usually are going to see these in the following brackets [] and the Regex inside these brackets are will be evaluated.
Example: 
[a-z] or [A-Z] this indicate that we are looking for a character from a-z and A-Z.

Adding parentheses ( ) creates groups in the pattern. In this pattern, the area code and phone number are in separate groups. Example:

print('Pattern: .(\d\d\d)-(\d\d\d-\d\d\d\d)')

### Bracket Expressions

Now we are going to learn how to use the different bracket expressions in Regex:
[] = Indicate a set of the characters that we want to match. As we saw in the last example, it is used to determine the range of an alphabet or numbers.
Example:
 ![image](https://user-images.githubusercontent.com/34308684/184455216-57488d26-8713-43a6-9c0a-9caf2d7f83e6.png)

{} = The curly braces as we saw before it is used to specify a number of expression to match.
Example:
 ![image](https://user-images.githubusercontent.com/34308684/184455227-99ed3c46-f12d-4ae9-8182-730868d4698f.png)

() = This is especially useful for find-and-replace operations or any time you need to do something with part of the match.  
![image](https://user-images.githubusercontent.com/34308684/184455236-ec43ace8-5ed9-4cbd-b436-9bd71a6a16ff.png)

### Character Classes

The most important classes the you will see in Regex are:

\d		numeric digits 0 - 9
\D		NOT numeric digits
\w		letters, numbers, _
\W		any character NOT in \w
\s		space, tab, newline
\S		any character NOT in \s

Other Character:
^ 	caret			match from the beginning of the search
$ 	dollar sign		match at the end of the search
. 	dot wildcard		match any single character except newline
.*	dot star			match anything (zero or more characters) except newline

### The OR Operator

As you might know the OR operator is used as a logical condition to select one option or other, but always selecting at least one of them. Well, is the same for Regex. You can add different text option and separated them with the or operator, this is se symbol for OR  (|):
Example:  
![image](https://user-images.githubusercontent.com/34308684/184455246-16e8bf0e-9487-4190-a68e-b05385936918.png)


### Flags

The flags are going to affect the search of in our expression. The most common are: 
i =With this flag the search is case-insensitive
g= With this one the search looks for all matches.
s = this one allows a dot . to match newline character.
u = The flag correct processing of surrogate pairs. 
y =“Sticky” mode: searching at the exact position in the text.

![image](https://user-images.githubusercontent.com/34308684/184455255-05ba3d05-81d5-4dba-944c-b2e00bb6dc1c.png)

### Character Escapes

Imagine you wish to select a specific character from your regex, but that character is a dot.  But this is a part of the regex expressions. You can select that dot. Using (\) this backslash which is a escaping character. Example:

![image](https://user-images.githubusercontent.com/34308684/184455265-f32b698b-ad08-4249-bc82-4df03fb84b59.png)

## Author

Hey I'm Cris an Ecuadorian immigrant that came to United States to work with technology, I love front-end and work with teams. Never refused to play a good game.
This is my GitHub profile, where I keep working and developing new tools, apps, and more. Applying my Frond-end abilities, with html, CSS , JavaScript. Knowledge in Node.js and Mysql to built an efficient Back-end web page.
https://github.com/cr7st74n
