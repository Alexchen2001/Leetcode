import bisect
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        prefixStr = ""
        # sorts in lexicographical order
        products.sort()
        n = len(products)
        
        for ltr in searchWord:
            #appends prefix
            prefixStr += ltr
            # finds the index of where the occurence of the prefix Str o nthe left
            prefixMatchIdx = bisect_left(products, prefixStr)
            suggestion = []

            for i in range(prefixMatchIdx,min(prefixMatchIdx + 3, n)):
                if products[i].startswith(prefixStr):
                    suggestion.append(products[i])
                else:
                    break
                
            res.append(suggestion)
        return res