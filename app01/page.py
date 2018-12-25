class Pagination(object):

    def __init__(self, totcalCount, currentPage, perPageNum=20, maxPageNum=7):
        self.totcalCount = totcalCount
        try:
            v = int(currentPage)
            if v < 0:
                v = 1
            self.currentPage = v
        except Exception as e:
            self.currentPage = 1
        self.perPageNum = perPageNum
        self.maxPageNum = maxPageNum

    def start(self):

        return (self.currentPage - 1) * self.perPageNum

    def end(self):

        return self.currentPage * self.perPageNum

    @property
    def num_pages(self):
        a, b = divmod(self.totcalCount, self.perPageNum)
        if b == 0:
            return a
        return a + 1

    def pager_num_range(self):
        if self.num_pages < self.maxPageNum:
            return range(1, self.num_pages + 1)  # 总页数小于每页数目
        part = int(self.maxPageNum / 2)

        if self.currentPage <= part:
            return range(1, self.maxPageNum + 1)
        if (self.currentPage + part) > self.num_pages:
            return (self.num_pages - self.maxPageNum + 1, self.num_pages + 1)
        return range(self.currentPage - part, self.currentPage + part + 1)

    def page_str(self):
        page_list = []
        if self.currentPage == 1:
            prev = "<a href=#>上一页</a>"

            
        else:
            prev = "<a href = /index2?p=%s>上一页</a>" % (self.currentPage - 1)
        page_list.append(prev)
        for i in self.pager_num_range():
            temp = "<a href='/index2?p=%s'>%s</a>" % (i, i)
            page_list.append(temp)
        if self.currentPage == self.num_pages:
            nex = "<a href=#>下一页</a>"
        else:
            nex = "<a href ='/index2?p=%s'>下一页</a>" % (self.currentPage + 1)
        page_list.append(nex)
        return ' '.join(page_list)
