# Natural Language Processing utilities (e.g., summarization, question generation)

from transformers import pipeline

summarizer = pipeline("summarization")
question_generator = pipeline("text2text-generation", model="t5-base")

def summarize_content(content: str) -> str:
    """Summarize long content into shorter form."""
    summary = summarizer(content, max_length=200, min_length=50, do_sample=False)
    return summary[0]['summary_text']

def generate_questions(content: str):
    """Generate quiz questions based on summarized content."""
    questions = question_generator(f"generate questions: {content}")
    return questions[0]['generated_text']
