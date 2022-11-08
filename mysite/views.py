# from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

# Import forms
# from .forms import formInput
from .contactform import formInput

# Import model
from about.models import About
from news.models import News
from contact.models import contactData
from home.models import homePageModel

# To send mail
from django.core.mail import send_mail, EmailMultiAlternatives


def homepage(request):
    homepageData = homePageModel.objects.all()
    return render(request, 'index.html', {'homepageData': homepageData})


def about(request):
    aboutData = About.objects.all().order_by('-id')[:4]

    data = {
        'aboutData': aboutData
    }
    return render(request, 'about.html', data)

# def about(request):
#     if request.method=='GET':
#         data=request.GET.get('result')
#     return render(request, 'about.html',{'data':data})


def blog(request):
    return render(request, 'blog.html')


# def submitdata(request):
#     try:
#         if request.method == 'POST':
#             isEven = False
#             number = eval(request.POST['num'])
#             if (number % 2 == 0):
#                 isEven = True
#             return render(request, 'contact.html', {'isEven': isEven, 'number': number})
#     except:
#         isEven = "Invalid input!!!"


def marksheet(request):
    return render(request, 'marksheet.html')


def submitMarks(request):
    # Handling blank input
    if request.POST.get('math') == "":
        return render(request, "marksheet.html", {'error': True})
    elif request.POST.get('phy') == "":
        return render(request, "marksheet.html", {'error': True})
    elif request.POST.get('chem') == "":
        return render(request, "marksheet.html", {'error': True})
    elif request.POST.get('mp') == "":
        return render(request, "marksheet.html", {'error': True})
    elif request.POST.get('os') == "":
        return render(request, "marksheet.html", {'error': True})

    # Handling actual logic of program
    if request.method == 'POST':
        math = eval(request.POST.get('math'))
        phy = eval(request.POST.get('phy'))
        chem = eval(request.POST.get('chem'))
        mp = eval(request.POST.get('mp'))
        os = eval(request.POST.get('os'))

        total = (math+phy+chem+mp+os)

        avg = total/5

        percent = (total/750)*100

        grade = ''
        if percent >= 90:
            grade = 'O grade'
        elif 70 <= percent >= 90:
            grade = 'A grade'
        elif 50 <= percent >= 70:
            grade = 'B grade'
        elif 35 <= percent <= 50:
            grade = 'C grade'
        else:
            grade = 'Failed!!!'
        result = {
            'math': math,
            'phy': phy,
            'chem': chem,
            'mp': mp,
            'os': os,
            'total': total,
            'avg': avg,
            'percent': percent,
            'grade': grade
        }
        return render(request, 'marksheet.html', result)

# def contact(request):
#     data=[]
#     try:
#         if request.method == 'GET':
#             # email=request.GET.get('email')
#             # password=request.GET.get('password')
#             email = request.GET['email']
#             password = request.GET['password']
#             print(email, password)
#             data=[email,password]
#     except:
#         pass

#     return render(request, 'contact.html', {'data':data})


def contact(request):
    formField = formInput()
    dataMessage = False
    if request.method == 'POST':
        name = request.POST.get('name')
        contactNum = request.POST.get('contactNum')
        email = request.POST.get('email')
        message = request.POST.get('message')
        saveData = contactData(name=name, contactNum=contactNum,
                               email=email, message=message)
        saveData.save()
        dataMessage = True
        # Sending mail to myself
        send_mail(
            'New contact',
            '''
            Name: {} \n Contact number: {} \n email: {} \n message: {} \n
                '''.format(name, contactNum, email, message),
            '1abhigup6@gmail.com',
            ['abhishekguptacode@gmail.com'],
            fail_silently=False,
        )
        # Sending mail to user who has contact
        # send_mail(
        #     'Enquiry Unison',
        #     '''
        #         Thankyou so much for contacting us, Our team will review you request and will get back to you soon!!! \n
        #         Do not reply. This is an auto generated message
        #         ''',
        #     '1abhigup6@gmail.com',
        #     [email],
        #     fail_silently=False,
        # )

        subject = "Enquiry Unison"
        from_email = '1abhigup6@gmail.com'
        to = email
        msg = '''
        Thankyou so much for contacting us, Our team will review you request and will get back to you soon!!! \n
        <b>Do not reply.</b> This is an auto generated message
        '''
        msg = EmailMultiAlternatives(subject, msg,from_email , [to])
        msg.content_subtype = 'html'
        msg.send()
    data = {
        'formData': formField,
        'dataMessage': dataMessage
    }
    return render(request, 'contact.html', data)


# def contact(request):
#     data = {}
#     try:
#         if request.method == 'POST':
#             # email=request.GET.get('email')
#             # password=request.GET.get('password')
#             number = int(request.POST['number'])
#             fact = 1
#             if (number <= 0):
#                 fact = -1
#             else:
#                 for i in range(1, number+1):
#                     fact = fact*i
#                 url="/about/?result={}".format(fact)
#                 return HttpResponseRedirect(url)
    # return redirect(url) HttpResponseRedirect or redirect both can be used
#             print(fact)

#             data = {
#                 'fact': fact,
#                 'number': number
#             }
#     except:
#         pass

#     return render(request, 'contact.html', data)

# def courses(request):
#     return HttpResponse("Courses Page")


# def courseDetail(request, courseId):
#     return render(request, "/article_html/sample.html",courseId)


def news(request):
    newsData = News.objects.all()
    searchData = ''
    if request.method == 'POST':
        searchData = request.POST.get('searchData')
        if searchData != None:
            # __icontains is similar to like keyword in dbms
            newsData = News.objects.filter(news_title__icontains=searchData)
    data = {
        'newsData': newsData,
        'searchData': searchData
    }
    return render(request, 'news.html', data)


def newsUrl(request, newsSlug):
    newsData = News.objects.get(news_title_slug=newsSlug)
    data = {
        'newsData': newsData
    }
    return render(request, 'article_html/sample.html', data)
