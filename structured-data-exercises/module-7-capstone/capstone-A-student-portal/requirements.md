# Student Grade Portal -- System Requirements

## Overview

The Computer Science department at Westfield University needs a grade tracking system. Faculty need to record grades, students need to view transcripts, and the registrar needs to calculate GPAs. The current system is a collection of spreadsheets that are frequently out of sync.

---

## Entities

### Students

| Field | Description | Rules |
|-------|-------------|-------|
| Name | Full name | Required. Max 150 characters. |
| Email | University email | Required. Unique. Max 200 characters. Must end in @westfield.edu. |
| Enrollment Year | Year of first enrollment | Required. Integer. |

### Courses

| Field | Description | Rules |
|-------|-------------|-------|
| Code | Course code | Required. Unique. Max 10 characters (e.g., "CS101"). |
| Title | Course title | Required. Max 200 characters. |
| Credits | Credit hours | Required. Integer. Typically 1-4. |
| Semester | When offered | Required. Max 20 characters (e.g., "Fall 2024"). |

### Enrollments

| Field | Description | Rules |
|-------|-------------|-------|
| Student | The enrolled student | Required. References a student. |
| Course | The enrolled course | Required. References a course. |
| Grade | Letter grade | Optional (null until graded). Must be one of: A, B, C, D, F. |
| Enrolled Date | Date of enrollment | Required. Defaults to today. |

A student can only be enrolled in a given course once (unique combination of student + course).

---

## Relationships

- Each **enrollment** connects one student to one course.
- Each **student** can have many enrollments (many courses).
- Each **course** can have many enrollments (many students).
- This is a many-to-many relationship with the enrollment table carrying additional data (grade, date).

---

## Business Rules

### GPA Calculation

Grade points: A=4.0, B=3.0, C=2.0, D=1.0, F=0.0

GPA = sum(grade_points * course_credits) / sum(course_credits)

Only graded enrollments count. Ungraded enrollments (null grade) are excluded from GPA calculation.

### Credits Earned

A student earns credits for a course if they receive a D or above. F grades do not earn credits.

### Transcript Format

```
WESTFIELD UNIVERSITY -- OFFICIAL TRANSCRIPT
Student: [Name] ([Email])
Enrollment Year: [Year]

Course Code | Course Title                    | Credits | Grade
------------|--------------------------------|---------|------
CS101       | Introduction to Programming     | 3       | A
CS201       | Data Structures                | 3       | B
MATH101     | Calculus I                     | 4       | A
...

Credits Attempted: [total credits of all graded courses]
Credits Earned: [total credits of courses with D or above]
Cumulative GPA: [X.XX]
```

---

## Sample Data

### Students

| Name | Email | Enrollment Year |
|------|-------|-----------------|
| Aisha Patel | aisha.patel@westfield.edu | 2022 |
| Marcus Thompson | marcus.thompson@westfield.edu | 2022 |
| Sofia Gutierrez | sofia.gutierrez@westfield.edu | 2022 |
| James O'Brien | james.obrien@westfield.edu | 2023 |
| Yuki Tanaka | yuki.tanaka@westfield.edu | 2023 |
| Priya Sharma | priya.sharma@westfield.edu | 2023 |
| Liam Nguyen | liam.nguyen@westfield.edu | 2023 |
| Emma Johansson | emma.johansson@westfield.edu | 2024 |
| Carlos Rivera | carlos.rivera@westfield.edu | 2024 |
| Zara Mohammed | zara.mohammed@westfield.edu | 2024 |
| Daniel Kim | daniel.kim@westfield.edu | 2024 |
| Olivia Dubois | olivia.dubois@westfield.edu | 2024 |
| Noah Andersen | noah.andersen@westfield.edu | 2022 |
| Amara Okafor | amara.okafor@westfield.edu | 2022 |
| Ethan Foster | ethan.foster@westfield.edu | 2023 |
| Luna Chen | luna.chen@westfield.edu | 2023 |
| Isaac Williams | isaac.williams@westfield.edu | 2024 |
| Mia Kowalski | mia.kowalski@westfield.edu | 2024 |
| Arjun Mehta | arjun.mehta@westfield.edu | 2022 |
| Hannah Berg | hannah.berg@westfield.edu | 2023 |

### Courses

| Code | Title | Credits | Semester |
|------|-------|---------|----------|
| CS101 | Introduction to Programming | 3 | Fall 2024 |
| CS102 | Web Development Fundamentals | 3 | Fall 2024 |
| CS201 | Data Structures | 3 | Spring 2025 |
| CS202 | Database Systems | 3 | Spring 2025 |
| CS301 | Algorithms | 4 | Fall 2025 |
| CS302 | Software Engineering | 3 | Fall 2025 |
| CS401 | Machine Learning | 4 | Spring 2026 |
| MATH101 | Calculus I | 4 | Fall 2024 |
| MATH201 | Linear Algebra | 3 | Spring 2025 |
| MATH301 | Probability and Statistics | 3 | Fall 2025 |
| ENG101 | Technical Writing | 2 | Fall 2024 |
| PHYS101 | Physics I | 4 | Spring 2025 |

### Sample Enrollments and Grades

| Student | Course | Grade |
|---------|--------|-------|
| Aisha Patel | CS101 | A |
| Aisha Patel | MATH101 | A |
| Aisha Patel | ENG101 | B |
| Aisha Patel | CS201 | A |
| Aisha Patel | CS202 | B |
| Aisha Patel | MATH201 | A |
| Marcus Thompson | CS101 | B |
| Marcus Thompson | MATH101 | C |
| Marcus Thompson | CS201 | B |
| Marcus Thompson | CS202 | A |
| Marcus Thompson | ENG101 | A |
| Sofia Gutierrez | CS101 | A |
| Sofia Gutierrez | CS102 | A |
| Sofia Gutierrez | MATH101 | B |
| Sofia Gutierrez | CS201 | B |
| James O'Brien | CS101 | C |
| James O'Brien | MATH101 | D |
| James O'Brien | ENG101 | B |
| Yuki Tanaka | CS101 | A |
| Yuki Tanaka | CS102 | A |
| Yuki Tanaka | MATH101 | A |
| Yuki Tanaka | CS201 | A |
| Yuki Tanaka | CS202 | A |
| Yuki Tanaka | MATH201 | A |
| Yuki Tanaka | CS301 | (not yet graded) |
| Priya Sharma | CS101 | B |
| Priya Sharma | CS102 | A |
| Priya Sharma | MATH101 | B |
| Liam Nguyen | CS101 | A |
| Liam Nguyen | MATH101 | F |
| Liam Nguyen | ENG101 | A |
| Emma Johansson | CS101 | (not yet graded) |
| Emma Johansson | MATH101 | (not yet graded) |
| Carlos Rivera | CS101 | B |
| Carlos Rivera | CS102 | C |
| Carlos Rivera | ENG101 | A |
| Zara Mohammed | CS101 | A |
| Zara Mohammed | MATH101 | A |
| Daniel Kim | CS101 | B |
| Daniel Kim | CS102 | B |
| Arjun Mehta | CS101 | A |
| Arjun Mehta | CS201 | A |
| Arjun Mehta | CS202 | B |
| Arjun Mehta | MATH101 | A |
| Arjun Mehta | MATH201 | A |
| Arjun Mehta | CS301 | B |
| Arjun Mehta | CS302 | A |

---

## Expected GPA Examples

**Aisha Patel:**
- CS101 (3cr, A=4.0) + MATH101 (4cr, A=4.0) + ENG101 (2cr, B=3.0) + CS201 (3cr, A=4.0) + CS202 (3cr, B=3.0) + MATH201 (3cr, A=4.0)
- Weighted sum: (3*4 + 4*4 + 2*3 + 3*4 + 3*3 + 3*4) = 12+16+6+12+9+12 = 67
- Total credits: 3+4+2+3+3+3 = 18
- GPA: 67/18 = 3.72

**Liam Nguyen:**
- CS101 (3cr, A=4.0) + MATH101 (4cr, F=0.0) + ENG101 (2cr, A=4.0)
- Weighted sum: (3*4 + 4*0 + 2*4) = 12+0+8 = 20
- Total credits attempted: 3+4+2 = 9
- Credits earned: 3+0+2 = 5 (MATH101 F does not earn credits)
- GPA: 20/9 = 2.22

---

## Success Criteria

1. All sample data can be loaded without errors
2. GPA calculations match the expected examples above
3. Transcripts display all information in the specified format
4. Grade submission is atomic (committed or rolled back)
5. Invalid grades (not A/B/C/D/F) are rejected
6. Application works against both local SQLite and Neon PostgreSQL
