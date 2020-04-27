from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from main.models import Articles, ArticleTags, Policy
from django.template import loader
from django.views.generic.detail import DetailView
from django.utils import timezone
from .forms import ContactForm
from django.core.mail import send_mail
from HelloDjango import settings

def article_list(request):
    article_list = Articles.objects.all().order_by("-date")
    article_tags = ArticleTags.objects.all()
    form = ContactForm()
    return render(request, 'main/main.html', {'article_tags': article_tags, 'article_list': article_list, 'form': form})

def article_category(request, tag):
    article_list = Articles.objects.filter(tag__slug=tag).order_by("-date")
    article_tags = ArticleTags.objects.all()
    form = ContactForm()
    return render(request, 'main/main.html', {'article_tags': article_tags, 'article_list': article_list, 'form': form, 'tag': tag})

def article_detail(request, slug):
    article_detail = get_object_or_404(Articles, slug=slug)
    article_list = Articles.objects.exclude(slug=slug).order_by("-date")[:3]
    article_tags = ArticleTags.objects.all()
    form = ContactForm()
    return render(request, 'main/article_detail.html', {'article_tags': article_tags, 'article_detail': article_detail, 'article_list': article_list, 'form': form})

def policy(request):
    article_list = Articles.objects.all().order_by("-date")[:3]
    policy = Policy.objects.all()
    article_tags = ArticleTags.objects.all()
    form = ContactForm()
    return render(request, 'main/policy.html', {'article_tags': article_tags, 'article_list': article_list, 'form': form, 'policy': policy})

def send_contact(request):
    article_list = Articles.objects.order_by("-date")[:3]
    article_tags = ArticleTags.objects.all()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            email_subject = 'Заявка с сайта Блог Lightwork'
            email_body = "С сайта отправлено новое сообщение\n\n" \
                         "Имя отправителя: %s \n" \
                         "Телефон: %s \n" % \
                         (form.cleaned_data['name'],
                         form.cleaned_data['phone'])
            send_mail(email_subject, email_body, settings.EMAIL_HOST_USER, ['apollonseven@gmail.com'], fail_silently=False)
            form = ContactForm()
            return render(request, "main/thanks.html", {'article_tags': article_tags, 'article_list': article_list, 'form': form})
        else:
            form = ContactForm()
            return render(request, "main/thanks.html", {'article_tags': article_tags, 'article_list': article_list, 'form': form})
    else:
        form = ContactForm()
        return render(request, "main/main.html", {'article_tags': article_tags, 'article_list': article_list, 'form': form})
        
def thanks(request):
    article_list = Articles.objects.order_by("-date")[:3]
    article_tags = ArticleTags.objects.all()
    form = ContactForm()
    return render(request, 'main/thanks.html', {'article_tags': article_tags, 'article_list': article_list, 'form': form})

