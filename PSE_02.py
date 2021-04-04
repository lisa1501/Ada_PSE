def get_student_data(student_list):
      all_student_data=[]
      if not student_list:
            return None
      for i in range(len(student_list)):
            student=student_list[i]
            student_data={}
            id_start_with=5071109000
            if  student != "" and type(student) == str:
                  student_data["name"]= student
                  student_data["id"]=(i*2)+id_start_with
                  all_student_data.append(student_data)
      
      return all_student_data
      

# my_students_list=["Mike","Jared","Alison","Heidi","","Heidi",55]
my_students_list=[]
a=get_student_data(my_students_list)
print(a)
def get_id_by_name(name,student_list):
      if not student_list:
            return None
      student_data=get_student_data(student_list)
      print(student_data)
     
      for student in student_data:
            
                  if student["name"]==name:
                        return student["id"]
      

my_name=get_id_by_name("Mike",my_students_list)
print(my_name)
def get_name_by_id(id,student_list):
      if not student_list:
            return None
      student_data=get_student_data(student_list)
      
      for student in student_data:
           
                  if student["id"]==id:
                        return student["name"]
my_id=get_name_by_id(5071109000,my_students_list)
print(my_id)









# five questions:
#time o(n) o(n)
#1.Given input data only the name list, 
#1. edge case : length of the input data, if it is an empty list
#2. if there is an empty string or type of the element is not string
#3. if there are same names in the name list
#4. how should we get the id (import UUID) or start with the  special number, how can we make it 
# consecutive, example: by increament 2 or three, odd or even number,range for id number. how many digits for one id number.

#5.how is format of the output what is the return value {"halise":456,"456":"halise"}

#import  uidd  for id_list

# sub problem :
# arguments one or two, two list length equeal or not 
# where can we find the id , 
# list of dictionary  in dictionary items key value format 