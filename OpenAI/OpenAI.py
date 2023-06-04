import openai

openai.api_key = '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'  # Replace with your ChatGPT API key

def search_custom_sentence(data):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f" From Virus Total, Analyze the URL report for the URL {data}. Review the Community Score and return it. Also Inform us if a vendor flagged this URL to be malicious ",
        max_tokens=200
    )
    return response.choices[0].text.strip()
