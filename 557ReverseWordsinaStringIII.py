class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        vec = s.split(" ")
        new_line = ""
        num_words = len(vec)
        for i in range(num_words):
        	word = vec[i]
        	for j in range(len(word),0,-1):
	        	new_line += word[j]
	        if i != num_words-1:
		        new_line += " "
		return new_line