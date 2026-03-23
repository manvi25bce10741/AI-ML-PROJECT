# Study platform recommender
OVERVIEW:
The Smart Study Platform Recommender System is a Python-based application designed to assist Computer Science students in selecting the most suitable platform for studying various subjects. It helps students navigate through the large number of options available to learn new concepts and skills. It aims at helping students avoid confusion when they are exposed to the huge glamorous yet scary world of computer science. The system takes user inputs such as subject, goal, learning preference, and available time, and uses a weighted scoring mechanism to recommend the top platforms.
Unlike basic rule-based systems, this project introduces a scoring and ranking approach, making it more aligned with Artificial Intelligence concepts such as decision-making, ranking, and explainability.

FEATURES:
User input collection:
 Subject (DSA, DBMS, OS, CN, Programming)
 Goal (Concept understanding, Practice, Revision)
 Learning preference (Video, Notes, Coding)
 Time available (Short, Medium, Long)
 Weighted scoring system for intelligent decision-making
 Ranking of platforms based on computed scores
 Top 2 platform recommendations instead of a single output
 Score breakdown for transparency and explainability
 Simple and user-friendly terminal interface

HOW THE PROGRAM WORKS:
Each platform is given a score based on the user’s inputs. For example, if the user selects coding practice, platforms like LeetCode get higher scores. After assigning scores, the platforms are sorted and the top two are shown.
This approach is similar to a basic recommendation system where decisions are made based on weighted conditions.
 
TECHNOLOGIES / TOOLS USED:
Python 3
Functions for modular programming
Conditional statements and scoring logic
GitHub for version control and repository management

STEPS TO INSTALL AND RUN THE PROGRAM:
Clone the repository
Navigate to the project folder
Run the program

LIMITATIONS:
The system uses fixed rules and does not learn automatically
Recommendations are general and may not fit everyone
No real-time data is used

FUTURE IMPROVEMENTS:
Add user feedback storage
Use real data for better recommendations
Convert into a web application
Implement machine learning for personalization

CONCLUSION:
This project solves a simple but common problem faced by students. It shows how basic programming and logic can be used to build a useful tool. With further improvements, it can be expanded into a more advanced recommendation system.
