# Capstone A -- Student Grade Portal

**Integration**: Full-stack database application -- modeling, CRUD, relationships, transactions, deployment

## Goal

Build a complete student grade tracking system from scratch. Design the data models, implement CRUD operations, configure relationships, add atomic grade submission, calculate GPAs, and deploy to Neon PostgreSQL. This capstone integrates skills from all six modules.

## What You Have

- `requirements.md` -- Full requirements for the grade tracking system, including entity specifications, relationship rules, business logic for GPA calculation, and sample data (20+ students, 10+ courses).

## Your Tasks

### Step 1: Design the Data Models

Read `requirements.md` and design three SQLAlchemy models:
- **Student** -- id, name, email, enrollment_year
- **Course** -- id, code, title, credits, semester
- **Enrollment** -- id, student_id (FK), course_id (FK), grade (nullable String), enrolled_date

Enrollment is the join table that connects students to courses, and it carries the grade attribute.

### Step 2: Implement CRUD Operations

Write functions to:
- Create students and courses
- Enroll a student in a course
- Submit a grade for an enrollment
- List all enrollments for a student
- List all students in a course

### Step 3: Configure Relationships

Add bidirectional relationships:
- Student.enrollments and Enrollment.student
- Course.enrollments and Enrollment.course
- Add appropriate cascade behavior

### Step 4: Implement Atomic Grade Submission

Write a `submit_grade(session, student_id, course_id, grade)` function that:
- Finds the enrollment record
- Sets the grade
- Commits atomically (grade is either recorded or not)
- Validates the grade value (must be A, B, C, D, or F)
- Returns success/failure

### Step 5: Implement GPA Calculation

Write a `calculate_gpa(session, student_id)` function that:
- Fetches all graded enrollments for the student
- Converts letter grades to points: A=4.0, B=3.0, C=2.0, D=1.0, F=0.0
- Weighs by course credits: GPA = sum(grade_points * credits) / sum(credits)
- Returns the GPA as a float rounded to 2 decimal places

### Step 6: Generate Transcript

Write a `generate_transcript(session, student_id)` function that prints:
- Student name and email
- Each course (code, title, credits, grade)
- Cumulative GPA
- Total credits attempted and earned (D or above)

### Step 7: Deploy to Neon

- Configure environment variables and connection pooling
- Create tables in Neon
- Load the sample data from requirements.md
- Run `generate_transcript()` against the cloud database for at least 3 students

## Expected Results

- Complete working application with models, CRUD, relationships, transactions
- GPA calculation weighted by credits
- Transcript generation showing all courses and cumulative GPA
- Application deployed and working against Neon PostgreSQL
- Sample data loaded and verifiable in Neon SQL Editor

## Reflection

1. Why is Enrollment a separate model instead of a simple many-to-many relationship? What data would you lose without it?
2. How does the atomic grade submission protect data integrity? What could go wrong without transaction safety?
3. What additional features would a real university grade system need that this one does not have?
