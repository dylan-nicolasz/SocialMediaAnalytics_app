# Overview

{I created a Social Media Analytics application using Python and SQLite. The purpose of the software is to store and manage social media post information, including the platform, content, number of likes, comments, shares, and the date of the post.}

{The program integrates with a SQL relational database using Python's sqlite3 library. The application creates an SQLite database and a posts table where the social media information is stored. The program uses SQL commands such as INSERT, SELECT, UPDATE, and DELETE to add, retrieve, modify, and remove information from the database.

To use the program, the user interacts with a menu in the terminal. The user can add a new social media post, view existing posts, update information about a post, or delete a post. When updating a post, the user can choose which information they want to change, such as the platform, content, likes, comments, shares, or date.}

{My purpose for writing this software is to improve my understanding of how Python applications communicate with relational databases and how SQL can be integrated into a real software application. I also wanted to create something related to social media because analyzing information such as likes, comments, and shares can help identify trends and understand how content performs.}

{Provide a link to your YouTube demonstration. It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of how created the Relational Database.}

[Software Demo Video](https://www.loom.com/share/f9c313634a804f8ca175b89b5d014598)

# Relational Database

{I am using an SQLite relational database to store and manage the social media data for my application. The database allows my Python program to use SQL commands to add, retrieve, update, and delete information.}

{The database contains one table called posts. It has the following columns:

id – unique ID for each post.
platform – social media platform.
content – post content.
likes – number of likes.
comments – number of comments.
shares – number of shares.
post_date – date the post was created.}

# Development Environment

{I used Visual Studio Code to write and organize the software. I also used the SQLite database to store the social media data and the terminal to run and test the program.}

{I used Python as the programming language. I used Python's built-in sqlite3 library to connect the program to the SQLite database and execute SQL commands.}

# Useful Websites

- [Geek for geeks](https://www.geeksforgeeks.org/dbms/sql-server-crud-operations/)
- [W3 Schools](https://www.w3schools.com/python/ref_module_sqlite3.asp)

# Future Work

- Add more analytics and reports using aggregate functions.
- Add better input validation and error handling.
- Add charts to visualize social media performance.