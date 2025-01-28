class Solution:
    def is_anagram(self,str1, str2):
        if len(str1) != len(str2):
            return False
        
        for char in str1:
            if str1.count(char) != str2.count(char):
                return False
        return True
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = []
        i=0
        while i < len(strs):
            current = strs.pop(i)
            result.append([current])
            j=0
            while j <len(strs): 
                if self.is_anagram(current, strs[j]):
                    result[len(result)-1].append(strs.pop(j))
                    continue
                j+=1
                
        return result
