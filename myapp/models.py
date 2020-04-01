from django.db import models

# Create your models here.
class Student(models.Model):
    program = models.CharField(max_length=50, choices=[('B.Sc in Computer Science & Engineering', 'B.Sc in Computer Science & Engineering')])
    name = models.CharField(max_length=30)
    stid = models.CharField(max_length=12)
    enrollment = models.CharField(max_length=20, choices=[('Spring 2017', 'Spring 2017'), ('Summer 2017', 'Summer 2017'),
        ('Fall 2017', 'Fall 2017'), ('Spring 2018', 'Spring 2018'), ('Summer 2018', 'Summer 2018'),
        ('Fall 2018', 'Fall 2018'),('Spring 2019', 'Spring 2019'), ('Summer 2019', 'Summer 2019'),
        ('Fall 2019', 'Fall 2019'), ('Spring 2020', 'Spring 2020'), ('Summer 2020', 'Summer 2020'),
        ('Fall 2020', 'Fall 2020'), ('Spring 2021', 'Spring 2021'), ('Summer 2021', 'Summer 2021'), ('Fall 2021', 'Fall 2021')])
    batch = models.IntegerField()

    def __str__(self):
        return self.stid

class Semester(models.Model):
    Stsemester =models.CharField(max_length=50,  choices=[('Spring 2017', 'Spring 2017'), ('Summer 2017', 'Summer 2017'),
        ('Fall 2017', 'Fall 2017'), ('Spring 2018', 'Spring 2018'), ('Summer 2018', 'Summer 2018'),
        ('Fall 2018', 'Fall 2018'),('Spring 2019', 'Spring 2019'), ('Summer 2019', 'Summer 2019'),
        ('Fall 2019', 'Fall 2019'), ('Spring 2020', 'Spring 2020'), ('Summer 2020', 'Summer 2020'),
        ('Fall 2020', 'Fall 2020'), ('Spring 2021', 'Spring 2021'), ('Summer 2021', 'Summer 2021'), ('Fall 2021', 'Fall 2021')])

    def __str__(self):
        return self.Stsemester

class Result(models.Model):
    studentId = models.ForeignKey('Student', on_delete=models.CASCADE)
    semester = models.ForeignKey('Semester', on_delete=models.CASCADE)

    # Course1
    Course_One_Title = models.CharField(max_length=50, choices=[('Engineering Mathematics', 'Engineering Mathematics'), ('Digital Electronics', 'Digital Electronics'), ('Digital Electronics Lab', 'Digital Electronics Lab'),
        ('Object Oriented Programming', 'Object Oriented Programming'), ('Object Oriented Programming Lab', 'Object Oriented Programming Lab'), ('Bangladesh Studies', 'Bangladesh Studies'), 
        ('Algorithms', 'Algorithms'), ('Algorithms Lab', 'Algorithms Lab'), ('Statiscs and Probability', 'Statiscs and Probability'),('Electronic Devices and Circuits', 'Electronic Devices and Circuits'),
        ('Electronic Devices and Circuits Lab', 'Electronic Devices and Circuits Lab'), ('Microcessor and Assembly Language', 'Microcessor and Assembly Language'),
        ('Microcessor and Assembly Language Lab', 'Microcessor and Assembly Language Lab'), ('Data Communication', 'Data Communication'), ('Numerical Methods', 'Numerical Methods'),
        ('Introduction to Bio-Informatics', 'Introduction to Bio-Informatics'), ('Database Management System', 'Database Management System'), ('Database Management System Lab', 'Database Management System Lab'),
        ('Computer Networks', 'Computer Networks'), ('Computer Networks Lab', 'Computer Networks Lab'), ('Economics', 'Economics'), ('System Analysis Design', 'System Analysis Design'),
        ('Computer Architecture and Organization', 'Computer Architecture and Organization'), ('Operating System', 'Operating System'), ('Operating System Lab', 'Operating System Lab'), ('Art of Living', 'Art of Living'),
        ('Compiler Design', 'Compiler Design'), ('Compiler Design Lab', 'Compiler Design Lab'), ('Software Engineering', 'Software Engineering'), ('Wireless Programming', 'Wireless Programming'),
        ('Financial and managerial Accounting', 'Financial and managerial Accounting'), ('Artificial Intelligence', 'Artificial Intelligence'), ('Artificial Intelligence Lab', 'Artificial Intelligence Lab'), 
        ('Simulation and Modelling', 'Simulation and Modelling'), ('Simulation and Modelling Lab', 'Simulation and Modelling Lab'), ('Web Engineering', 'Web Engineering'), ('Web Engineering Lab', 'Web Engineering Lab'),
        ('Computer Graphics', 'Computer Graphics'), ('Computer Graphics Lab', 'Computer Graphics Lab'), ('Embedded Systems', 'Embedded Systems')]
)

    Course_One_Code = models.CharField(max_length=50,choices=[('MAT211', 'MAT211'), ('CSE212', 'CSE212'), ('CSE213', 'CSE213'), ('CSE214', 'CSE214'), ('GED201', 'GED201'), ('CSE221', 'CSE221'), ('CSE222', 'CSE222'), ('STA133', 'STA133'),
        ('CSE224', 'CSE224'), ('CSE225', 'CSE225'), ('CSE231', 'CSE231'), ('CSE232', 'CSE232'), ('CSE233', 'CSE233'), ('CSE234', 'CSE234'), ('CSE235', 'CSE235'), 
        ('CSE311', 'CSE311'), ('CSE312', 'CSE312'), ('CSE313', 'CSE313'), ('CSE314', 'CSE314'), ('ECO314', 'ECO314'), ('CSE321', 'CSE321'), ('CSE322', 'CSE322'), 
        ('CSE323', 'CSE323'), ('CSE324', 'CSE324'), ('GED321', 'GED321'), ('CSE331', 'CSE331'), ('CSE332', 'CSE332'), ('CSE333', 'CSE333'), ('CSE334', 'CSE334'), 
        ('ACT301', 'ATC301'), ('CSE412', 'CSE412'), ('CSE413', 'CSE413'), ('CSE414', 'CSE414'), ('CSE415', 'CSE415'), ('CSE416', 'CSE416'), ('CSE417', 'CSE417'), ('CSE418', 'CSE418')
        , ('CSE421', 'CSE421'), ('CSE422', 'CSE422'), ('CSE423', 'CSE423')])
    Course_One_Credit = models.CharField(max_length=5, choices= [('1', '1'), ('2', '2'), ('3', '3')])
    Course_One_TotalNum = models.IntegerField()

    # Course2
    Course_Two_Title = models.CharField(max_length=50, choices=[('Engineering Mathematics', 'Engineering Mathematics'), ('Digital Electronics', 'Digital Electronics'), ('Digital Electronics Lab', 'Digital Electronics Lab'),
        ('Object Oriented Programming', 'Object Oriented Programming'), ('Object Oriented Programming Lab', 'Object Oriented Programming Lab'), ('Bangladesh Studies', 'Bangladesh Studies'), 
        ('Algorithms', 'Algorithms'), ('Algorithms Lab', 'Algorithms Lab'), ('Statiscs and Probability', 'Statiscs and Probability'),('Electronic Devices and Circuits', 'Electronic Devices and Circuits'),
        ('Electronic Devices and Circuits Lab', 'Electronic Devices and Circuits Lab'), ('Microcessor and Assembly Language', 'Microcessor and Assembly Language'),
        ('Microcessor and Assembly Language Lab', 'Microcessor and Assembly Language Lab'), ('Data Communication', 'Data Communication'), ('Numerical Methods', 'Numerical Methods'),
        ('Introduction to Bio-Informatics', 'Introduction to Bio-Informatics'), ('Database Management System', 'Database Management System'), ('Database Management System Lab', 'Database Management System Lab'),
        ('Computer Networks', 'Computer Networks'), ('Computer Networks Lab', 'Computer Networks Lab'), ('Economics', 'Economics'), ('System Analysis Design', 'System Analysis Design'),
        ('Computer Architecture and Organization', 'Computer Architecture and Organization'), ('Operating System', 'Operating System'), ('Operating System Lab', 'Operating System Lab'), ('Art of Living', 'Art of Living'),
        ('Compiler Design', 'Compiler Design'), ('Compiler Design Lab', 'Compiler Design Lab'), ('Software Engineering', 'Software Engineering'), ('Wireless Programming', 'Wireless Programming'),
        ('Financial and managerial Accounting', 'Financial and managerial Accounting'), ('Artificial Intelligence', 'Artificial Intelligence'), ('Artificial Intelligence Lab', 'Artificial Intelligence Lab'), 
        ('Simulation and Modelling', 'Simulation and Modelling'), ('Simulation and Modelling Lab', 'Simulation and Modelling Lab'), ('Web Engineering', 'Web Engineering'), ('Web Engineering Lab', 'Web Engineering Lab'),
        ('Computer Graphics', 'Computer Graphics'), ('Computer Graphics Lab', 'Computer Graphics Lab'), ('Embedded Systems', 'Embedded Systems')])
    Course_Two_Code = models.CharField(max_length=50, choices=[('MAT211', 'MAT211'), ('CSE212', 'CSE212'), ('CSE213', 'CSE213'), ('CSE214', 'CSE214'), ('GED201', 'GED201'), ('CSE221', 'CSE221'), ('CSE222', 'CSE222'), ('STA133', 'STA133'),
        ('CSE224', 'CSE224'), ('CSE225', 'CSE225'), ('CSE231', 'CSE231'), ('CSE232', 'CSE232'), ('CSE233', 'CSE233'), ('CSE234', 'CSE234'), ('CSE235', 'CSE235'), 
        ('CSE311', 'CSE311'), ('CSE312', 'CSE312'), ('CSE313', 'CSE313'), ('CSE314', 'CSE314'), ('ECO314', 'ECO314'), ('CSE321', 'CSE321'), ('CSE322', 'CSE322'), 
        ('CSE323', 'CSE323'), ('CSE324', 'CSE324'), ('GED321', 'GED321'), ('CSE331', 'CSE331'), ('CSE332', 'CSE332'), ('CSE333', 'CSE333'), ('CSE334', 'CSE334'), 
        ('ACT301', 'ATC301'), ('CSE412', 'CSE412'), ('CSE413', 'CSE413'), ('CSE414', 'CSE414'), ('CSE415', 'CSE415'), ('CSE416', 'CSE416'), ('CSE417', 'CSE417'), ('CSE418', 'CSE418')
        , ('CSE421', 'CSE421'), ('CSE422', 'CSE422'), ('CSE423', 'CSE423')])
    Course_Two_Credit = models.CharField(max_length=5, choices= [('1', '1'), ('2', '2'), ('3', '3')])
    Course_Two_TotalNum = models.IntegerField()

    # Course3
    Course_Three_Title = models.CharField(max_length=50, choices=[('Engineering Mathematics', 'Engineering Mathematics'), ('Digital Electronics', 'Digital Electronics'), ('Digital Electronics Lab', 'Digital Electronics Lab'),
        ('Object Oriented Programming', 'Object Oriented Programming'), ('Object Oriented Programming Lab', 'Object Oriented Programming Lab'), ('Bangladesh Studies', 'Bangladesh Studies'), 
        ('Algorithms', 'Algorithms'), ('Algorithms Lab', 'Algorithms Lab'), ('Statiscs and Probability', 'Statiscs and Probability'),('Electronic Devices and Circuits', 'Electronic Devices and Circuits'),
        ('Electronic Devices and Circuits Lab', 'Electronic Devices and Circuits Lab'), ('Microcessor and Assembly Language', 'Microcessor and Assembly Language'),
        ('Microcessor and Assembly Language Lab', 'Microcessor and Assembly Language Lab'), ('Data Communication', 'Data Communication'), ('Numerical Methods', 'Numerical Methods'),
        ('Introduction to Bio-Informatics', 'Introduction to Bio-Informatics'), ('Database Management System', 'Database Management System'), ('Database Management System Lab', 'Database Management System Lab'),
        ('Computer Networks', 'Computer Networks'), ('Computer Networks Lab', 'Computer Networks Lab'), ('Economics', 'Economics'), ('System Analysis Design', 'System Analysis Design'),
        ('Computer Architecture and Organization', 'Computer Architecture and Organization'), ('Operating System', 'Operating System'), ('Operating System Lab', 'Operating System Lab'), ('Art of Living', 'Art of Living'),
        ('Compiler Design', 'Compiler Design'), ('Compiler Design Lab', 'Compiler Design Lab'), ('Software Engineering', 'Software Engineering'), ('Wireless Programming', 'Wireless Programming'),
        ('Financial and managerial Accounting', 'Financial and managerial Accounting'), ('Artificial Intelligence', 'Artificial Intelligence'), ('Artificial Intelligence Lab', 'Artificial Intelligence Lab'), 
        ('Simulation and Modelling', 'Simulation and Modelling'), ('Simulation and Modelling Lab', 'Simulation and Modelling Lab'), ('Web Engineering', 'Web Engineering'), ('Web Engineering Lab', 'Web Engineering Lab'),
        ('Computer Graphics', 'Computer Graphics'), ('Computer Graphics Lab', 'Computer Graphics Lab'), ('Embedded Systems', 'Embedded Systems')])
    Course_Three_Code = models.CharField(max_length=50, choices=[('MAT211', 'MAT211'), ('CSE212', 'CSE212'), ('CSE213', 'CSE213'), ('CSE214', 'CSE214'), ('GED201', 'GED201'), ('CSE221', 'CSE221'), ('CSE222', 'CSE222'), ('STA133', 'STA133'),
        ('CSE224', 'CSE224'), ('CSE225', 'CSE225'), ('CSE231', 'CSE231'), ('CSE232', 'CSE232'), ('CSE233', 'CSE233'), ('CSE234', 'CSE234'), ('CSE235', 'CSE235'), 
        ('CSE311', 'CSE311'), ('CSE312', 'CSE312'), ('CSE313', 'CSE313'), ('CSE314', 'CSE314'), ('ECO314', 'ECO314'), ('CSE321', 'CSE321'), ('CSE322', 'CSE322'), 
        ('CSE323', 'CSE323'), ('CSE324', 'CSE324'), ('GED321', 'GED321'), ('CSE331', 'CSE331'), ('CSE332', 'CSE332'), ('CSE333', 'CSE333'), ('CSE334', 'CSE334'), 
        ('ACT301', 'ATC301'), ('CSE412', 'CSE412'), ('CSE413', 'CSE413'), ('CSE414', 'CSE414'), ('CSE415', 'CSE415'), ('CSE416', 'CSE416'), ('CSE417', 'CSE417'), ('CSE418', 'CSE418')
        , ('CSE421', 'CSE421'), ('CSE422', 'CSE422'), ('CSE423', 'CSE423')])
    Course_Three_Credit = models.CharField(max_length=5, choices= [('1', '1'), ('2', '2'), ('3', '3')])
    Course_Three_TotalNum = models.IntegerField()

    # Course4
    Course_Four_Title = models.CharField(max_length=50,blank=True,null=True, choices=[('Engineering Mathematics', 'Engineering Mathematics'), ('Digital Electronics', 'Digital Electronics'), ('Digital Electronics Lab', 'Digital Electronics Lab'),
        ('Object Oriented Programming', 'Object Oriented Programming'), ('Object Oriented Programming Lab', 'Object Oriented Programming Lab'), ('Bangladesh Studies', 'Bangladesh Studies'), 
        ('Algorithms', 'Algorithms'), ('Algorithms Lab', 'Algorithms Lab'), ('Statiscs and Probability', 'Statiscs and Probability'),('Electronic Devices and Circuits', 'Electronic Devices and Circuits'),
        ('Electronic Devices and Circuits Lab', 'Electronic Devices and Circuits Lab'), ('Microcessor and Assembly Language', 'Microcessor and Assembly Language'),
        ('Microcessor and Assembly Language Lab', 'Microcessor and Assembly Language Lab'), ('Data Communication', 'Data Communication'), ('Numerical Methods', 'Numerical Methods'),
        ('Introduction to Bio-Informatics', 'Introduction to Bio-Informatics'), ('Database Management System', 'Database Management System'), ('Database Management System Lab', 'Database Management System Lab'),
        ('Computer Networks', 'Computer Networks'), ('Computer Networks Lab', 'Computer Networks Lab'), ('Economics', 'Economics'), ('System Analysis Design', 'System Analysis Design'),
        ('Computer Architecture and Organization', 'Computer Architecture and Organization'), ('Operating System', 'Operating System'), ('Operating System Lab', 'Operating System Lab'), ('Art of Living', 'Art of Living'),
        ('Compiler Design', 'Compiler Design'), ('Compiler Design Lab', 'Compiler Design Lab'), ('Software Engineering', 'Software Engineering'), ('Wireless Programming', 'Wireless Programming'),
        ('Financial and managerial Accounting', 'Financial and managerial Accounting'), ('Artificial Intelligence', 'Artificial Intelligence'), ('Artificial Intelligence Lab', 'Artificial Intelligence Lab'), 
        ('Simulation and Modelling', 'Simulation and Modelling'), ('Simulation and Modelling Lab', 'Simulation and Modelling Lab'), ('Web Engineering', 'Web Engineering'), ('Web Engineering Lab', 'Web Engineering Lab'),
        ('Computer Graphics', 'Computer Graphics'), ('Computer Graphics Lab', 'Computer Graphics Lab'), ('Embedded Systems', 'Embedded Systems')])
    Course_Four_Code = models.CharField(max_length=50,blank=True,null=True, choices= [('MAT211', 'MAT211'), ('CSE212', 'CSE212'), ('CSE213', 'CSE213'), ('CSE214', 'CSE214'), ('GED201', 'GED201'), ('CSE221', 'CSE221'), ('CSE222', 'CSE222'), ('STA133', 'STA133'),
        ('CSE224', 'CSE224'), ('CSE225', 'CSE225'), ('CSE231', 'CSE231'), ('CSE232', 'CSE232'), ('CSE233', 'CSE233'), ('CSE234', 'CSE234'), ('CSE235', 'CSE235'), 
        ('CSE311', 'CSE311'), ('CSE312', 'CSE312'), ('CSE313', 'CSE313'), ('CSE314', 'CSE314'), ('ECO314', 'ECO314'), ('CSE321', 'CSE321'), ('CSE322', 'CSE322'), 
        ('CSE323', 'CSE323'), ('CSE324', 'CSE324'), ('GED321', 'GED321'), ('CSE331', 'CSE331'), ('CSE332', 'CSE332'), ('CSE333', 'CSE333'), ('CSE334', 'CSE334'), 
        ('ACT301', 'ATC301'), ('CSE412', 'CSE412'), ('CSE413', 'CSE413'), ('CSE414', 'CSE414'), ('CSE415', 'CSE415'), ('CSE416', 'CSE416'), ('CSE417', 'CSE417'), ('CSE418', 'CSE418')
        , ('CSE421', 'CSE421'), ('CSE422', 'CSE422'), ('CSE423', 'CSE423')])
    Course_Four_Credit = models.CharField(max_length=5,blank=True,null=True, choices= [('1', '1'), ('2', '2'), ('3', '3')])
    Course_Four_TotalNum = models.IntegerField(blank=True,null=True)

    # Course5
    Course_Five_Title = models.CharField(max_length=50,blank=True,null=True, choices=[('Engineering Mathematics', 'Engineering Mathematics'), ('Digital Electronics', 'Digital Electronics'), ('Digital Electronics Lab', 'Digital Electronics Lab'),
        ('Object Oriented Programming', 'Object Oriented Programming'), ('Object Oriented Programming Lab', 'Object Oriented Programming Lab'), ('Bangladesh Studies', 'Bangladesh Studies'), 
        ('Algorithms', 'Algorithms'), ('Algorithms Lab', 'Algorithms Lab'), ('Statiscs and Probability', 'Statiscs and Probability'),('Electronic Devices and Circuits', 'Electronic Devices and Circuits'),
        ('Electronic Devices and Circuits Lab', 'Electronic Devices and Circuits Lab'), ('Microcessor and Assembly Language', 'Microcessor and Assembly Language'),
        ('Microcessor and Assembly Language Lab', 'Microcessor and Assembly Language Lab'), ('Data Communication', 'Data Communication'), ('Numerical Methods', 'Numerical Methods'),
        ('Introduction to Bio-Informatics', 'Introduction to Bio-Informatics'), ('Database Management System', 'Database Management System'), ('Database Management System Lab', 'Database Management System Lab'),
        ('Computer Networks', 'Computer Networks'), ('Computer Networks Lab', 'Computer Networks Lab'), ('Economics', 'Economics'), ('System Analysis Design', 'System Analysis Design'),
        ('Computer Architecture and Organization', 'Computer Architecture and Organization'), ('Operating System', 'Operating System'), ('Operating System Lab', 'Operating System Lab'), ('Art of Living', 'Art of Living'),
        ('Compiler Design', 'Compiler Design'), ('Compiler Design Lab', 'Compiler Design Lab'), ('Software Engineering', 'Software Engineering'), ('Wireless Programming', 'Wireless Programming'),
        ('Financial and managerial Accounting', 'Financial and managerial Accounting'), ('Artificial Intelligence', 'Artificial Intelligence'), ('Artificial Intelligence Lab', 'Artificial Intelligence Lab'), 
        ('Simulation and Modelling', 'Simulation and Modelling'), ('Simulation and Modelling Lab', 'Simulation and Modelling Lab'), ('Web Engineering', 'Web Engineering'), ('Web Engineering Lab', 'Web Engineering Lab'),
        ('Computer Graphics', 'Computer Graphics'), ('Computer Graphics Lab', 'Computer Graphics Lab'), ('Embedded Systems', 'Embedded Systems')])
    Course_Five_Code = models.CharField(max_length=50,blank=True,null=True, choices= [('MAT211', 'MAT211'), ('CSE212', 'CSE212'), ('CSE213', 'CSE213'), ('CSE214', 'CSE214'), ('GED201', 'GED201'), ('CSE221', 'CSE221'), ('CSE222', 'CSE222'), ('STA133', 'STA133'),
        ('CSE224', 'CSE224'), ('CSE225', 'CSE225'), ('CSE231', 'CSE231'), ('CSE232', 'CSE232'), ('CSE233', 'CSE233'), ('CSE234', 'CSE234'), ('CSE235', 'CSE235'), 
        ('CSE311', 'CSE311'), ('CSE312', 'CSE312'), ('CSE313', 'CSE313'), ('CSE314', 'CSE314'), ('ECO314', 'ECO314'), ('CSE321', 'CSE321'), ('CSE322', 'CSE322'), 
        ('CSE323', 'CSE323'), ('CSE324', 'CSE324'), ('GED321', 'GED321'), ('CSE331', 'CSE331'), ('CSE332', 'CSE332'), ('CSE333', 'CSE333'), ('CSE334', 'CSE334'), 
        ('ACT301', 'ATC301'), ('CSE412', 'CSE412'), ('CSE413', 'CSE413'), ('CSE414', 'CSE414'), ('CSE415', 'CSE415'), ('CSE416', 'CSE416'), ('CSE417', 'CSE417'), ('CSE418', 'CSE418')
        , ('CSE421', 'CSE421'), ('CSE422', 'CSE422'), ('CSE423', 'CSE423')])
    Course_Five_Credit = models.CharField(max_length=5,blank=True,null=True, choices= [('1', '1'), ('2', '2'), ('3', '3')])
    Course_Five_TotalNum = models.IntegerField(blank=True,null=True)

    # Course6
    Course_Six_Title = models.CharField(max_length=50,blank=True,null=True, choices=[('Engineering Mathematics', 'Engineering Mathematics'), ('Digital Electronics', 'Digital Electronics'), ('Digital Electronics Lab', 'Digital Electronics Lab'),
        ('Object Oriented Programming', 'Object Oriented Programming'), ('Object Oriented Programming Lab', 'Object Oriented Programming Lab'), ('Bangladesh Studies', 'Bangladesh Studies'), 
        ('Algorithms', 'Algorithms'), ('Algorithms Lab', 'Algorithms Lab'), ('Statiscs and Probability', 'Statiscs and Probability'),('Electronic Devices and Circuits', 'Electronic Devices and Circuits'),
        ('Electronic Devices and Circuits Lab', 'Electronic Devices and Circuits Lab'), ('Microcessor and Assembly Language', 'Microcessor and Assembly Language'),
        ('Microcessor and Assembly Language Lab', 'Microcessor and Assembly Language Lab'), ('Data Communication', 'Data Communication'), ('Numerical Methods', 'Numerical Methods'),
        ('Introduction to Bio-Informatics', 'Introduction to Bio-Informatics'), ('Database Management System', 'Database Management System'), ('Database Management System Lab', 'Database Management System Lab'),
        ('Computer Networks', 'Computer Networks'), ('Computer Networks Lab', 'Computer Networks Lab'), ('Economics', 'Economics'), ('System Analysis Design', 'System Analysis Design'),
        ('Computer Architecture and Organization', 'Computer Architecture and Organization'), ('Operating System', 'Operating System'), ('Operating System Lab', 'Operating System Lab'), ('Art of Living', 'Art of Living'),
        ('Compiler Design', 'Compiler Design'), ('Compiler Design Lab', 'Compiler Design Lab'), ('Software Engineering', 'Software Engineering'), ('Wireless Programming', 'Wireless Programming'),
        ('Financial and managerial Accounting', 'Financial and managerial Accounting'), ('Artificial Intelligence', 'Artificial Intelligence'), ('Artificial Intelligence Lab', 'Artificial Intelligence Lab'), 
        ('Simulation and Modelling', 'Simulation and Modelling'), ('Simulation and Modelling Lab', 'Simulation and Modelling Lab'), ('Web Engineering', 'Web Engineering'), ('Web Engineering Lab', 'Web Engineering Lab'),
        ('Computer Graphics', 'Computer Graphics'), ('Computer Graphics Lab', 'Computer Graphics Lab'), ('Embedded Systems', 'Embedded Systems')])
    Course_Six_Code = models.CharField(max_length=50,blank=True,null=True, choices=[('MAT211', 'MAT211'), ('CSE212', 'CSE212'), ('CSE213', 'CSE213'), ('CSE214', 'CSE214'), ('GED201', 'GED201'), ('CSE221', 'CSE221'), ('CSE222', 'CSE222'), ('STA133', 'STA133'),
        ('CSE224', 'CSE224'), ('CSE225', 'CSE225'), ('CSE231', 'CSE231'), ('CSE232', 'CSE232'), ('CSE233', 'CSE233'), ('CSE234', 'CSE234'), ('CSE235', 'CSE235'), 
        ('CSE311', 'CSE311'), ('CSE312', 'CSE312'), ('CSE313', 'CSE313'), ('CSE314', 'CSE314'), ('ECO314', 'ECO314'), ('CSE321', 'CSE321'), ('CSE322', 'CSE322'), 
        ('CSE323', 'CSE323'), ('CSE324', 'CSE324'), ('GED321', 'GED321'), ('CSE331', 'CSE331'), ('CSE332', 'CSE332'), ('CSE333', 'CSE333'), ('CSE334', 'CSE334'), 
        ('ACT301', 'ATC301'), ('CSE412', 'CSE412'), ('CSE413', 'CSE413'), ('CSE414', 'CSE414'), ('CSE415', 'CSE415'), ('CSE416', 'CSE416'), ('CSE417', 'CSE417'), ('CSE418', 'CSE418')
        , ('CSE421', 'CSE421'), ('CSE422', 'CSE422'), ('CSE423', 'CSE423')])
    Course_Six_Credit = models.CharField(max_length=5,blank=True,null=True, choices= [('1', '1'), ('2', '2'), ('3', '3')])
    Course_Six_TotalNum = models.IntegerField(blank=True,null=True)

    # def __str__(self):
    #     return self.studentId
