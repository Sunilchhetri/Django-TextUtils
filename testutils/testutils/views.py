#I have created this file = sunil
from django.http import HttpResponse
from django.shortcuts import render
#code for video 7:
# def index(request):
#     return HttpResponse("Home")
def index(request):
    # parameter={ 'name':'sunil', 'place':'Baglung'}
    return render(request, 'index.html')
# def removepunc(request):
#     print(request.GET.get('text', 'default'))
#
#     return HttpResponse('''remove punc''')
#
# def capfirst(response):
#     return HttpResponse("capfirst")
#
# def newlineremove(request):
#     return HttpResponse("new line remove")
#
# def spaceremove(request):
#     return HttpResponse("space remove")

def ex1(request):
    s = '''<h1>Navigatin Bar</h1>
    <a href="https://www.youtube.com/">Youtube</a><br>
    <a href="https://www.facebook.com/">Facebook</a>'''

    return HttpResponse(s)

def analyze(request):
    djtext=request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc', 'off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')

    print(removepunc)
    print(djtext)
    if removepunc == "on":
        # analyzed= djtext
        punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if fullcaps == "on":
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params={'purpose': 'Changed to Upper case', 'analyzed_text':analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if(newlineremover=='on'):
        analyzed=""
        for char in djtext:
            if char != "\n" and char!='\r':
                analyzed=analyzed+char

        params={'purpose':'Removed new lines','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)
    if(extraspaceremover=="on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed+char

        params={'purpose':'removed extra spaces','analyzed_text':analyzed}

    if(removepunc!="on"and newlineremover!="on"and fullcaps!="on"and extraspaceremover!="on"):
        return HttpResponse("Please select any operation.Try again")# return render(request,'analyze.html',params)

    # elif(charcount=="on"):
    #     analyzed = len(djtext)
    #     params={'purpose':'count character','analyzed_text':analyzed}
    #     return render(request,'analyze.html',params)
    return render(request, 'analyze.html', params)


def AboutUs(request):
    return render(request, 'AboutUs.html')
