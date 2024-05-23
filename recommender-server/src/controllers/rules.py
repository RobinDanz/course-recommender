RULES = []

# Social computing
RULES.append("IF "
             "(Evaluation IS project) "
             "THEN "
             "(SocialComputing IS recommended)")

RULES.append("IF "
             "(NOT(Evaluation IS project)) "
             "THEN "
             "(SocialComputing IS notRecommended)")

RULES.append("IF "
             "(University IS fribourg) "
             "THEN "
             "(SocialComputing IS recommended) ")

RULES.append("IF "
             "(NOT(University IS fribourg)) "
             "THEN "
             "(SocialComputing IS notRecommended)")

RULES.append("IF "
             "(CourseType IS seminar) "
             "THEN "
             "(SocialComputing IS recommended)")

RULES.append("IF "
             "(NOT(CourseType IS seminar)) "
             "THEN "
             "(SocialComputing IS notRecommended)")

RULES.append("IF "
             "(Track IS T5) OR "
             "(Track IS T6) "
             "THEN "
             "(SocialComputing IS recommended)")

# RULES.append("IF "
#              "(NOT(Track IS T5)) "
#              "THEN "
#              "(SocialComputing IS notRecommended)")

RULES.append("IF "
             "(Lectures IS always) "
             "THEN "
             "(SocialComputing IS recommended)")

RULES.append("IF "
             "(NOT(Lectures IS always)) "
             "THEN "
             "(SocialComputing IS notRecommended)")

RULES.append("IF "
             "(SubjectType IS always) "
             "THEN "
             "(SocialComputing IS recommended)")

RULES.append("IF "
             "(NOT(SubjectType IS always)) "
             "THEN "
             "(SocialComputing IS notRecommended)")

RULES.append("IF "
             "(Interactions IS some) OR "
             "(Interactions IS none) "
             "THEN "
             "(SocialComputing IS recommended")

# RULES.append("IF "
#              "(NOT(Interactions IS some)) "
#              "THEN "
#              "(SocialComputing IS notRecommended)")

RULES.append("IF "
             "(Blackboard IS none) "
             "THEN "
             "(SocialComputing IS recommended)")

RULES.append("IF "
             "(NOT(Blackboard IS none)) "
             "THEN "
             "(SocialComputing IS notRecommended)")

RULES.append("IF "
             "(Recordings IS none) "
             "THEN "
             "(SocialComputing IS recommended)")

RULES.append("IF "
             "(NOT(Recordings IS none)) "
             "THEN "
             "(SocialComputing IS notRecommended)")

RULES.append("IF "
             "(TeacherAccessibilty IS middle) "
             "THEN "
             "(SocialComputing IS recommended)")

RULES.append("IF "
             "(NOT(TeacherAccessibilty IS middle)) "
             "THEN "
             "(SocialComputing IS notRecommended)")

# Concurrency
RULES.append("IF "
             "(Evaluation IS written) "
             "THEN "
             "(Concurrency IS recommended)")

RULES.append("IF "
             "(NOT(Evaluation IS written)) "
             "THEN "
             "(Concurrency IS notRecommended)")

RULES.append("IF "
             "(University IS neuchatel) "
             "THEN "
             "(Concurrency IS recommended)")

RULES.append("IF "
             "(NOT(University IS neuchatel)) "
             "THEN "
             "(Concurrency IS notRecommended)")

RULES.append("IF "
             "(CourseType IS course) "
             "THEN "
             "(Concurrency IS recommended)")

RULES.append("IF "
             "(NOT(CourseType IS course)) "
             "THEN "
             "(Concurrency IS notRecommended)")

RULES.append("IF "
             "(Track IS T1) OR "
             "(Track IS T6) "
             "THEN "
             "(Concurrency IS recommended)")

# RULES.append("IF "
#              "(NOT(Track IS T1)) "
#              "THEN "
#              "(Concurrency IS notRecommended)")

RULES.append("IF "
             "(Lectures IS some) "
             "THEN "
             "(Concurrency IS recommended)")

RULES.append("IF "
             "(NOT(Lectures IS some)) "
             "THEN "
             "(Concurrency IS notRecommended)")

RULES.append("IF "
             "(SubjectType IS regularly) "
             "THEN "
             "(Concurrency IS recommended)")

RULES.append("IF "
             "(NOT(SubjectType IS regularly)) "
             "THEN "
             "(Concurrency IS notRecommended)")

RULES.append("IF "
             "(Interactions IS some) "
             "THEN "
             "(Concurrency IS recommended)")

RULES.append("IF "
             "(NOT(Interactions IS some)) "
             "THEN "
             "(Concurrency IS notRecommended)")

RULES.append("IF "
             "(Blackboard IS none) "
             "THEN "
             "(Concurrency IS recommended)")

RULES.append("IF "
             "(NOT(Blackboard IS none)) "
             "THEN "
             "(Concurrency IS notRecommended)")

RULES.append("IF "
             "(Recordings IS always) "
             "THEN "
             "(Concurrency IS recommended)")

RULES.append("IF "
             "(NOT(Recordings IS always)) "
             "THEN "
             "(Concurrency IS notRecommended)")

RULES.append("IF "
             "(TeacherAccessibilty IS regularly) "
             "THEN "
             "(Concurrency IS recommended)")

RULES.append("IF "
             "(NOT(TeacherAccessibilty IS regularly)) "
             "THEN "
             "(Concurrency IS notRecommended)")

# Fuzzy Sets 2
RULES.append("IF "
             "(Evaluation IS written) "
             "THEN "
             "(FuzzySets2 IS recommended)")

RULES.append("IF "
             "(NOT(Evaluation IS written)) "
             "THEN "
             "(FuzzySets2 IS notRecommended)")

RULES.append("IF "
             "(University IS fribourg) "
             "THEN "
             "(FuzzySets2 IS recommended)")

RULES.append("IF "
             "(NOT(University IS fribourg)) "
             "THEN "
             "(FuzzySets2 IS notRecommended)")

RULES.append("IF "
             "(CourseType IS course) "
             "THEN "
             "(FuzzySets2 IS recommended)")

RULES.append("IF "
             "(NOT(CourseType IS course)) "
             "THEN "
             "(FuzzySets2 IS notRecommended)")

RULES.append("IF "
             "(Track IS T5) OR "
             "(Track IS T6) "
             "THEN "
             "(FuzzySets2 IS recommended)")

# RULES.append("IF "
#              "(NOT(Track IS T5)) "
#              "THEN "
#              "(FuzzySets2 IS notRecommended)")

RULES.append("IF "
             "(Lectures IS regularly) "
             "THEN "
             "(FuzzySets2 IS recommended)")

RULES.append("IF "
             "(NOT(Lectures IS regularly)) "
             "THEN "
             "(FuzzySets2 IS notRecommended)")

RULES.append("IF "
             "(SubjectType IS some) "
             "THEN "
             "(FuzzySets2 IS recommended)")

RULES.append("IF "
             "(NOT(SubjectType IS some)) "
             "THEN "
             "(FuzzySets2 IS notRecommended)")

RULES.append("IF "
             "(Interactions IS always) "
             "THEN "
             "(FuzzySets2 IS recommended)")

RULES.append("IF "
             "(NOT(Interactions IS always)) "
             "THEN "
             "(FuzzySets2 IS notRecommended)")

RULES.append("IF "
             "(Blackboard IS none) "
             "THEN "
             "(FuzzySets2 IS recommended)")

RULES.append("IF "
             "(NOT(Blackboard IS none)) "
             "THEN "
             "(FuzzySets2 IS notRecommended)")

RULES.append("IF "
             "(Recordings IS none) "
             "THEN "
             "(FuzzySets2 IS recommended)")

RULES.append("IF "
             "(NOT(Recordings IS none)) "
             "THEN "
             "(FuzzySets2 IS notRecommended)")

RULES.append("IF "
             "(TeacherAccessibilty IS middle) "
             "THEN "
             "(FuzzySets2 IS recommended)")

RULES.append("IF "
             "(NOT(TeacherAccessibilty IS middle)) "
             "THEN "
             "(FuzzySets2 IS notRecommended)")

RULES.append("IF "
             "(University IS bern) "
             "THEN "
             "(test IS recommended)")
