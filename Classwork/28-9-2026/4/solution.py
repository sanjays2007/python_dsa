class Solution:
    def areAnagrams(self, s1, s2):


        freq1={}
        freq2={}
        for i in s1:
            freq1[i]=freq1.get(i,0)+1
        for j in s2:
            freq2[j]=freq2.get(j,0)+1
        return freq1==freq2