from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from . import std_extra
from myapp.models import Student, Semester, Result
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
# Create your views here.

def login_view(request):

    if request.method == 'POST' and 'login-btn' in request.POST:
        login_username = request.POST.get('username').lower()
        login_password = request.POST.get('password')
        
        if login_password=="" or login_username=="":
            messages.error(request,"Fill Username and Password!")
        else:
            user = authenticate(username = login_username, password = login_password)
            if user :
                if user.is_active:
                    login(request,user)
                    return redirect('profile')
                else:
                    messages.error(request,"This Id is Blocked!")
            else:
                messages.error(request,"Wrong username or password!")
    return render(request, 'login.html')

@login_required
def profile_view(request):
    check = False
    user = User.objects.get(username=request.user)
    if request.method == 'POST' and 'submit_btn' in request.POST:
        user.first_name =  request.POST.get('first_name').strip()
        user.last_name =  request.POST.get('last_name').strip()
        user.email = request.POST.get('email').strip().lower()
        check = True

    if request.POST.get('passcheck')=="on":
        user.set_password(request.POST.get('password'))
        login(request,user)
    
    user.save()
    
    if check:
        return redirect('profile')
    return render(request, 'profile.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def student_table(request):

    check = False

    student = Student.objects.all().order_by('-id')
    
    paginator = Paginator(student, 2)  # Show 10 obj per page

    page = request.GET.get('page')
    student = paginator.get_page(page)

    if request.method == 'POST' and 'btn-search' in request.POST:
        q = request.POST.get('search').strip()
        student = Student.objects.filter(Q(name__icontains = q) | Q(stid__icontains = q)).order_by('-id')
        check = True 

    context = {
        'student': student,
        'check' : check,
    }

    return render(request, 'student/student_table.html', context)

@login_required
def student_add(request):
   
    student = Student()

    if request.method == 'POST' and 'submit_btn' in request.POST:
        student.program = request.POST.get('program').strip()
        student.name = request.POST.get('name').strip()
        student.stid = request.POST.get('id').strip()
        student.enrollment = request.POST.get('enrollment').strip()
        student.batch = request.POST.get('batch').strip()
        student.email = request.POST.get('email').strip()
        student.mobile = request.POST.get('mobile').strip()
        student.gender = request.POST.get('gender').strip()
        student.blood = request.POST.get('blood').strip()
        # student.slug = Student.objects.get('id')
        student.date = request.POST.get('date').strip()
        if student.name is None or student.stid is None or student.enrollment == 'Choose...' or student.batch is None or student.email is None or student.mobile is None or student.gender == 'Choose...' or student.blood == 'Choose...' :
            messages.error(request, 'Fill up all fields!')
            # return redirect('student_add')
        else:
            if Student.objects.filter(stid=student.stid).exists():
                messages.error(request, 'Id already exixts...')
            else:
                student.save()
                return redirect('students')

    context = {
        'semester' : std_extra.semester,
        
        
    }
    return render(request, 'student/student_add.html', context)

@login_required
def add_result(request):

    result = Result()

    student = Student.objects.all().order_by('-id')
    semester = Semester.objects.all().order_by('-id')

    if request.method == 'POST' and 'btn-result' in request.POST:

        if  request.POST.get('stid') != 'Choose...' and request.POST.get('semester') != 'Choose...' and Result.objects.all().filter(studentId__iexact = request.POST.get('stid'), semester__iexact = request.POST.get('semester')).count() == 0:
            result.studentId = request.POST.get('stid')
            result.semester = request.POST.get('semester')

            if request.POST.get('course_one_title') != 'Choose...' and request.POST.get('course_one_code') != 'Choose...' and request.POST.get('course_one_credit') != 'Choose...' and  request.POST.get('course_one_number') is not None and request.POST.get('course_two_title') != 'Choose...' and request.POST.get('course_two_code') != 'Choose...' and request.POST.get('course_two_credit') != 'Choose...' and request.POST.get('course_two_number') is not None and request.POST.get('course_three_title') != 'Choose...' and request.POST.get('course_three_code') != 'Choose...' and request.POST.get('course_three_credit') != 'Choose...' and request.POST.get('course_three_number') is not None:

                result.Course_One_Title = request.POST.get('course_one_title')
                result.Course_One_Code = request.POST.get('course_one_code')
                result.Course_One_Credit = request.POST.get('course_one_credit')
                result.Course_One_TotalNum = request.POST.get('course_one_number')

                result.Course_Two_Title = request.POST.get('course_two_title')
                result.Course_Two_Code = request.POST.get('course_two_code')
                result.Course_Two_Credit = request.POST.get('course_two_credit')
                result.Course_Two_TotalNum = request.POST.get('course_two_number')

                result.Course_Three_Title = request.POST.get('course_three_title')
                result.Course_Three_Code = request.POST.get('course_three_code')
                result.Course_Three_Credit = request.POST.get('course_three_credit')
                result.Course_Three_TotalNum = request.POST.get('course_three_number')

                if request.POST.get('course_four_title') != 'Choose...' and request.POST.get('course_four_code') != 'Choose...' and request.POST.get('course_four_credit') != 'Choose...' and request.POST.get('course_four_number') is not None:
                 
                    result.Course_Four_Title = request.POST.get('course_four_title')
                    result.Course_Four_Code = request.POST.get('course_four_code')
                    result.Course_Four_Credit = request.POST.get('course_four_credit')
                    result.Course_Four_TotalNum = request.POST.get('course_four_number')

                    if request.POST.get('course_five_title') != 'Choose...' and request.POST.get('course_five_code') != 'Choose...' and request.POST.get('course_five_code') != 'Choose...' and request.POST.get('course_five_number') is not None:
                        result.Course_Five_Title = request.POST.get('course_five_title')
                        result.Course_Five_Code = request.POST.get('course_five_code')
                        result.Course_Five_Credit =request.POST.get('course_five_credit')
                        result.Course_Five_TotalNum = request.POST.get('course_five_number')

                        if request.POST.get('course_six_title') != 'Choose...' and request.POST.get('course_six_code') != 'Choose...' and request.POST.get('course_six_credit') != 'Choose...' and request.POST.get('course_six_number') is not None:
                            result.Course_Six_Title = request.POST.get('course_six_title')
                            result.Course_Six_Code = request.POST.get('course_six_code')
                            result.Course_Six_Credit = request.POST.get('course_six_credit')
                            result.Course_Six_TotalNum = request.POST.get('course_six_number')

                result.save()
                return redirect('result_table')

            else:
                return redirect('result_add')

        else:
            return redirect('result_add')
    


    context = {
        'course_title' : std_extra.course_title,
        'course_credit' : std_extra.course_credit,
        'course_code' : std_extra.course_code,

        'student' : student,
        'semester' : semester,

    }

    return render(request, 'result/add_result.html', context)

@login_required
def result_table(request):

    check = False

    result = Result.objects.all().order_by('-id')

    paginator = Paginator(result, 1)  # Show 10 obj per page

    page = request.GET.get('page')
    result = paginator.get_page(page)

    if request.method == 'POST' and 'btn-search' in request.POST:
        q = request.POST.get('search').strip()
        result = Result.objects.filter(Q(studentId__icontains = q)).order_by('-id')
        check = True 
    
    context = {
        'result': result,
        'check' : check,
    }



    return render(request, 'result/result_table.html', context)

@login_required
def add_semester(request):

    semester = Semester()

    if request.method == 'POST' and 'btn-semester' in request.POST:

        if Semester.objects.all().filter(Stsemester__iexact = request.POST.get('semester')).count() != 0:
            return redirect('semester')
        else:
            if request.POST.get('semester') == 'Choose...':
                pass
            else:
                semester.Stsemester = request.POST.get('semester')
                semester.save()
                return redirect('semester')

    context = {
        'enrollment' : std_extra.semester,
        'semester' : Semester.objects.all().order_by('-id')
    }

    return render(request, 'result/add_semester.html', context)


@login_required
def student_details(request, id):

    std_details = Student.objects.get(id = id)

    student = Student.objects.get(id = id)

    if request.method == 'POST' and 'submit_btn' in request.POST:
        student.program = request.POST.get('program').strip()
        student.name = request.POST.get('name').strip()
        # student.stid = request.POST.get('id').strip()
        student.enrollment = request.POST.get('enrollment').strip()
        # student.batch = request.POST.get('batch').strip()
        student.email = request.POST.get('email').strip()
        student.mobile = request.POST.get('mobile').strip()
        student.gender = request.POST.get('gender').strip()
        student.blood = request.POST.get('blood').strip()
        # student.slug = Student.objects.get('id')
        student.date = request.POST.get('date').strip()
        
        student.save()

        return redirect('students')
    
    context = {
        'std_details':std_details, 
        'semester' : std_extra.semester
    }

    return render(request, 'student/student_details.html' , context)

@login_required
def result_details(request, id):

    result = Result.objects.get(id = id)

    student = Student.objects.all().order_by('-id')
    semester = Semester.objects.all().order_by('-id')

    if request.method == 'POST' and 'btn-result' in request.POST:

        # if  request.POST.get('stid') != 'Choose...' and request.POST.get('semester') != 'Choose...':
        #     result.studentId = request.POST.get('stid')
        #     result.semester = request.POST.get('semester')

            if request.POST.get('course_one_title') != 'Choose...' and request.POST.get('course_one_code') != 'Choose...' and request.POST.get('course_one_credit') != 'Choose...' and  request.POST.get('course_one_number') is not None and request.POST.get('course_two_title') != 'Choose...' and request.POST.get('course_two_code') != 'Choose...' and request.POST.get('course_two_credit') != 'Choose...' and request.POST.get('course_two_number') is not None and request.POST.get('course_three_title') != 'Choose...' and request.POST.get('course_three_code') != 'Choose...' and request.POST.get('course_three_credit') != 'Choose...' and request.POST.get('course_three_number') is not None:

                result.Course_One_Title = request.POST.get('course_one_title')
                result.Course_One_Code = request.POST.get('course_one_code')
                result.Course_One_Credit = request.POST.get('course_one_credit')
                result.Course_One_TotalNum = request.POST.get('course_one_number')

                result.Course_Two_Title = request.POST.get('course_two_title')
                result.Course_Two_Code = request.POST.get('course_two_code')
                result.Course_Two_Credit = request.POST.get('course_two_credit')
                result.Course_Two_TotalNum = request.POST.get('course_two_number')

                result.Course_Three_Title = request.POST.get('course_three_title')
                result.Course_Three_Code = request.POST.get('course_three_code')
                result.Course_Three_Credit = request.POST.get('course_three_credit')
                result.Course_Three_TotalNum = request.POST.get('course_three_number')

                if request.POST.get('course_four_title') != 'Choose...' and request.POST.get('course_four_code') != 'Choose...' and request.POST.get('course_four_credit') != 'Choose...' and request.POST.get('course_four_number') is not None:
                 
                    result.Course_Four_Title = request.POST.get('course_four_title')
                    result.Course_Four_Code = request.POST.get('course_four_code')
                    result.Course_Four_Credit = request.POST.get('course_four_credit')
                    result.Course_Four_TotalNum = request.POST.get('course_four_number')

                    if request.POST.get('course_five_title') != 'Choose...' and request.POST.get('course_five_code') != 'Choose...' and request.POST.get('course_five_code') != 'Choose...' and request.POST.get('course_five_number') is not None:
                        result.Course_Five_Title = request.POST.get('course_five_title')
                        result.Course_Five_Code = request.POST.get('course_five_code')
                        result.Course_Five_Credit =request.POST.get('course_five_credit')
                        result.Course_Five_TotalNum = request.POST.get('course_five_number')

                        if request.POST.get('course_six_title') != 'Choose...' and request.POST.get('course_six_code') != 'Choose...' and request.POST.get('course_six_credit') != 'Choose...' and request.POST.get('course_six_number') is not None:
                            result.Course_Six_Title = request.POST.get('course_six_title')
                            result.Course_Six_Code = request.POST.get('course_six_code')
                            result.Course_Six_Credit = request.POST.get('course_six_credit')
                            result.Course_Six_TotalNum = request.POST.get('course_six_number')

                result.save()
                return redirect('result_table')

            else:
                return redirect('result_add')

        
    


    context = {
        'course_title' : std_extra.course_title,
        'course_credit' : std_extra.course_credit,
        'course_code' : std_extra.course_code,

        'student' : student,
        'semester' : semester,
        'result' : result,

    }

    return render(request, 'result/result_details.html', context)

def error_page(request):
    return render(request,'404.html')

def handler404(request,Exception):
    return render(request, '404.html', status=404)