"""
https://leetcode.com/problems/read-n-characters-given-read4/solution/

Given a file and assume that you can only read the file using a given method read4, implement a method to read n characters.
Method read4:
The API read4 reads 4 consecutive characters from the file, then writes those characters into the buffer array buf.
The return value is the number of actual characters read.
Note that read4() has its own file pointer, much like FILE *fp in C.
Definition of read4:
    Parameter:  char[] buf4
    Returns:    int
Note: buf4[] is destination not source, the results from read4 will be copied to buf4[]
intialize the number of copied characters copiedChars = 0, and the number of read characters: readChars = 4. 
It's convenient initialize readChars to 4 and then use readChars != 4 as EOF marker.
Initialize an internal buffer of 4 characters: buf4.
While number of copied characters is less than N: copiedChars < n and there are still characters in the file: readChars == 4:
Read from file into internal buffer: readChars = read4(buf4).
Copy the characters from internal buffer buf4 into main buffer buf one by one. Increase copiedChars after each character. 
In the number of copied characters is equal to N: copiedChars == n, interrupt the copy process and return copiedChars.

TC:O(N)
SC:O(N)
"""

The read4 API is already defined for you.

    @param buf4, a list of characters
    @return an integer
    def read4(buf4):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf4 = [' '] * 4 # Create buffer with enough space to store characters
read4(buf4) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf4) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf4) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""

class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        copied_chars=0
        read_chars=4
        temp_buf=['']*4
        
        while copied_chars<n and read_chars==4:
            read_chars=read4(temp_buf)
            
            for i in range(read_chars):
                if copied_chars==n:
                    return copied_chars
                buf[copied_chars]=temp_buf[i]
                copied_chars+=1
        
        return copied_chars
        
