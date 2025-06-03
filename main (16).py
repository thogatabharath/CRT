class student_Data:
    def __init__(self,name,roll,age,branch,cgpa):
        self.name=name
        self.roll=roll
        self.age=age
        self.branch=branch
        self.cgpa=cgpa
        self.marks_btech==marks_btech
        self.marks_10th=marks_10th
        self.marks_inter=marks_inter
    def Display(name,roll,age,branch,cgpa):
        return f"name :{name} roll_number :{roll} age = {age}"
        
    def grade(cgpa):
        if(cgpa>9.5):
            return"EXCELLENT"
        elif(cgpa>7 and cgpa>9):
            return "good"
        elif(cgpa>6 and cgpa<7):
            return "average"
    def check_placements(marks_10th,marks_inter,marks_btech):
        if(marks_10th>60 and marks_btech>60 and marks_inter>60):
            return"you are eligible for placements"
        else:return"you are not eligible for placement"
    # creating object
student_1=student_Data
student_2=student_Data
    
    #print(student_1.display("shruthi",20,21,"civil",7.0))
    #print(student_1.check_displacemnet(70,77,80))
    #print(student_2.grade(9.7))
    
            
            
        
        
    
