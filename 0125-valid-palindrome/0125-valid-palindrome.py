class Solution(object):
    def isPalindrome(self, s):
      s=s.lower()
      res=""
      for char in s:
          if char.isalpha() or char.isdigit():     
              res=res+char
      print(res)
      return res==res[::-1]       

     
        