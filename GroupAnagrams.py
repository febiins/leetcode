class GroupAnagrams:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        g={}

        for words in strs:
            keys="".join(sorted(words))

            if keys not in g:
                g[keys]=[]
            g[keys].append(words)
        return list(g.values())            

        
