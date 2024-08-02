from utils.prompt_making import make_prompt
from utils.generation import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav

### Use given transcript
make_prompt(name="paimon", audio_prompt_path="paimon_prompt.wav",
                transcript="Just, what was that? Paimon thought we were gonna get eaten.")

# ### Alternatively, use whisper
# make_prompt(name="paimon", audio_prompt_path="paimon_prompt.wav")



# download and load all models
import time

# Record the start time
start_time = time.time()

# Call the function you want to measure
preload_models()

# Calculate and print the elapsed time
elapsed_time = time.time() - start_time
print(f"Time taken to preload models: {elapsed_time} seconds")

start_time = time.time()
text_prompt = """
Hey, Traveler, Listen to this, This machine has taken my voice, and now it can talk just like me!
"""
audio_array = generate_audio(text_prompt, prompt="paimon")
# Calculate and print the elapsed time
elapsed_time = time.time() - start_time
print(f"Time taken for audio array generation models: {elapsed_time} seconds")

start_time = time.time()
write_wav("paimon_cloned.wav", SAMPLE_RATE, audio_array)
# Calculate and print the elapsed time
elapsed_time = time.time() - start_time
print(f"Time taken to write wav file: {elapsed_time} seconds")