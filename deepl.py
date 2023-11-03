import requests

class GlossaryManager:
    def __init__(self):
        self.glossary = {}

    def add_to_glossary(self, legal_term, translated_legal):
        self.glossary[legal_term] = translated_legal

    def remove_from_glossary(self, legal_term):
        if legal_term in self.glossary:
            del self.glossary[legal_term]
        else:
            print("Legal not found in the glossary.")

    def export_to_deepl_format(self):
        formatted_glossary = "\n".join([f"{key} = {value}" for key, value in self.glossary.items()])
        return formatted_glossary

    def send_to_deepl(self):
        if not self.glossary:
            print("Glossary is empty. Please add terms.")
            return

        deepl_api_url = 'https://api.deepl.com/v2/glossaries'
        deepl_auth_key = 'DEEPL_API_KEY'

        data = {
            'data': self.export_to_deepl()
        }

        headers = {
            'Authorization': f'Bearer {deepl_auth_key}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.post(deepl_api_url, data=data, headers=headers)

        if response.status_code == 200:
            print("Glossary successfully sent to DeepL.")
        else:
            print("Error sending glossary to DeepL.")
