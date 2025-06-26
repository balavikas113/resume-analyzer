import argparse
import fitz  # PyMuPDF
import spacy
from textblob import TextBlob

# Load NLP model
nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path):
    with fitz.open(pdf_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    return text

def count_skills(resume_text, skills):
    skill_count = {}
    for skill in skills:
        count = resume_text.lower().count(skill.lower())
        skill_count[skill] = count
    return skill_count

def suggest_improvements(skill_count):
    suggestions = []
    for skill, count in skill_count.items():
        if count == 0:
            suggestions.append(f"Consider adding more emphasis on {skill}.")
    return suggestions

def extract_keywords(text):
    doc = nlp(text)
    keywords = [chunk.text for chunk in doc.noun_chunks if len(chunk.text.split()) > 1]
    return keywords

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

def calculate_resume_score(skill_count, sentiment):
    total_skills = len(skill_count)
    matched_skills = sum(1 for count in skill_count.values() if count > 0)
    skill_score = matched_skills / total_skills
    sentiment_score = (sentiment + 1) / 2  # Normalize between 0 and 1
    return (skill_score * 0.7 + sentiment_score * 0.3) * 100

def analyze_formatting(text):
    issues = []
    if 'References available upon request' not in text:
        issues.append("Consider adding a 'References' section.")
    return issues

def main():
    parser = argparse.ArgumentParser(description="Advanced Resume Analyzer CLI Tool")
    parser.add_argument('resume', type=str, help='Path to the resume PDF')
    args = parser.parse_args()

    resume_text = extract_text_from_pdf(args.resume)
    skills = ['Python', 'SQL', 'Machine Learning', 'Data Analysis','web development','AWS']
    skill_count = count_skills(resume_text, skills)

    print("\nSkill Mentions:")
    for skill, count in skill_count.items():
        print(f"{skill}: {count}")
    
    print("\nSuggestions for Improvement:")
    suggestions = suggest_improvements(skill_count)
    for suggestion in suggestions:
        print(suggestion)

    # Advanced Features
    keywords = extract_keywords(resume_text)
    print("\nExtracted Keywords:", keywords)
    
    sentiment = analyze_sentiment(resume_text)
    print("\nSentiment Score:", sentiment)

    resume_score = calculate_resume_score(skill_count, sentiment)
    print("\nResume Score:", resume_score)

    formatting_issues = analyze_formatting(resume_text)
    if formatting_issues:
        print("\nFormatting Suggestions:")
        for issue in formatting_issues:
            print(issue)

if __name__ == '__main__':
    main()