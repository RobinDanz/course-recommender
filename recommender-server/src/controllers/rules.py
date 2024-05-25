RULES = []

# Track 0: Quantitative Methods of Performance Evaluation for Computing Systems (QMPECS)
RULES.append("IF "
             "(Evaluation IS continuous) OR "
             "(Evaluation IS project) "
             "THEN "
             "(QMPECS IS recommended)")

RULES.append("IF "
             "(University IS neuchatel) "
             "THEN "
             "(QMPECS IS recommended)")

RULES.append("IF "
             "(NOT(University IS neuchatel)) "
             "THEN "
             "(QMPECS IS notRecommended)")

RULES.append("IF "
             "(CourseType IS course) "
             "THEN "
             "(QMPECS IS recommended)")

RULES.append("IF "
             "(NOT(CourseType IS course)) "
             "THEN "
             "(QMPECS IS notRecommended)")

RULES.append("IF "
             "(Track IS T0) OR "
             "(Track IS T6) "
             "THEN "
             "(QMPECS IS recommended)")

RULES.append("IF "
             "(Lectures IS regularly) "
             "THEN "
             "(QMPECS IS recommended)")

RULES.append("IF "
             "(NOT(Lectures IS regularly)) "
             "THEN "
             "(QMPECS IS notRecommended)")

RULES.append("IF "
             "(SubjectType IS none) OR "
             "(SubjectType IS some) "
             "THEN "
             "(QMPECS IS recommended)")

RULES.append("IF "
             "(Interactions IS middle) "
             "THEN "
             "(QMPECS IS recommended)")

RULES.append("IF "
             "(NOT(Interactions IS middle)) "
             "THEN "
             "(QMPECS IS notRecommended)")

RULES.append("IF "
             "(Blackboard IS some) "
             "THEN "
             "(QMPECS IS recommended)")

RULES.append("IF "
             "(NOT(Blackboard IS some)) "
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
             "(TeacherAccessibilty IS some) "
             "THEN "
             "(FuzzySets2 IS recommended)")

RULES.append("IF "
             "(NOT(TeacherAccessibilty IS some)) "
             "THEN "
             "(FuzzySets2 IS notRecommended)")

# Track 1: Concurrency
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

# Track 2:

# Track 3: Applied Optimization
RULES.append("IF "
             "(Evaluation IS written) "
             "THEN "
             "(AppliedOptimization IS recommended)")

RULES.append("IF "
             "(NOT(Evaluation IS written)) "
             "THEN "
             "(AppliedOptimization IS notRecommended)")

RULES.append("IF "
             "(University IS bern) "
             "THEN "
             "(AppliedOptimization IS recommended)")

RULES.append("IF "
             "(NOT(University IS bern)) "
             "THEN "
             "(AppliedOptimization IS notRecommended)")

RULES.append("IF "
             "(CourseType IS course) "
             "THEN "
             "(AppliedOptimization IS recommended)")

RULES.append("IF "
             "(NOT(CourseType IS course)) "
             "THEN "
             "(AppliedOptimization IS notRecommended)")

RULES.append("IF "
             "(Track IS T3) OR "
             "(Track IS T6) "
             "THEN "
             "(AppliedOptimization IS recommended)")

RULES.append("IF "
             "(Lectures IS middle) "
             "THEN "
             "(AppliedOptimization IS recommended)")

RULES.append("IF "
             "(NOT(Lectures IS middle)) "
             "THEN "
             "(AppliedOptimization IS notRecommended)")

RULES.append("IF "
             "(SubjectType IS some) "
             "THEN "
             "(AppliedOptimization IS recommended)")

RULES.append("IF "
             "(NOT(SubjectType IS some)) "
             "THEN "
             "(AppliedOptimization IS notRecommended)")

RULES.append("IF "
             "(Interactions IS some) "
             "THEN "
             "(AppliedOptimization IS recommended)")

RULES.append("IF "
             "(NOT(Interactions IS some)) "
             "THEN "
             "(AppliedOptimization IS notRecommended)")

RULES.append("IF "
             "(Blackboard IS middle) "
             "THEN "
             "(AppliedOptimization IS recommended)")

RULES.append("IF "
             "(NOT(Blackboard IS middle)) "
             "THEN "
             "(AppliedOptimization IS notRecommended)")

RULES.append("IF "
             "(Recordings IS always) "
             "THEN "
             "(AppliedOptimization IS recommended)")

RULES.append("IF "
             "(NOT(Recordings IS always)) "
             "THEN "
             "(AppliedOptimization IS notRecommended)")

RULES.append("IF "
             "(TeacherAccessibilty IS middle) "
             "THEN "
             "(AppliedOptimization IS recommended)")

RULES.append("IF "
             "(NOT(TeacherAccessibilty IS middle)) "
             "THEN "
             "(AppliedOptimization IS notRecommended)")

# Track 4: Machine Learning and Data Mining
RULES.append("IF "
             "(Evaluation IS written) "
             "THEN "
             "(MLDM IS recommended)")

RULES.append("IF "
             "(NOT(Evaluation IS written)) "
             "THEN "
             "(MLDM IS notRecommended)")

RULES.append("IF "
             "(University IS neuchatel) "
             "THEN "
             "(MLDM IS recommended)")

RULES.append("IF "
             "(NOT(University IS neuchatel)) "
             "THEN "
             "(MLDM IS notRecommended)")

RULES.append("IF "
             "(CourseType IS course) "
             "THEN "
             "(MLDM IS recommended)")

RULES.append("IF "
             "(NOT(CourseType IS course)) "
             "THEN "
             "(MLDM IS notRecommended)")

RULES.append("IF "
             "(Track IS T4) OR "
             "(Track IS T6) "
             "THEN "
             "(MLDM IS recommended)")

RULES.append("IF "
             "(Lectures IS middle) "
             "THEN "
             "(MLDM IS recommended)")

RULES.append("IF "
             "(NOT(Lectures IS middle)) "
             "THEN "
             "(MLDM IS notRecommended)")

RULES.append("IF "
             "(SubjectType IS none) "
             "THEN "
             "(MLDM IS recommended)")

RULES.append("IF "
             "(NOT(SubjectType IS none)) "
             "THEN "
             "(MLDM IS notRecommended)")

RULES.append("IF "
             "(Interactions IS some) "
             "THEN "
             "(MLDM IS recommended)")

RULES.append("IF "
             "(NOT(Interactions IS some)) "
             "THEN "
             "(MLDM IS notRecommended)")

RULES.append("IF "
             "(Blackboard IS always) "
             "THEN "
             "(MLDM IS recommended)")

RULES.append("IF "
             "(NOT(Blackboard IS always)) "
             "THEN "
             "(MLDM IS notRecommended)")

RULES.append("IF "
             "(Recordings IS always) "
             "THEN "
             "(MLDM IS recommended)")

RULES.append("IF "
             "(NOT(Recordings IS always)) "
             "THEN "
             "(MLDM IS notRecommended)")

RULES.append("IF "
             "(TeacherAccessibilty IS middle) "
             "THEN "
             "(MLDM IS recommended)")

RULES.append("IF "
             "(NOT(TeacherAccessibilty IS middle)) "
             "THEN "
             "(MLDM IS notRecommended)")

# Track 5: Social computing
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
             "(SocialComputing IS recommended)")

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
             "(TeacherAccessibilty IS regularly) "
             "THEN "
             "(SocialComputing IS recommended)")

RULES.append("IF "
             "(NOT(TeacherAccessibilty IS regularly)) "
             "THEN "
             "(SocialComputing IS notRecommended)")


# Track 5: Fuzzy Sets 2
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

RULES.append("IF "
             "(Lectures IS regularly) "
             "THEN "
             "(FuzzySets2 IS recommended)")

RULES.append("IF "
             "(NOT(Lectures IS regularly)) "
             "THEN "
             "(FuzzySets2 IS notRecommended)")

RULES.append("IF "
             "(SubjectType IS middle) "
             "THEN "
             "(FuzzySets2 IS recommended)")

RULES.append("IF "
             "(NOT(SubjectType IS middle)) "
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
             "(TeacherAccessibilty IS regularly) "
             "THEN "
             "(FuzzySets2 IS recommended)")

RULES.append("IF "
             "(NOT(TeacherAccessibilty IS regularly)) "
             "THEN "
             "(FuzzySets2 IS notRecommended)")


