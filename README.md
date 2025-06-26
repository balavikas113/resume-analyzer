# Resume Analyzer CLI

This is an advanced command-line tool designed to analyze PDF resumes. It evaluates key skill mentions, extracts keywords, performs sentiment analysis, and offers suggestions for improvement, helping candidates optimize their resumes for better job prospects.



## Demo video
https://github.com/user-attachments/assets/d2f1ac9b-1b31-40ab-a3d0-36eeeda63265


## screenshot
![Screenshot 2025-06-26 102904](https://github.com/user-attachments/assets/b8f9ca84-3f22-4cad-bc84-26c6cfc3cbb3)


## Features

- **Text Extraction**: Extracts text content from PDF resumes.
- **Skill Counting**: Identifies and counts key skill mentions like Python, SQL, and Machine Learning.
- **Keyword Extraction**: Extracts important keywords using NLP.
- **Sentiment Analysis**: Analyzes the sentiment of the resume content.
- **Resume Scoring**: Provides a comprehensive score based on skills and sentiment.
- **Formatting Suggestions**: Checks for common formatting issues.










## Usage

1. **Run the Tool:**

    ```bash
    python resume_analyzer.py <path-to-resume.pdf>
    ```

2. **Output:**
   - Displays skill mentions and counts.
   - Provides suggestions for improvement.
   - Extracts and displays keywords.
   - Analyzes and shows sentiment score.
   - Provides a resume score.
   - Offers formatting suggestions.

## Example

```bash
python analyzer.py resume.pdf
