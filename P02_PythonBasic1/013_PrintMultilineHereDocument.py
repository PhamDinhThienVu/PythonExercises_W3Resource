"""
Write a Python program to print the following 'here document'.

Sample string:
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example

a string that you "don't" have to escape                                                                      
This                                                                                                          
is a  ....... multi-line                                                                                      
heredoc string --------> example 


A here document (or "heredoc") is a way of specifying a text block, preserving the line breaks, indents, and other whitespace within the text. The said code uses triple quotes to define a multi-line string, also known as a heredoc string. It allows the string to span multiple lines without the need to escape newline characters.

The output will be the string exactly as it appears in the code, including the newline characters.

"""

print("""
a string that you "don't" have to escape
This
is a  ....... multi-line
heredoc string --------> example
""")