import openai
import tkinter as tk
import os
import json
import pyperclip
import logging
import tkinter.ttk as ttk

os.environ['TK_SILENCE_DEPRECATION'] = '1'

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Initialise the API key
with open('api_key.txt', 'r') as file:
    api_key = file.read().strip()

openai.api_key = api_key

# Load the JSON file
with open('project_data.json') as file:
    data = json.load(file)

# Access the project types list
PROJECT = data['project_types']

# DEFINE THE TONE OF THE ANSWER WITH THE JSON FILE
TONES = data['tones']

# List of mixing quality
MIX_QUALITY = data['mixing_quality']

# List of mixing quality trouble
MIX_AMELIORATIONS = data['mixing_ameliorations']

# List of master quality
MASTERING_QUALITY = data['mastering_quality']

# Define the list of available music type
ARTIST_SEXE_GENDER = data['ARTIST_SEXE_GENDER']

# Define the list of available music type
VOCAL_OR_INSTRUMENT = data['VOCAL_OR_INSTRUMENT']

# Define the list of available themes
THEMES = data['THEMES']

# Define the list of available STYLE
STYLE = data['STYLE']

# List of available languages
LANGUAGES = data['LANGUAGES']

# Dictionary of engines for each language
ENGINES = {
    'English': "text-davinci-003",
    'French': "text-davinci-003",
    'Galician': "text-davinci-003",
    'Italian': "text-davinci-003",
    'Spanish': "text-davinci-003",
    'Portuguese': "text-davinci-003",
    'Dutch': "text-davinci-003",
    'Russian': "text-davinci-003",
    'Japanese': "text-davinci-003",
    'Chinese (Simplified)': "text-davinci-003",
}

# Define the function to generate the response
def generate_response():
    response_label.config(text="")  # Réinitialiser l'étiquette de réponse
    prompt = ""
    prompt_type = prompt_type_var.get()
    response_mode_var = tk.StringVar()
    mode = response_mode_var.get()
    tones = selected_tone_var.get()
    temperature = float(selected_temperature_var.get())
    language = language_var.get()
    artist = artist_entry.get()
    single = single_entry.get()
    genre = music_genre_var.get()
    project = project_var.get()
    artist_sexe_gender = artist_sexe_gender_var.get()
    vocal_or_instrument = vocal_or_instrument_var.get()
    theme = theme_var.get()
    mix_quality = mix_quality_var.get()
    mix_ameliorations = mix_quality_trouble_var.get()
    mastering_quality = mastering_quality_var.get()
    agency_name = agency_entry.get()
    engine = ENGINES[language]

    try:
        if prompt_type == "article":
            # Code pour le mode "article"
            prompt = f"Your Write under the name of {agency_name}, an objective music review for the latest {project} titled '{single}' by artist '{artist}' in the {genre} genre. The theme & mood revolves around '{theme}'. Describe the musical aspects such as production, arrangements,audio mix quality :{mix_quality}  ,  mastering :{mastering_quality} , including {vocal_or_instrument} (if applicable) and somes advice to arrange or not the mix :{mix_ameliorations} . Analyze the strengths and weaknesses of the project and express your personal opinion on the overall musical value of the album, using a {tones} tone and in {language}. The writing format should be in the form of a {artist_sexe_gender} genre. Add emoji related to the musical theme to enrich your text."
        elif prompt_type == "personnel":
            # Code pour le mode "personnel"
            prompt = f"Hey {artist}! Just listened to your latest project '{single}' and it's mind-blowing! As a music professional, wanted to give you a friend-to-friend review. Nailed the {genre} genre with the theme of '{theme}' - simply amazing. Production skills and arrangements are top-notch, and the audio mix quality is {mix_quality}. The mastering on this track is {mastering_quality}, making it sound really professional. Impressed with how you incorporated {vocal_or_instrument} into the mix. The flow and energy of the track are on point, capturing the essence of {theme} perfectly. If I had one suggestion, it would be to consider {mix_ameliorations} to take the track to another level. Overall, gotta say, this single is pure genius! Keep up the great work! 🎵🎶😎"
        else:
            logging.error("Invalid response mode")

        # Utiliser la variable prompt mise à jour pour générer la réponse avec OpenAI API
        completion = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            max_tokens=2448,
            n=1,
            stop=None,
            temperature=temperature,
        )
        response = completion.choices[0].text
        response_label.config(text=response)

        logging.info("Response generated successfully!")
    except Exception as e:
        logging.error("Failed to generate response:", str(e))

# Create the main window
window = tk.Tk()
window.title("Music Review Generator")
window.geometry("800x600")

# Create the prompt type selection label
prompt_type_label = tk.Label(window, text="Prompt Type:")
prompt_type_label.pack()

# Create the prompt type dropdown
prompt_type_var = tk.StringVar()
prompt_type_dropdown = ttk.Combobox(window, textvariable=prompt_type_var)
prompt_type_dropdown['values'] = ('article', 'personnel')
prompt_type_dropdown.current(0)
prompt_type_dropdown.pack()

# Create the artist entry
artist_label = tk.Label(window, text="Artist Name:")
artist_label.pack()
artist_entry = tk.Entry(window)
artist_entry.pack()

# Create the single entry
single_label = tk.Label(window, text="Single Title:")
single_label.pack()
single_entry = tk.Entry(window)
single_entry.pack()

# Create the genre selection dropdown
music_genre_label = tk.Label(window, text="Music Genre:")
music_genre_label.pack()
music_genre_var = tk.StringVar()
music_genre_dropdown = ttk.Combobox(window, textvariable=music_genre_var)
music_genre_dropdown['values'] = ('Pop', 'Rock', 'Hip-Hop', 'Electronic', 'R&B', 'Country', 'Jazz', 'Classical', 'Other')
music_genre_dropdown.current(0)
music_genre_dropdown.pack()

# Create the project type selection dropdown
project_label = tk.Label(window, text="Project Type:")
project_label.pack()
project_var = tk.StringVar()
project_dropdown = ttk.Combobox(window, textvariable=project_var)
project_dropdown['values'] = PROJECT
project_dropdown.current(0)
project_dropdown.pack()

# Create the artist gender/sex selection dropdown
artist_sexe_gender_label = tk.Label(window, text="Artist Gender/Sex:")
artist_sexe_gender_label.pack()
artist_sexe_gender_var = tk.StringVar()
artist_sexe_gender_dropdown = ttk.Combobox(window, textvariable=artist_sexe_gender_var)
artist_sexe_gender_dropdown['values'] = ARTIST_SEXE_GENDER
artist_sexe_gender_dropdown.current(0)
artist_sexe_gender_dropdown.pack()

# Create the vocal/instrument selection dropdown
vocal_or_instrument_label = tk.Label(window, text="Vocal or Instrument:")
vocal_or_instrument_label.pack()
vocal_or_instrument_var = tk.StringVar()
vocal_or_instrument_dropdown = ttk.Combobox(window, textvariable=vocal_or_instrument_var)
vocal_or_instrument_dropdown['values'] = VOCAL_OR_INSTRUMENT
vocal_or_instrument_dropdown.current(0)
vocal_or_instrument_dropdown.pack()

# Create the theme entry
theme_label = tk.Label(window, text="Theme:")
theme_label.pack()
theme_var = tk.StringVar()
theme_entry = tk.Entry(window, textvariable=theme_var)
theme_entry.pack()

# Create the mixing quality selection dropdown
mix_quality_label = tk.Label(window, text="Mixing Quality:")
mix_quality_label.pack()
mix_quality_var = tk.StringVar()
mix_quality_dropdown = ttk.Combobox(window, textvariable=mix_quality_var)
mix_quality_dropdown['values'] = MIX_QUALITY
mix_quality_dropdown.current(0)
mix_quality_dropdown.pack()

# Create the mixing quality trouble selection dropdown
mix_quality_trouble_label = tk.Label(window, text="Mixing Improvements:")
mix_quality_trouble_label.pack()
mix_quality_trouble_var = tk.StringVar()
mix_quality_trouble_dropdown = ttk.Combobox(window, textvariable=mix_quality_trouble_var)
mix_quality_trouble_dropdown['values'] = MIX_AMELIORATIONS
mix_quality_trouble_dropdown.current(0)
mix_quality_trouble_dropdown.pack()

# Create the mastering quality selection dropdown
mastering_quality_label = tk.Label(window, text="Mastering Quality:")
mastering_quality_label.pack()
mastering_quality_var = tk.StringVar()
mastering_quality_dropdown = ttk.Combobox(window, textvariable=mastering_quality_var)
mastering_quality_dropdown['values'] = MASTERING_QUALITY
mastering_quality_dropdown.current(0)
mastering_quality_dropdown.pack()

# Create the agency name entry
agency_label = tk.Label(window, text="Agency Name:")
agency_label.pack()
agency_entry = tk.Entry(window)
agency_entry.pack()

# Create the selected tone selection dropdown
selected_tone_label = tk.Label(window, text="Selected Tone:")
selected_tone_label.pack()
selected_tone_var = tk.StringVar()
selected_tone_dropdown = ttk.Combobox(window, textvariable=selected_tone_var)
selected_tone_dropdown['values'] = TONES
selected_tone_dropdown.current(0)
selected_tone_dropdown.pack()

# Create the selected temperature entry
selected_temperature_label = tk.Label(window, text="Selected Temperature:")
selected_temperature_label.pack()
selected_temperature_var = tk.StringVar()
selected_temperature_entry = tk.Entry(window, textvariable=selected_temperature_var)
selected_temperature_entry.pack()

# Create the language selection dropdown
language_label = tk.Label(window, text="Language:")
language_label.pack()
language_var = tk.StringVar()
language_dropdown = ttk.Combobox(window, textvariable=language_var)
language_dropdown['values'] = LANGUAGES
language_dropdown.current(0)
language_dropdown.pack()

# Create the generate button
generate_button = tk.Button(window, text="Generate", command=generate_response)
generate_button.pack()

# Create the response label
response_label = tk.Label(window, text="")
response_label.pack()

# Run the main window loop
window.mainloop()
