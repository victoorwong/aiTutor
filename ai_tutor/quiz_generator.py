# Python code for generating quizzes from extracted content

from nlp_utils import summarize_content, generate_questions

def generate_quiz(content: str):
    """Generate a set of quiz questions from the content."""
    summary = summarize_content(content)  # Summarize the content
    questions = generate_questions(summary)  # Generate questions based on the summary
    return questions

