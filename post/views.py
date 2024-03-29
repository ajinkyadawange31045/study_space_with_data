# views.py
from django.shortcuts import render, get_object_or_404,HttpResponseRedirect,redirect
from .models import Branch, Semester, Course, Instructor,Instructor_post_pdf,Instructor_post_text,Course_post
from django.urls import reverse
from django.contrib.auth import logout
from .forms import ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render

def home(request):
    # branch = get_object_or_404(Branch, id=branch_id)
    branch = Branch.objects.all()
    user_count = User.objects.count()
    # print(branch)

    # contact form
    # contact form
    user_comment = None
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            user_comment = contact_form.save(commit=False)
            # user_comment.post = post
            user_comment.save()
            return HttpResponseRedirect('/')
    else:
        contact_form = ContactForm()

    context = {'branch':branch,'contact_form':contact_form,'user_count': user_count}
    return render(request,'post/home.html',context) 

def logout_views(request):
    logout(request)
    return redirect("/")

# @login_required
@login_required(login_url='/accounts/google/login/')
def semester(request, url):
    branch = Branch.objects.get(url=url)
    semesters = Semester.objects.filter(branch=branch)
    context = {
        'branch': branch,
        'semesters': semesters
    }
    return render(request, 'post/semester.html', context)


def course(request, url,branch_url,semester_url):
    branch = Branch.objects.get(url = branch_url)
    semester = Semester.objects.get(url = semester_url)
    course = get_object_or_404(Course, url=url)
    post_thing =Instructor.objects.filter(course=course)
    course_post = Course_post.objects.filter(course=course)
    context = {'branch':branch, 'course': course,'inc':post_thing,'course_post':course_post,'semester':semester}
    return render(request, 'post/course.html',context)

def instructor(request, url, branch_url,semester_url,course_url,course_taken_in_year):
    branch = Branch.objects.get(url = branch_url)
    semester = Semester.objects.get(url = semester_url)
    course = Course.objects.get(url = course_url)
    instructor = get_object_or_404(Instructor, url=url,id=course_taken_in_year)
    instructor_post_pdf1 = Instructor_post_pdf.objects.all().filter(instructor=instructor)
    instructor_post_text1 = Instructor_post_text.objects.all().filter(instructor=instructor)
    course_post = Course_post.objects.filter(course=course)
    context = {'instructor': instructor,'instructor_post_pdf1':instructor_post_pdf1,'instructor_post_text1':instructor_post_text1,'course':course,'branch':branch,'semester':semester,'course_post':course_post,}
    return render(request, 'post/instructor.html', context)

def instructor_post_pdf(request, pdf_url, branch_url,semester_url,course_url,instructor_url,course_taken_in_year):
    branch = Branch.objects.get(url = branch_url)
    semester = Semester.objects.get(url = semester_url)
    course = Course.objects.get(url = course_url)
    instructor = Instructor.objects.get(url=instructor_url,id=course_taken_in_year)
    instructor_post_pdf1 = get_object_or_404(Instructor_post_pdf, url=pdf_url)
    context = {'instructor_post_pdf1': instructor_post_pdf1,'course':course,'branch':branch,'semester':semester,'instructor':instructor}
    return render(request, 'post/instructor_post_pdf.html', context)

def instructor_post_text(request, post_url, branch_url,semester_url,course_url,instructor_url,course_taken_in_year):
    branch = Branch.objects.get(url = branch_url)
    semester = Semester.objects.get(url = semester_url)
    course = Course.objects.get(url = course_url)
    instructor = Instructor.objects.get(url=instructor_url,id=course_taken_in_year)
    instructor_post_text1 = get_object_or_404(Instructor_post_text, url=post_url)
    context = {'instructor_post_text1': instructor_post_text1,'course':course,'branch':branch,'semester':semester,'instructor':instructor}
    return render(request, 'post/instructor_post_text.html', context)

