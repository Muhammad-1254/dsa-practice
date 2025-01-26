class Solution:
    def cipher(self, text:str, mode:str)->str:
        encoded_str = ''
        shift = 3 if mode=='encode' else -3 
        for char in text:
            if char.isalpha():
                shift_base = 65 if char.isupper()else 97
                new_char = (ord(char)-shift_base+shift)%26
                encoded_str+=chr(new_char+shift_base)
            else:
                encoded_str+=char
        return encoded_str                        
    def encode(self, strs: list[str]) -> str:
        import json
        return json.dumps([self.cipher(i,'encode') for i in strs])
    def decode(self, s: str) -> list[str]:
        import json
        strs = json.loads(s)    
        return [self.cipher(i,'decode') for i in strs]          

