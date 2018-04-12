from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

# Create your views here.

user_list = []

for i in range(999):
    temp = {'name': 'root' + str(i), 'age': i}
    user_list.append(temp)


def index(request):
    per_page_count = 10
    current_page = request.GET.get('p')
    current_page = int(current_page)

    start = (current_page - 1) * per_page_count
    end = current_page * per_page_count
    data = user_list[start:end]
    if current_page <= 1:
        pre_pager = 1
    pre_pager = current_page - 1
    next_pager = current_page + 1
    return render(request, 'index.html', {'user_list': data, 'pre_pager': pre_pager, 'next_pager': next_pager})


class basePaginator(Paginator):
    def __init__(self, current_page, per_page_num, *args, **kwargs):
        self.current_page = int(current_page)
        self.per_page_num = int(per_page_num)

        super(basePaginator, self).__init__(*args, **kwargs)

    def pager_num_range(self):
        if self.num_pages < self.per_page_num:
            return range(1, self.num_pages + 1)  # 总页数小于每页数目
        part = int(self.per_page_num / 2)

        if self.current_page <= part:
            return range(1, self.per_page_num + 1)
        if (self.current_page + part) > self.num_pages:
            return (self.num_pages - self.per_page_num + 1, self.num_pages + 1)
        return range(self.current_page - part, self.current_page + part + 1)


def index1(request):
    current_page = request.GET.get('p')

    paginator = basePaginator(current_page, 11, user_list, 10)
    try:
        posts = paginator.page(current_page)
        # 全部数据
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'index1.html', {'posts': posts})


from app01.page import Pagination


def index2(request):
    current_page = request.GET.get('p')

    page_obj = Pagination(666, current_page)

    data_list = user_list[page_obj.start():page_obj.end()]
    return render(request, 'index2.html', {'data_list': data_list, 'page_obj': page_obj})
