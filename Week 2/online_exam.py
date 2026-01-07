class Question:
    def __init__(self, q_no, text, category, topic, q_type):
        self.q_no = q_no
        self.text = text
        self.category = category
        self.topic = topic
        self.q_type = q_type

    def __str__(self):
        return f"Q{self.q_no}: {self.text}"

class Exam:
    def __init__(self, exam_name):
        self.exam_name = exam_name
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    # 1. Total number of questions
    def total_questions(self):
        return len(self.questions)

    # 2. Questions by topic
    def questions_by_topic(self, topic):
        return [q for q in self.questions if q.topic == topic]

    # 3. Questions by topic and category
    def questions_by_topic_and_category(self, topic, category):
        return [
            q for q in self.questions
            if q.topic == topic and q.category == category
        ]

# Create exam
exam = Exam("Python Online Test")

# Create questions
q1 = Question(1, "What is Python?", "Basics", "Introduction", "MCQ")
q2 = Question(2, "Explain OOP concepts", "OOP", "Introduction", "Paragraph")
q3 = Question(3, "What is inheritance?", "OOP", "Inheritance", "MCQ")

# Add questions
exam.add_question(q1)
exam.add_question(q2)
exam.add_question(q3)

# Outputs
print("Total questions:", exam.total_questions())

print("\nQuestions under topic 'Introduction':")
for q in exam.questions_by_topic("Introduction"):
    print(q)

print("\nQuestions under topic 'Introduction' and category 'OOP':")
for q in exam.questions_by_topic_and_category("Introduction", "OOP"):
    print(q)

