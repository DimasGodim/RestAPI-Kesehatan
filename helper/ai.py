import openai
from configs import config

client_openai = openai.OpenAI(api_key=config.api_key_openai)

def hitungKlasifikasiTDEE(NilaiTDEE: str, NilaiBMR: str, rating_aktivitas):
    response = client_openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": ""},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
    )
