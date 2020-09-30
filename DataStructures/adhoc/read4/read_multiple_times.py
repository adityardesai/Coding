"""
Given a file and assume that you can only read the file using a given method read4, implement a method read to read n characters. 
Your method read may be called multiple times.

Method read4:

The API read4 reads 4 consecutive characters from the file, then writes those characters into the buffer array buf.
The return value is the number of actual characters read.
Note that read4() has its own file pointer, much like FILE *fp in C.

Definition of read4:
    Parameter:  char[] buf4
    Returns:    int
    
Ref:https://happygirlzt.com/code/158.html
"""


# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.tmp_count=0
        self.tmp_ptr=0
        self.tmp_buf=['']*4
    
    def read(self, buf: List[str], n: int) -> int:
        total=0
        
        while total<n:
            if self.tmp_ptr==0:
                self.tmp_count=read4(self.tmp_buf)
        
            while total<n and self.tmp_ptr<self.tmp_count:
                buf[total]=self.tmp_buf[self.tmp_ptr]
                total+=1
                self.tmp_ptr+=1

            if self.tmp_count<4:
                break

            if self.tmp_ptr == self.tmp_count: 
                self.tmp_ptr=0
        
        return total
        
