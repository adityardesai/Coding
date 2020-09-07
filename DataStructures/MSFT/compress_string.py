class Solution:
    def compress(self, chars: List[str]) -> int:
        
        n=len(chars)
        i=0
        index=0
        while i<n:
            j=i
            while j<n and chars[i] == chars[j]:
                j+=1
            chars[index]=chars[i]
            index+=1
            if j-i>1:
                count=str(j-i)
                for ch in count:
                    chars[index]=ch
                    index+=1
            i=j
        return index
