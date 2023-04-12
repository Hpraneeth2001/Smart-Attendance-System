# Smart-Attendance-System
This is a Python program that recognizes faces from images and videos, and marks attendance based on the faces detected. It uses the face_recognition library to perform face recognition.

Prerequisites
Python 3
OpenCV
NumPy
face_recognition
pyttsx3
How to use
Clone the repository to your local machine.
Navigate to the project directory and install the required libraries by running the following command: pip install -r requirements.txt
Add images of the students to the student_images directory with their names as the file name.
Run the program by executing the command python main.py.
The program will open the default camera and start detecting faces.
If a recognized face is detected, the program will mark attendance in a CSV file and welcome the student.
To stop the program, press q.
References
face_recognition library
OpenCV
NumPy
pyttsx3 library
