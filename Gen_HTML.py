import os
from openai import OpenAI

#API CONFIG
OPENAI_API_KEY = "WPROWADŹ SWOJ KLUCZ API"
client = OpenAI(api_key=OPENAI_API_KEY)


def BuildArtykul(system_prompt, user_prompt, article_content):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            # Rola systemu: Określenie wytycznych dla generowania HTML
            {"role": "system", "content": system_prompt},
            # Rola użytkownika: Przekazanie promptu i artykułu
            {"role": "user", "content": user_prompt + "\n" + article_content}
        ]
    )
    
    output = completion.choices[0].message.content
    return output


system_prompt = (
    "You are an expert assistant who specializes in generating well-structured HTML code. "
    "Your task is to take the article content and structure it into HTML format that is easy to read and visually appealing. "
    "Ensure the output is correctly indented and well-organized."
)

user_prompt = (
    "Generate HTML code from the following article_content."
    "The returned code should only contain content to be placed between <body> and </body> tags. Do not include <html>, <head>, or <body> tags. Do not include any CSS or JavaScript."
    "Divide the text into separate sections by topic, with each section containing a header and a paragraph (<p>) of content related to that topic."
    "After each section, add an image placeholder using the format: <figure> <img src='image_placeholder.jpg' alt='Detailed prompt for generating an image in DALL-E related to the paragraph content'> "
    "<figcaption> A specific prompt for DALL-E describing the scene in detail based on the paragraph content. The prompt should describe exactly what the image should depict, including relevant objects, background, lighting, colors, and other visual details.</figcaption> </figure>."
    "Ensure the alt text and <figcaption> are detailed and provide all necessary information for generating the image with DALL-E, based on the content of the paragraph."
    "Additionally, include the following structure in the returned HTML: <header> <h1>Podgląd artykułu</h1> </header> "
    "<div class='container'> Include the generated content for the sections here. </div> "
    "<footer> <p>Oxido Recruitment Task &copy; 2024</p> </footer>"
)

#OpenArticleTXT
with open("artykulbase.txt", "r", encoding="utf-8") as file:
    article_content = file.read()

#RunFunction
html_content = BuildArtykul(system_prompt, user_prompt, article_content)

#Save
with open("artykul.html", "w", encoding="utf-8") as output_file:
    output_file.write(html_content)

#LOG
print("HTML wygenerowany i zapisany w artykul.html")
