RULES = []

# Social computing
RULES.append("IF "
             "(Evaluation IS project) OR "
             "(University IS fribourg) OR "
             "(CourseType IS seminar) OR "
             "(Track IS T5) OR "
             "(Lectures IS always) OR "
             "(SubjectType IS always) OR "
             "(Interactions IS some) OR "
             "(Blackboard IS none) OR "
             "(Recordings IS none) OR "
             "(TeacherAccessibilty IS middle) "
             "THEN "
             "(SocialComputing IS recommended)")
"""
RULES.append("IF "
             "(NOT(Evaluation IS project)) OR "
             "(NOT(University IS fribourg)) OR "
             "(NOT(CourseType IS seminar)) OR "
             "(NOT(Track IS T5)) OR "
             "(NOT(Lectures IS always)) OR "
             "(NOT(SubjectType IS always)) OR "
             "(NOT(Interactions IS some)) OR "
             "(NOT(Blackboard IS none)) OR "
             "(NOT(Recordings IS none)) OR "
             "(NOT(TeacherAccessibilty IS middle)) "
             "THEN "
             "(SocialComputing IS notRecommended)")
"""
RULES.append("IF "
             "(Evaluation IS project) AND "
             "(University IS fribourg) AND "
             "(CourseType IS seminar) AND "
             "(Track IS T6) AND "
             "(Lectures IS always) AND "
             "(SubjectType IS always) AND "
             "(Interactions IS some) AND "
             "(Blackboard IS none) AND "
             "(Recordings IS none) AND "
             "(TeacherAccessibilty IS middle) "
             "THEN "
             "(SocialComputing IS recommended)")

RULES.append("IF "
             "(Evaluation IS project) AND "
             "(University IS fribourg) AND "
             "(CourseType IS seminar) AND "
             "(Track IS T5) AND "
             "(Lectures IS always) AND "
             "(SubjectType IS always) AND "
             "(Interactions IS none) AND "
             "(Blackboard IS none) AND "
             "(Recordings IS none) AND "
             "(TeacherAccessibilty IS middle) "
             "THEN "
             "(SocialComputing IS recommended)")

RULES.append("IF "
             "(Evaluation IS project) AND "
             "(University IS fribourg) AND "
             "(CourseType IS seminar) AND "
             "(Track IS T6) AND "
             "(Lectures IS always) AND "
             "(SubjectType IS always) AND "
             "(Interactions IS none) AND "
             "(Blackboard IS none) AND "
             "(Recordings IS none) AND "
             "(TeacherAccessibilty IS middle) "
             "THEN "
             "(SocialComputing IS recommended)")


# Concurrency
RULES.append("IF "
             "(Evaluation IS written) AND "
             "(University IS neuchatel) AND "
             "(CourseType IS course) AND "
             "(Track IS T1) AND "
             "(Lectures IS some) AND "
             "(SubjectType IS regularly) AND "
             "(Interactions IS some) AND "
             "(Blackboard IS none) AND "
             "(Recordings IS always) AND "
             "(TeacherAccessibilty IS regularly) "
             "THEN "
             "(Concurrency IS recommended)")

RULES.append("IF "
             "(Evaluation IS written) AND "
             "(University IS neuchatel) AND "
             "(CourseType IS course) AND "
             "(Track IS T6) AND "
             "(Lectures IS some) AND "
             "(SubjectType IS regularly) AND "
             "(Interactions IS some) AND "
             "(Blackboard IS none) AND "
             "(Recordings IS always) AND "
             "(TeacherAccessibilty IS regularly) "
             "THEN "
             "(Concurrency IS recommended)")


# Fuzzy Sets 2
RULES.append("IF "
             "(Evaluation IS written) AND "
             "(University IS fribourg) AND "
             "(CourseType IS course) AND "
             "(Track IS T5) AND "
             "(Lectures IS regularly) AND "
             "(SubjectType IS some) AND "
             "(Interactions IS always) AND "
             "(Blackboard IS none) AND "
             "(Recordings IS none) AND "
             "(TeacherAccessibilty IS middle) "
             "THEN "
             "(FuzzySets2 IS recommended)")

RULES.append("IF "
             "(Evaluation IS written) AND "
             "(University IS fribourg) AND "
             "(CourseType IS course) AND "
             "(Track IS T6) AND "
             "(Lectures IS regularly) AND "
             "(SubjectType IS some) AND "
             "(Interactions IS always) AND "
             "(Blackboard IS none) AND "
             "(Recordings IS none) AND "
             "(TeacherAccessibilty IS middle) "
             "THEN "
             "(FuzzySets2 IS recommended)")


# Test 
RULES.append("IF "
             "(University IS bern) "
             "THEN "
             "(test IS recommended)")