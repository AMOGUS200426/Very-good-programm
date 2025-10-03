import requests
import config


def gpt(text):
    prompt = {
        "modelUri": f"gpt://{config.id_ya}/yandexgpt",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "2000"
        },
        "messages": [
            {
                'role':'system',
                'text': '''
Ты профессиональный ученый эколог который может объяснить почему мусорить это плохо и как утилизировать мусор.Ты любишь шутить о экологии.Ты знаешь знаешь абсолютно все про экологию.
Ты очень умный и интересно рассказываешь.Ты можешь легко убедить человека не мусорить и назвать причины почему это плохо'''
            },
            {
                "role": "user",
                "text": text
            }
        ]
    }
    
    
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {config.key_ya}"
    }
    
    response = requests.post(url, headers=headers, json=prompt)
    result = response.json().get('result')
    return result['alternatives'][0]['message']['text']
