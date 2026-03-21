def recommend_platform(subject, goal, preference, time):

    subject = subject.lower()
    goal = goal.lower()
    preference = preference.lower()
    time = time.lower()

    # DSA rules
    if subject == "dsa":
        if goal == "practice":
            return "LeetCode", "Best platform for coding practice and problem-solving"
        elif preference == "video":
            return "YouTube", "Quick and easy video explanations available"
        else:
            return "GeeksforGeeks", "Good for theory and structured learning"

    # DBMS rules
    elif subject == "dbms":
        if preference == "notes":
            return "GeeksforGeeks", "Well-structured notes for theory subjects"
        else:
            return "YouTube", "Helpful for understanding concepts visually"

    # OS rules
    elif subject == "os":
        if time == "short":
            return "YouTube", "Quick revision videos available"
        else:
            return "GeeksforGeeks", "Detailed explanation of OS concepts"

    # CN rules
    elif subject == "cn":
        if goal == "revision":
            return "YouTube", "Fast revision content available"
        else:
            return "GeeksforGeeks", "Clear explanations for networking topics"

    # Programming rules
    elif subject == "programming":
        if preference == "coding":
            return "LeetCode", "Practice coding problems effectively"
        else:
            return "YouTube", "Beginner-friendly tutorials available"

    # Default fallback
    return "YouTube", "General learning platform with wide content"


def main():
    print("=== Smart Study Platform Recommender (CS Students) ===\n")

    subject = input("Enter subject (DSA/DBMS/OS/CN/Programming): ")
    goal = input("Enter goal (concept/practice/revision): ")
    preference = input("Enter preference (video/notes/coding): ")
    time = input("Enter time available (short/medium/long): ")

    result, reason = recommend_platform(subject, goal, preference, time)

    print("\n✅ Recommended Platform:", result)
    print("💡 Reason:", reason)


if __name__ == "__main__":
    main()
