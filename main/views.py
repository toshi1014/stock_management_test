from django.shortcuts import render, redirect
from .models import Item
from django.utils import timezone
from django.utils.timezone import localtime
from .forms import ItemForm
from itertools import chain


def top(request):
    return render(request, "top.html", {})


def get_details(item):
    names = item.user.split("$#@#$")[1:-1]
    numbers = item.number.split("$#@#$")[1:-1]
    bo_dates = item.bo_date.split("$#@#$")[1:-1]
    b_or_n = item.back_or_not.split("$#@#$")[1:-1]
    re_dates = item.re_date.split("$#@#$")[1:-1]

    return names, numbers, bo_dates, b_or_n, re_dates


def nesting(items):
    mlists = []  ## add
    pm_c2 = []
    m_c2 = []

    elists = []
    pe_c2 = []
    e_c2 = []

    for i in items:  ## add
        if i.C1 == "MISUMI":  ## change name
            mlists.append(i)
        if i.C1 == "電気系":  ## change name
            elists.append(i)

    c1 = [
        ["MISUMI", pm_c2, m_c2, mlists],
        ["電気系", pe_c2, e_c2, elists]
    ]  ## add

    for c in c1:
        for m in c[3]:
            if not m.C2 in c[1]:
                c[1].append(m.C2)
                c[2].append([m.C2, []])
            for r in c[2]:
                if r[0] == m.C2:
                    r[1].append(m)

    return m_c2, e_c2


def lists(request):
    items = Item.objects.all()
    m_c2, e_c2 = nesting(items)

    return render(request, "lists.html", {"res" : [["MISUMI", m_c2], ["電気系", e_c2]]})       ## add


def item(request, pk):
    item = Item.objects.get(pk=pk)
    details = get_details(item)
    log = []
    for na, nu, d, b, r in zip(details[0], details[1], details[2], details[3], details[4]):
        log.append([d, nu, na, b, r])
    log = log[::-1]
    return render(request, "item.html", {"item" : item, "log" : log, "detail" : details})


def use(request, pk):
    item = Item.objects.get(pk=pk)
    name = request.GET.get("name")
    number = request.GET.get("number")
    if int(number) < item.stock:
        check = 1
    else:
        check = 0
    date = str(localtime(timezone.now()))[:19]

    if name and number and check:
        item.user = item.user + name + "$#@#$"
        item.number = item.number + number + "$#@#$"
        item.bo_date = item.bo_date + date + "$#@#$"
        item.back_or_not = item.back_or_not + "0$#@#$"
        item.re_date = item.re_date + "NONE$#@#$"
        item.stock = item.stock - int(number)
        item.using = item.using + int(number)
        item.save()

    return redirect("item", pk=pk)


def b_or_n(request, pk, date, number, b_or_n):
    box = []
    re_box = []
    check = 0
    item = Item.objects.get(pk=pk)
    details = get_details(item)
    for i, d in enumerate(details[2]):
        if d == date:
            break
    for idx, d in enumerate(details[3]):
        if idx == i:
            if b_or_n == "0":
                d = "1"
                check = 1
                item.stock = item.stock + int(number)
                item.using = item.using - int(number)
            else:
                d = "0"
                item.stock = item.stock - int(number)
                item.using = item.using + int(number)
        box.append(d)

    for idx, r in enumerate(details[4]):
        if idx == i:
            if check:
                re_date = str(localtime(timezone.now()))[:19]
                r = re_date
        if not r == "NONE":
            re_box.append(r)

    item.back_or_not = "hoge$#@#$" + ("$#@#$").join(box)+ "$#@#$"
    item.re_date = "hoge$#@#$" + ("$#@#$").join(re_box) + "$#@#$"
    item.save()
    return redirect("item", pk=pk)


def category(request, c2):
    items = Item.objects.all()
    m_c2, e_c2 = nesting(items)
    num_m, num_e = 1, 1
    if not c2 == "NONE":
        items = Item.objects.filter(C2__icontains=c2)
        m_c2, e_c2 = nesting(items)
        num_m = len(m_c2)
        num_e = len(e_c2)
    return render(request, "category.html", {
        "res": [["MISUMI", m_c2, num_m], ["電気系", e_c2, num_e]], "c2" : c2           ## add
    })


def new(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.stock = post.sum
            post.save()
            pk = post.id
            return redirect("item", pk=pk)
    else:
        form = ItemForm()

    return render(request, "new.html", {"form" : form})


def search(request):
    query = request.GET.get("query")
    if query:
        c1_box = Item.objects.filter(C1__icontains=query)
        c2_box = Item.objects.filter(C2__icontains=query)
        name_box = Item.objects.filter(name__icontains=query)

        ritems = list(chain(c1_box, c2_box, name_box))
        items = list(set(ritems))
        m_c2, e_c2 = nesting(items)                         ## add ↓
        num_m = len(m_c2)
        num_e = len(e_c2)
    else:
        return redirect("top")

    return render(request, "result.html", {
        "res": [["MISUMI", m_c2, num_m], ["電気系", e_c2, num_e]], "query" : query     ## add
    })