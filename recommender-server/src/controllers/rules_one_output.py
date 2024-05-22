RULES = []

# Social computing
RULES.append("IF "
             "(Evaluation IS project) "
             "THEN "
             "(Course IS SocialComputing)")

RULES.append("IF "
             "(University IS fribourg) "
             "THEN "
             "(Course IS SocialComputing) ")


RULES.append("IF "
             "(CourseType IS seminar) "
             "THEN "
             "(Course IS SocialComputing)")


RULES.append("IF "
             "(Track IS T5) OR "
             "(Track IS T6) "
             "THEN "
             "(Course IS SocialComputing)")


RULES.append("IF "
             "(Lectures IS always) "
             "THEN "
             "(Course IS SocialComputing)")


RULES.append("IF "
             "(SubjectType IS always) "
             "THEN "
             "(Course IS SocialComputing)")


RULES.append("IF "
             "(Interactions IS some) OR "
             "(Interactions IS none) "
             "THEN "
             "(Course IS SocialComputing")


RULES.append("IF "
             "(Blackboard IS none) "
             "THEN "
             "(Course IS SocialComputing)")


RULES.append("IF "
             "(Recordings IS none) "
             "THEN "
             "(Course IS SocialComputing)")

RULES.append("IF "
             "(TeacherAccessibilty IS middle) "
             "THEN "
             "(Course IS SocialComputing)")


# Concurrency
RULES.append("IF "
             "(Evaluation IS written) "
             "THEN "
             "(Course IS Concurrency)")


RULES.append("IF "
             "(University IS neuchatel) "
             "THEN "
             "(Course IS Concurrency)")

RULES.append("IF "
             "(CourseType IS course) "
             "THEN "
             "(Course IS Concurrency)")

RULES.append("IF "
             "(Track IS T1) OR "
             "(Track IS T6) "
             "THEN "
             "(Course IS Concurrency)")

RULES.append("IF "
             "(Lectures IS some) "
             "THEN "
             "(Course IS Concurrency)")

RULES.append("IF "
             "(SubjectType IS regularly) "
             "THEN "
             "(Course IS Concurrency)")

RULES.append("IF "
             "(Interactions IS some) "
             "THEN "
             "(Course IS Concurrency)")

RULES.append("IF "
             "(Blackboard IS none) "
             "THEN "
             "(Course IS Concurrency)")

RULES.append("IF "
             "(Recordings IS always) "
             "THEN "
             "(Course IS Concurrency)")

RULES.append("IF "
             "(TeacherAccessibilty IS regularly) "
             "THEN "
             "(Course IS Concurrency)")


# Fuzzy Sets 2
RULES.append("IF "
             "(Evaluation IS written) "
             "THEN "
             "(Course IS FuzzySets2)")

RULES.append("IF "
             "(University IS fribourg) "
             "THEN "
             "(Course IS FuzzySets2)")

RULES.append("IF "
             "(CourseType IS course) "
             "THEN "
             "(Course IS FuzzySets2)")

RULES.append("IF "
             "(Track IS T5) OR "
             "(Track IS T6) "
             "THEN "
             "(Course IS FuzzySets2)")

RULES.append("IF "
             "(Lectures IS regularly) "
             "THEN "
             "(Course IS FuzzySets2)")

RULES.append("IF "
             "(SubjectType IS some) "
             "THEN "
             "(Course IS FuzzySets2)")

RULES.append("IF "
             "(Interactions IS always) "
             "THEN "
             "(Course IS FuzzySets2)")

RULES.append("IF "
             "(Blackboard IS none) "
             "THEN "
             "(Course IS FuzzySets2)")

RULES.append("IF "
             "(Recordings IS none) "
             "THEN "
             "(Course IS FuzzySets2)")

RULES.append("IF "
             "(TeacherAccessibilty IS middle) "
             "THEN "
             "(Course IS FuzzySets2)")

# Test 
RULES.append("IF "
             "(University IS bern) "
             "THEN "
             "(Course IS test)")
