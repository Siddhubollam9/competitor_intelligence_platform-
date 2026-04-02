import google.generativeai as genai

genai.configure(api_key="AIzaSyBiFecRAjrCjDyFO3d8tKY_vBV2pWYnS2E")

for m in genai.list_models():
    print(m.name)