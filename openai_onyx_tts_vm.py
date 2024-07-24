from openai import OpenAI

client = OpenAI()

response = client.audio.speech.create(
    model="tts-1",
    voice="onyx",
    input="<this is where you input your text>",
)

response.stream_to_file("output3.mp3")
