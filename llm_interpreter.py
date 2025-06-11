import google.generativeai as genai

genai.configure(api_key="AIzaSyB9G5PKJdlJc4Y8ILLjvKCb3297Jak9oN0")

def interpret_with_gemini(astro_data, user_query):
    prompt = f"Answer astrologically based on the user's input. Query: {user_query}"
    if astro_data:
        prompt += f"\nAstrological data: {astro_data}"

    try:
        model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Gemini fallback failed: {str(e)}"
