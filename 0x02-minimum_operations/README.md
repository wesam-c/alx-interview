In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.
----------------------------------
The minOperations function calculates the minimum number of operations required to achieve exactly n occurrences of the character 'H' in a text editor, starting with a single 'H'. The two operations allowed are:

Copy All: Copy all the characters in the editor (this operation can be performed only when the current number of characters is a divisor of n).
Paste: Paste the copied characters (this can be done multiple times).
