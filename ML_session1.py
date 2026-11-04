class Student:
    def __init__(self, name, family, national_id, major, grades, units):
        self.name = name
        self.family = family
        self.national_id = national_id
        self.major = major
        self.grades = grades
        self.units = units

    def data_validate(self):
        # بررسی نام
        if not self.name:
            print("error: name should not be empty")
            return False

        if len(self.name) < 2:
            print("error: name is not valid")
            return False

        if self.name.isdigit():
            print("error: name is not valid")
            return False

        # بررسی نام خانوادگی
        if not self.family:
            print("error: family should not be empty")
            return False

        if len(self.family) < 3:
            print("error: family is not valid")
            return False

        if self.family.isdigit():
            print("error: family is not valid")
            return False

        # بررسی کد ملی
        if not self.national_id:
            print("error: national_id should not be empty")
            return False

        if not self.national_id.isdigit():
            print("error: national_id should contain numbers only")
            return False

        if len(self.national_id) != 10:
            print("error: national_id should be exactly 10 digits")
            return False

        if len(set(self.national_id)) == 1:
            print("error: national_id should not contain the same digit 10 times")
            return False

        # بررسی رشتهٔ تحصیلی (هم فارسی هم انگلیسی پذیرفته شود)
        valid_majors = [
            "financial management", "accounting", "economy", "computer engineering",
            "مدیریت مالی", "حسابداری", "اقتصاد", "مهندسی کامپیوتر"
        ]

        if self.major not in valid_majors:
            print("error: major is not valid")
            return False

        # بررسی لیست نمرات
        if not isinstance(self.grades, list):
            print("error: grades should be list type")
            return False
    
        if len(self.grades) == 0:
            print("error: list of grades should not be empty")
            return False
        
        if len(self.grades) > 10:
            print("error: maximum of lessons should be 10")
            return False
        
        for grade in self.grades:
            if isinstance(grade, str):
                print("error: every member of the list should not be string")
                return False
            
            if not isinstance(grade, (int, float)):
                print("error: every member should be integer or float")
                return False
            
            if not (0 <= grade <= 20):
                print("error: every grade should be between 0 and 20")
                return False
            
        # بررسی لیست واحدها
        if not isinstance(self.units, list):
            print("error: units should be list type")
            return False
        
        if len(self.units) != len(self.grades):
            print("error: the number of units should match the number of grades")
            return False
        
        for unit in self.units:
            if not isinstance(unit, int) or isinstance(unit, bool):
                print("error: every unit should be integer")
                return False
            
            if not (1 <= unit <= 4):
                print("error: every unit should be between 1 and 4")
                return False
            
        # محاسبه معدل وزنی
        total_points = sum(g * u for g, u in zip(self.grades, self.units))
        total_units = sum(self.units) 
        gpa = round(total_points / total_units, 2)

        # وضعیت تحصیلی
        if 17 <= gpa <= 20:
            status = "ممتاز"
        elif 12 <= gpa < 17:
            status = "عادی"
        else:
            status = "مشروط"

        # ذخیره در فایل
        with open("student_report.txt", "a", encoding="utf-8") as file:
            file.write(f"نام: {self.name} {self.family}\n")
            file.write(f"کد ملی: {self.national_id}\n")
            file.write(f"رشته: {self.major}\n")
            file.write(f"معدل: {gpa}\n")
            file.write(f"وضعیت: {status}\n")
            file.write("--------------------\n")

        print("اطلاعات با موفقیت ذخیره شد")
        print("معدل:", gpa)
        print("وضعیت:", status)
        return True


# نمونه اجرا
student = Student(
    name="زهرا",
    family="رضایی",
    national_id="0018345678",
    major="مهندسی کامپیوتر",
    grades=[18, 15, 12.5],
    units=[3, 3, 3]
)

# متد اجرا می‌شود
student.data_validate()