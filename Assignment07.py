# ---------------------------------------- #
# Title: Assignment07
# Description: This assignment demonstrates data processing with added classes.
# Change Log: Katie Debetaz, 11/21/2024, Created Script
# ---------------------------------------- #

import json

# Define Constants
MENU = """ 
---- Course Registration Program ----
Select from the following menu:  
1. Register a student for a course
2. Show current data  
3. Save data to a file
4. Exit the program
----------------------------------------- 
"""
FILE_NAME = "Enrollments.json"

# Define Variables
students: list = []
menu_choice: str = ""

class Person:
    """
    This class represents person data.

    Properties:
        student_first_name: str
        student_last_name: str

    Katie Debetaz, 11/26/2024, Created Class
    """
    def __init__(self,student_first_name: str='',student_last_name: str=''):
        self.student_first_name = student_first_name
        self.student_last_name = student_last_name

    @property
    def student_first_name(self):
        return self.__student_first_name.title()

    @student_first_name.setter
    def student_first_name(self, value:str):
        if value.isalpha() or value == "":
            self.__student_first_name = value
        else:
            raise ValueError("The first name must be alphabetic")

    @property
    def student_last_name(self):
        return self.__student_last_name.title()

    @student_last_name.setter
    def student_last_name(self, value: str):
        if value.isalpha() or value == "":
            self.__student_last_name = value
        else:
            raise ValueError("The last name must be alphabetic")

    def __str__(self):
        return f'{self.student_first_name},{self.student_last_name}'


class Student(Person):
    """
    This class represents student data.

    Properties:
        student_first_name: str
        student_last_name: str
        course_name: str

    Katie Debetaz, 11/26/2024, Created Class
    """

    def __init__(self,student_first_name: str='',student_last_name: str='',course_name: str=''):
        super().__init__(student_first_name=student_first_name, student_last_name=student_last_name)
        self.course_name = course_name

    @property
    def course_name(self):
        return self.__course_name.title()

    @course_name.setter
    def course_name(self, value:str):
        self.__course_name = value


    def __str__(self):
        return f'{self.student_first_name},{self.student_last_name},{self.course_name}'

class FileProcessor:
    """
    Collection of functions for processing json files.

    Katie Debetaz, 11/14/2024, Created Class
    """

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        This function reads the existing data from the json.

        Katie Debetaz, 11/14/2024, Created function

        :return: list of current data
        """

        list_of_dictionary_data: list = []
        student_object: object
        try:
            file = open(file_name, "r")
            list_of_dictionary_data = json.load(file)  # the load function returns a list of dictionary rows.
            for student in list_of_dictionary_data:  # Convert the list of dictionary rows into Student objects
                student_object: Student = Student(student_first_name=student["FirstName"],
                                                  student_last_name=student["LastName"],
                                                  course_name=student["CourseName"])
                student_data.append(student_object)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running this script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        This function writes new data to the json.

        Katie Debetaz, 11/14/2024, Created function

        :return: None
        """

        try:
            list_of_dictionary_data: list = []
            for student in student_data:  # Convert List of Student objects to list of dictionary rows.
                student_json: dict \
                    = {"FirstName": student.student_first_name, "LastName": student.student_last_name,
                       "CourseName": student.course_name}
                list_of_dictionary_data.append(student_json)

            file = open(file_name, "w")
            json.dump(list_of_dictionary_data, file)
            file.close()
            IO.output_student_courses(student_data=student_data)
        except TypeError as e:
            IO.output_error_messages("Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()


class IO:
    """
    Collection of functions for user interaction.

    Katie Debetaz, 11/14/2024, Created Class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        This function prints the error message if applicable.

        Katie Debetaz, 11/14/2024, Created function

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        This function prints the menu.

        Katie Debetaz, 11/14/2024, Created function

        :return: None
        """
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """
        This function asks the user to make a menu choice.

        Katie Debetaz, 11/14/2024, Created function

        :return: string of user's menu choice
        """
        try:
            menu_choice = input("Please enter your choice: ")
            if menu_choice not in ("1","2","3","4"):
                raise Exception("Please only choose 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return menu_choice

    @staticmethod
    def output_student_courses(student_data: list):
        """
        This function prints the current data.

        Katie Debetaz, 11/14/2024, Created function

        :return: None
        """
        print("The current data is:")
        for student in student_data:
            print(f'{student.student_first_name}'
                  f' {student.student_last_name} is registered for {student.course_name}.')


    @staticmethod
    def input_student_data(student_data: list):
        """
        This function asks the user to input the first, last, and course name.

        Katie Debetaz, 11/14/2024, Created function

        :return: list of current student data
        """
        try:
            student = Student()
            student.student_first_name = input("Enter student's first name: ")
            student.student_last_name = input("Enter student's last name: ")
            student.course_name = input("Enter the name of the course: ")
            student_data.append(student)

        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data


# Main program
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Processing options for menu
while True:
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input for student name and course
    if menu_choice == "1":
        students = IO.input_student_data(student_data=students)

    # Print saved data as a formatted string
    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)

    # Export data to json
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)

    # End program
    elif menu_choice == "4":
        print("Program ended")
        break

    # Validate input
    else:
        print("Choice invalid, please try again.")