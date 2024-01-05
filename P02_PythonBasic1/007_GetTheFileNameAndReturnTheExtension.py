"""

Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')



Write a Python program that accepts a filename from the user and prints the extension of the file.

Sample filename: abc.java

Python str.rsplit(sep=None, maxsplit=-1) function:

str.split(sep=None, maxsplit=-1)

Return a list of the words in the string, using sep as the delimiter string. If maxsplit is given, at most maxsplit splits are done (thus, the list will have at most maxsplit+1 elements). If maxsplit is not specified or -1, then there is no limit on the number of splits (all possible splits are made).

If sep is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings (for example, '1,,2'.split(',') returns ['1', '', '2']). The sep argument may consist of multiple characters (for example, '1<>2<>3'.split('<>') returns ['1', '2', '3']). Splitting an empty string with a specified separator returns [''].
If sep is not specified or is None, a different splitting algorithm is applied: runs of consecutive whitespace are regarded as a single separator, and the result will contain no empty strings at the start or end if the string has leading or trailing whitespace. Consequently, splitting an empty string or a string consisting of just whitespace with a None separator returns [].
For example, ' 1 2 3 '.split() returns ['1', '2', '3'], and ' 1 2 3 '.split(None, 1) returns ['1', '2 3 '].

The function returns a list of the words of a given string using a separator as the delimiter string.

If maxsplit is given, the list will have at most maxsplit+1 elements.
If maxsplit is not specified or -1, then there is no limit on the number of splits.
If sep is given, consecutive delimiters are not grouped together and are deemed to delimit empty strings.
The sep argument may consist of multiple characters.
Splitting an empty string with a specified separator returns [''].
Pictorial Presentation:
"""


#Get the fileName from user
inFileName = input("Enter the file name: ");

#Split fileName into 2 part, NAME and EXTENSION
detailsFileName = inFileName.split(".");
print("Details of file: ",detailsFileName);

#Return the ENTENSION, the last of list
extension = detailsFileName[-1];
print("Extension of file: " + extension);







