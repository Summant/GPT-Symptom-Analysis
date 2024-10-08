import openai

# API Key
openai.api_key = "API-KEY"

def get_possible_health_issues(symptoms):
    symptoms_str = ', '.join(symptoms)
    
    # prompt to ask GPT-4
    prompt = (f"I have the following symptoms: {symptoms_str}. "
              "Based on these symptoms, list possible diseases or health issues "
              "along with an approximate severity percentage from 0 to 100%.")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use GPT-4 or GPT-3.5-turbo
        messages=[
            {"role": "system", "content": "You are a helpful assistant for health-related queries."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200,
        temperature=0.5
    )

    # Get the response text
    possible_issues = response['choices'][0]['message']['content'].strip()

    return possible_issues

def main():
    # Take input for symptoms from the user
    symptoms = []
    print("Enter your symptoms one by one, type 'done' when finished:")
    
    while True:
        symptom = input("Enter a symptom: ")
        if symptom.lower() == 'done':
            break
        symptoms.append(symptom)
    
    if symptoms:
        # Get possible health issues and severity
        issues = get_possible_health_issues(symptoms)
        print("\nPossible health issues and severity estimates:\n")
        print(issues)
    else:
        print("No symptoms provided.")

if __name__ == "__main__":
    main()
