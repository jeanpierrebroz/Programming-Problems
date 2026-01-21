class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s)-1
        s_list = list(s)
        vowel_set = {'a', 'e', 'i', 'o', 'u'}

        print(s_list)

        while l < r:
            print(l, r)
            if s_list[l].lower() in vowel_set and s_list[r].lower() in vowel_set:
                s_list[l], s_list[r] = s_list[r], s_list[l]
                l+=1
                r-=1
                continue
            if s_list[l].lower() not in vowel_set:
                l+=1
            if s_list[r].lower() not in vowel_set:
                r-=1            

        return ''.join(s_list)