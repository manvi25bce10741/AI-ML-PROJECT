#function to calculate scores
def recommend_platform(subject, goal, preference, time):

    subject = subject.lower()
    goal = goal.lower()
    preference = preference.lower()
    time = time.lower()
    # Initialize scores
    scores = {
        "YouTube": 0,
        "GeeksforGeeks": 0,
        "LeetCode": 0,
        "Coursera": 0
    }
    #subject based scoring
    if subject == "dsa":
        scores["LeetCode"] += 3
        scores["GeeksforGeeks"] += 2
    elif subject in ["dbms", "os", "cn"]:
        scores["GeeksforGeeks"] += 3
        scores["YouTube"] += 2
    elif subject == "programming":
        scores["YouTube"] += 2
        scores["LeetCode"] += 2
    #goal based scoring
    if goal == "practice":
        scores["LeetCode"] += 3
    elif goal == "concept":
        scores["YouTube"] += 2
        scores["Coursera"] += 2
    elif goal == "revision":
        scores["YouTube"] += 3
    #preference based scoring
    if preference == "video":
        scores["YouTube"] += 3
        scores["Coursera"] += 2
    elif preference == "notes":
        scores["GeeksforGeeks"] += 3
    elif preference == "coding":
        scores["LeetCode"] += 3
    #time based scoring
    if time == "short":
        scores["YouTube"] += 2
    elif time == "long":
        scores["Coursera"] += 3
    #sort platforms by score
    sorted_platforms = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    #top two recommendations
    top_two = sorted_platforms[:2]

    return top_two, scores

#function for final display of recommendations
def main():
    print("=== Intelligent Study Platform Recommender (AI-Based) ===\n")

    subject = input("Enter subject (DSA/DBMS/OS/CN/Programming): ")
    goal = input("Enter goal (concept/practice/revision): ")
    preference = input("Enter preference (video/notes/coding): ")
    time = input("Enter time available (short/medium/long): ")

    top_two, scores = recommend_platform(subject, goal, preference, time)

    print("\n Score Breakdown:")
    for platform, score in scores.items():
        print(f"{platform}: {score}")

    print("\n Top Recommendations:")
    print(f"1. {top_two[0][0]} (Score: {top_two[0][1]})")
    print(f"2. {top_two[1][0]} (Score: {top_two[1][1]})")


if __name__ == "__main__":
    main()
    #to collect feedback from user
    feedback = input("\nWas this recommendation helpful? (yes/no): ").strip().lower()

    if feedback == "yes":
        print("Glad it helped! ")
    elif feedback == "no":
        print("Thanks for your feedback! This can be used to improve the system.")
    else:
        print("Invalid input. Please enter yes or no next time.")
