from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.template.defaultfilters import linebreaksbr
from django.template.defaultfilters import linebreaks
from .models import Blog, Profile, Sponsor, Events

# Create your views here.
#def index(request):
#  blogs = get_list_or_404(Blog)
#  return render(request, 'blog/index.html',{'blogs':blogs})
def home(request):
  title = "Home"
  return render(request, 'blog/index.html', {'title':title})

def about(request):
  title = "About"
  page_area = "page-area-wwd"
  return render(request, 'blog/whatwedo.html', {'title':title, 'page area':page_area})

def blogs(request):
  blogs = get_list_or_404(Blog)
  title = "Blogs"
  page_area = "page-area-ob"
  return render(request, 'blog/blogs.html', {'blogs':blogs,
    'title':title,
    'page_area':page_area
  })

def blog_post(request, blog_id):
  blog = get_object_or_404(Blog, pk=blog_id)
  blog_formatted = linebreaksbr(blog.blog_content)
  title = blog.blog_title
  page_area = "page-area-ob"
  return render(request, 'blog/blog_post.html', {'blog':blog, 'title':title, 'blog_formatted':blog_formatted, 'page_area':page_area})

def whatwedo(request):
  title = "What we do"
  page_area = "page-area-wwd"
  return render(request, 'blog/whatwedo.html', {'title':title,'page_area':page_area})
  
def ourteam(request):
  title = "Our team"
  profiles_2018 = get_list_or_404(Profile.objects.order_by('id'), year="2018")
  profiles_2019 = get_list_or_404(Profile.objects.order_by('id'), year="2019")
  profiles_2020 = get_list_or_404(Profile.objects.order_by('id'), year="2020")
  page_area = "page-area-ot"
  return render(request, 'blog/ourteam.html', {
'title':title, 
'profiles_2018':profiles_2018, 
'profiles_2019':profiles_2019, 
'profiles_2020':profiles_2020,
'page_area':page_area
})

def sponsors(request):
  title = "Sponsors"
  principal_sponsors = get_list_or_404(Sponsor, type_of_sponsor="Principal Sponsor")
  major_sponsors = get_list_or_404(Sponsor, type_of_sponsor="Major Sponsor")
  supporting_sponsors = get_list_or_404(Sponsor, type_of_sponsor="Supporting Sponsor")
  affiliated_with = get_list_or_404(Sponsor, type_of_sponsor="Affiliated With")
  page_area = "page-area-sponsors"
  return render(request, 'blog/sponsors.html', {
    'title':title, 
    'principal_sponsors':principal_sponsors,
    'major_sponsors':major_sponsors,
    'supporting_sponsors':supporting_sponsors,
    'affiliated_with':affiliated_with,
    'page_area':page_area
    })

def events(request):
  title = "Current Events"
  page_area = "page-area-ce"
  all_c_events = Events.objects.order_by('date').filter(current_or_past="CURRENT")  
  social_c_events = Events.objects.order_by('date').filter(current_or_past="CURRENT", portfolio="SOCIAL")  
  education_c_events= Events.objects.order_by('date').filter(current_or_past="CURRENT", portfolio="EDUCATION")  
  careers_c_events = Events.objects.order_by('date').filter(current_or_past="CURRENT", portfolio="CAREERS")  
  return render(request, 'blog/currentevents.html', {
    'title':title,
    'page_area':page_area,
    'all_c_events':all_c_events,
    'social_c_events': social_c_events,
    'education_c_events': education_c_events,
    'careers_c_events': careers_c_events
    })

def currentevents(request):
  title = "Current Events"
  page_area = "page-area-ce"
  all_c_events = Events.objects.order_by('date').filter(current_or_past="CURRENT")  
  social_c_events = Events.objects.order_by('date').filter(current_or_past="CURRENT", portfolio="SOCIAL")  
  education_c_events= Events.objects.order_by('date').filter(current_or_past="CURRENT", portfolio="EDUCATION")  
  careers_c_events = Events.objects.order_by('date').filter(current_or_past="CURRENT", portfolio="CAREERS")  
  return render(request, 'blog/currentevents.html', {
    'title':title,
    'page_area':page_area,
    'all_c_events':all_c_events,
    'social_c_events': social_c_events,
    'education_c_events': education_c_events,
    'careers_c_events': careers_c_events
    })

def pastevents(request):
  title = "Past Events"
  page_area = "page-area-pe"
  all_p_events = Events.objects.order_by('-date').filter(current_or_past="PAST")  
  social_p_events = Events.objects.order_by('-date').filter(current_or_past="PAST", portfolio="SOCIAL")  
  education_p_events= Events.objects.order_by('-date').filter(current_or_past="PAST", portfolio="EDUCATION")  
  careers_p_events = Events.objects.order_by('-date').filter(current_or_past="PAST", portfolio="CAREERS")  
  return render(request, 'blog/pastevents.html', {
    'title':title,
    'page_area':page_area,
    'all_p_events':all_p_events,
    'social_p_events': social_p_events,
    'education_p_events': education_p_events,
    'careers_p_events': careers_p_events
    })

def bitsamag(request):
  title = "Bitsa Mag"
  page_area = "page-area-bmag"
  return render(request, 'blog/bitsamag.html', {'title':title,'page_area':page_area})

def getinvolved(request):
  title = "Get Involved"
  page_area = "page-area-gi"
  return render(request, 'blog/getinvolved.html', {'title':title,'page_area':page_area})
