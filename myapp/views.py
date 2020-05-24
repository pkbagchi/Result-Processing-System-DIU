from django.shortcuts import render,redirect
from .models import Student, Result, Semester
from django.contrib import messages

stdquery = Student.objects.none() # Student Information
student_grade = []   # All Result information of Student like (grade, grade_point, credit, courseName, corseCode)
sel_semester = ''
grade_point = []
credit = []


def index(request):

    course_name = []
    course_code = []
    grade = []

    global grade_point
    global credit
    global stdquery
    global student_grade
    global sel_semester

    credit.clear()
    grade_point.clear()
    
    def result_analysis(result):
        if result >= 80 and result <= 100:
            return 'A+', 4.00
        elif  result < 80 and result >= 75:
            return 'A', 3.75
        elif  result < 74 and result >= 70:
            return 'A-', 3.50
        elif  result < 70 and result >= 65:
            return 'B+', 3.25
        elif  result < 65 and result >= 60:
            return 'B', 3.00
        elif  result < 60 and result >= 55:
            return 'B-', 2.75
        elif  result < 55 and result >= 50:
            return 'C+', 2.50
        elif  result < 50 and result >= 45:
            return 'C', 2.25
        elif  result < 45 and result >= 40:
            return 'D', 2.00
        elif  result < 40 and result >= 00:
            return 'F', 0.00
        else:
            return 'error', 0.00
            
        
   
    # Student id and Semester Query
    
    if 'selstudentid' in request.GET and 'selsemester' in request.GET:
        std_id = request.GET['selstudentid']
        selsem = request.GET['selsemester']
        studentid = std_id.strip()  

        if selsem == 'Select Semester':
            messages.warning(request, 'Please select your semester')
            return redirect('home')
        if len(studentid) < 9:
            messages.warning(request, 'Enter your Correct Id')
            return redirect('home')
        elif Student.objects.filter(stid=studentid).count() == 0:
            messages.warning(request, 'Student not found')
            return redirect('home')
        else:
            stdquery = Student.objects.all().filter(stid__exact = studentid)
            relquery = Result.objects.all().filter(studentId__exact = studentid, semester__exact = selsem) 
            sel_semester = selsem
            if Result.objects.all().filter(studentId__exact = studentid, semester__exact = selsem).count() == 0:
                messages.warning(request, 'Result not found')
                return redirect('home')
            else:
                for query in relquery:
                    grade.append(result_analysis(query.Course_One_TotalNum)[0])
                    grade_point.append(result_analysis(query.Course_One_TotalNum)[1])

                    grade.append(result_analysis(query.Course_Two_TotalNum)[0])
                    grade_point.append(result_analysis(query.Course_Two_TotalNum)[1])

                    grade.append(result_analysis(query.Course_Three_TotalNum)[0])
                    grade_point.append(result_analysis(query.Course_Three_TotalNum)[1])

                    if query.Course_Four_Title is not None:
                        grade.append(result_analysis(query.Course_Four_TotalNum)[0])
                        grade_point.append(result_analysis(query.Course_Four_TotalNum)[1])
                        
                    if query.Course_Five_Title is not None:
                        grade.append(result_analysis(query.Course_Five_TotalNum)[0])
                        grade_point.append(result_analysis(query.Course_Five_TotalNum)[1])
                        
                    if query.Course_Six_Title is not None:
                        grade.append(result_analysis(query.Course_Six_TotalNum)[0])
                        grade_point.append(result_analysis(query.Course_Six_TotalNum)[1])
                    
                for query in relquery:
                    credit.append(query.Course_One_Credit)
                    course_name.append(query.Course_One_Title)
                    course_code.append(query.Course_One_Code)

                    credit.append(query.Course_Two_Credit)
                    course_name.append(query.Course_Two_Title)
                    course_code.append(query.Course_Two_Code)

                    course_name.append(query.Course_Three_Title)
                    credit.append(query.Course_Three_Credit)
                    course_code.append(query.Course_Three_Code)

                    if query.Course_Four_Title is not None:
                        course_name.append(query.Course_Four_Title)
                        credit.append(query.Course_Four_Credit)
                        course_code.append(query.Course_Four_Code)

                    if query.Course_Five_Title is not None:
                        course_name.append(query.Course_Five_Title)
                        credit.append(query.Course_Five_Credit)
                        course_code.append(query.Course_Five_Code)
                        
                    if query.Course_Six_Title is not None:
                        course_name.append(query.Course_Six_Title)
                        credit.append(query.Course_Six_Credit)
                        course_code.append(query.Course_Six_Code)

                student_grade = zip(course_code, course_name, credit, grade, grade_point) 
                print(student_grade)
                return redirect('results')   
            
        

        
    
    resSem = Semester.objects.all()
    context = {
        'resSem' : resSem,
    }

    return render(request, 'index.html', context)

def results(request):
    
    count_credit = 0   # Count Student all Credit
    total_sgpa = 0.00
    sub_cgpa = 0.00

    for key in credit:
        count_credit += int(key)
    

    for i in range(len(grade_point)):
        sub_cgpa += float(grade_point[i]*float(credit[i]))
    
    total_sgpa = round(float(sub_cgpa/count_credit), 2)
    

    context = {
        'total_sgpa' : total_sgpa,
        'count_credit' : count_credit,
        'stdquery' : stdquery,
        'student_grade' : student_grade,
        'sel_semester' : sel_semester,

    }
   
    return render(request, 'result.html', context)


