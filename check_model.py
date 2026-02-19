import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

target_model = "gemini-1.5-flash-latest"
found = False
print("Checking for model:", target_model)
try:
    for m in genai.list_models():
        if m.name == f"models/{target_model}" or m.name == target_model:
            found = True
            print(f"FOUND: {m.name}")
            break
    if not found:
        print(f"NOT FOUND: {target_model}")
        print("Available models:")
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(m.name)
except Exception as e:
    print(f"Error: {e}")

with open("model_list.txt", "w", encoding="utf-8") as f:
    found = False
    f.write(f"Checking for model: {target_model}\n")
    try:
        for m in genai.list_models():
            if m.name == f"models/{target_model}" or m.name == target_model:
                found = True
                f.write(f"FOUND: {m.name}\n")
                break
        if not found:
            f.write(f"NOT FOUND: {target_model}\n")
            f.write("Available models:\n")
            for m in genai.list_models():
                if 'generateContent' in m.supported_generation_methods:
                    f.write(f"{m.name}\n")
    except Exception as e:
        f.write(f"Error: {e}\n")
