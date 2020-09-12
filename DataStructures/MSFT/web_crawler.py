# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """
from collections import deque

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        if not startUrl:
            return []
        
        result=list()
        visited=set()
        
        visited.add(startUrl)
        queue=deque()
        queue.append(startUrl)
        result.append(startUrl)
        
        host=startUrl.split('http://')[1].split('/')[0]
        
        while queue:
            url=queue.popleft()
            children=htmlParser.getUrls(url)
            for child in children:
                child_host=child.split('http://')[1].split('/')[0]
                if child not in visited and child_host==host:
                    visited.add(child)
                    queue.append(child)
                    result.append(child)
        print(result)
        return result