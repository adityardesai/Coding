# Python program to print all permutations with 
# duplicates allowed 
class Solution:

  def permute(self, a, result, temp_list): 
    if len(temp_list)==len(a): 
      result.append(''.join(list(temp_list)))
      return
    else: 
      for i in range(len(a)):
        if a[i] in temp_list:
          continue
        temp_list.append(a[i])
        self.permute(a, result, temp_list)
        temp_list.pop()

def main():
  s=Solution()
  string = "ABC"
  result=list()
  temp_list=list() 
  s.permute(list(string), result, temp_list)
  print(result)


main()
