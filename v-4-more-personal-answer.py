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

# Define the list of available tones
TEMPERATURE = {
    0.2: "plus précises, plus conservatrices",
    0.5: "un bon équilibre entre créativité et cohérence",
    0.8: "créatives mais potentiellement moins cohérentes"
}
# define the list of available themes
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
            # Mode de réponse invalide
            logging.error("Invalid response mode")

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
        logging.exception("An error occurred while generating the response.")
        response_label.config(text="An error occurred while generating the response.")



# Créer la fenêtre racine
root = tk.Tk()
root.title("Music Single Review Generator, le meilleur générateur de critique musicale et de moula")
root.configure(bg='#212845')




# Define the function to copy the response to the clipboard
def copy_response():
    pyperclip.copy(response_label['text'])



# demande clef api
with open('api_key.txt', 'w') as file:
    file.write(api_key)

# Add the copy button in case of the bottom button disapear
copy_button = tk.Button(root, text="🎹 Copy to Clipboard 🎹  -  🪕 Copier La réponse 🪕", command=copy_response, bg='white',
                        fg='green')
copy_button.pack()

# Add the option to choose the language of the response
language_label = tk.Label(root, text="Choisissez la langue de la réponse :", bg='purple', fg='white', width=80,
                          height=2)
language_label.pack()
language_var = tk.StringVar(value=LANGUAGES[0])
language_scale = tk.OptionMenu(root, language_var, *LANGUAGES)
language_scale.pack()


def update_response_mode_var(value, response_mode_var=None):
    response_mode_var.set(value)
    # Reset the response label
    response_mode_label.config(text="")

# Define the list of available prompt types
PROMPT_TYPES = ['Article', 'Direct Response']

# Add the option to choose the prompt type
prompt_type_label = tk.Label(root, text="Choose the prompt type:")
prompt_type_label.pack()

prompt_type_var = tk.StringVar(value=PROMPT_TYPES[0])
prompt_type_scale = tk.OptionMenu(root, prompt_type_var, *PROMPT_TYPES, command=prompt_type_var.set)
prompt_type_scale.pack()



# Add the frame for project information and make it responsive
frame_project_information = tk.Frame(root)
frame_project_information.pack(fill=tk.X, padx=10, pady=10)

# add a title to the window information about the artist project
title_label_project_information = tk.Label(root, text="🔇⬇️ PROJECT INFORMATIONS ⬇️ 🔇")
title_label_project_information.pack(fill=tk.X, padx=10, pady=10)

# Add a frame for project informations
frame = tk.Frame(root)
frame.pack()

# Add the option to choose the genre of the response
music_genre_label = tk.Label(frame, text="Choose the music genre of the artist:")
music_genre_label.pack(side='left', padx=10)
music_genre_var = tk.StringVar(value=STYLE[0])
music_genre_scale = tk.OptionMenu(frame, music_genre_var, *STYLE, command=music_genre_var.set)
music_genre_scale.pack(side='left', padx=10, pady=10)

# Add a frame for project informations
frame = tk.Frame(root)
frame.pack()

# Add the mood of the music
theme_label = tk.Label(frame, text="Choose the music mood/Theme for this song:")
theme_label.pack(side='left', padx=10)
theme_var = tk.StringVar(value=THEMES[0])
theme_scale = tk.OptionMenu(frame, theme_var, *THEMES, command=theme_var.set)
theme_scale.pack(side='left', padx=10)

# Add a frame for project informations
frame = tk.Frame(root)
frame.pack()
# Add the option to choose the project of the response
project_label = tk.Label(frame, text="is a single/album/ep ?:")
project_label.pack(side='left', padx=10)
project_var = tk.StringVar(value=PROJECT[0])
project_scale = tk.OptionMenu(frame, project_var, *PROJECT, command=project_var.set)
project_scale.pack(side='left', padx=10)

# Add a frame for project informations
frame = tk.Frame(root)
frame.pack()
# Add the option to choose the vocal or instrument
vocal_or_instrument_var = tk.StringVar()
vocal_or_instrument_label = tk.Label(frame, text="Vocal or Instrument")
vocal_or_instrument_label.pack(side='left', padx=10)

vocal_or_instrument_dropdown = tk.OptionMenu(frame, vocal_or_instrument_var, *VOCAL_OR_INSTRUMENT)
vocal_or_instrument_dropdown.pack(side='left', padx=10)

# add a title to the window information about the artist project
title_label_project_information = tk.Label(root, text="🔇⬇️ MIX AND MASTER INFORMATIONS ⬇️ 🔇")
title_label_project_information.pack(fill=tk.X, padx=10, pady=10)

# Add a frame for the mix quality and mix quality trouble
frame = tk.Frame(root)
frame.pack()

# Add the option to choose the mix quality
mix_quality_label = tk.Label(frame, text="Enter mix quality:")
mix_quality_label.pack(side='left')
mix_quality_var = tk.StringVar(value=MIX_QUALITY[0])
mix_quality_scale = tk.OptionMenu(frame, mix_quality_var, *MIX_QUALITY, command=mix_quality_var.set)
mix_quality_scale.pack(side='left')

frame = tk.Frame(root)
frame.pack()
# Add the option to choose the mix quality ameliorations
mix_quality_trouble = tk.Label(frame, text="Choose the mix quality ameliorations of the artist:")
mix_quality_trouble.pack(side='left')
mix_quality_trouble_var = tk.StringVar(value=MIX_AMELIORATIONS[0])
mix_quality_trouble_scale = tk.OptionMenu(frame, mix_quality_trouble_var, *MIX_AMELIORATIONS,
                                          command=mix_quality_trouble_var.set)
mix_quality_trouble_scale.pack(side='left')

frame = tk.Frame(root)
frame.pack()
# Add the option to choose the mastering quality
mastering_quality = tk.Label(frame, text="Choose the mastering quality of the artist:")
mastering_quality.pack(side='left')
mastering_quality_var = tk.StringVar(value=MASTERING_QUALITY[0])
mastering_quality_scale = tk.OptionMenu(frame, mastering_quality_var, *MASTERING_QUALITY,
                                        command=mastering_quality_var.set)
mastering_quality_scale.pack(side='left')

# Add the title to the window information about the artist
title_label_artists_information = tk.Label(root, text="🔇⬇️ ARTIST INFORMATIONS ⬇️ 🔇")
title_label_artists_information.pack(fill=tk.X, padx=10, pady=10)

# Add a frame for the artist and single name
frame = tk.Frame(root)
frame.pack()

# Add input fields for the artist and single name
artist_label = tk.Label(frame, text="Enter artist name:")
artist_label.pack(side='left', )
artist_entry = tk.Entry(frame, bg='grey')
artist_entry.pack(side='left', padx=10)

single_label = tk.Label(frame, text="Enter single or album name:", fg='white')
single_label.pack(side='left', padx=10)
single_entry = tk.Entry(frame, bg='grey')
single_entry.pack(side='left', padx=10)

# Add a label for the agency name
agency_label = tk.Label(root, text="Enter your agency name:")
agency_label.pack()

# Add an entry field for the agency name
agency_entry = tk.Entry(root, bg='grey')
agency_entry.pack()

# Création d'un conteneur pour les éléments côte à côte avec de l'espace entre eux
container = tk.Frame(root)
container.pack()

# Ajout de l'option pour choisir le type de musique
artist_sexe_gender_label = tk.Label(container, text="Choose The Type Of Bot Written:")
artist_sexe_gender_label.pack(side=tk.LEFT, padx=(10, 20), pady=10)

artist_sexe_gender_var = tk.StringVar(value=ARTIST_SEXE_GENDER[0])
artist_sexe_gender_scale = tk.OptionMenu(container, artist_sexe_gender_var, *ARTIST_SEXE_GENDER,
                                         command=artist_sexe_gender_var.set)
artist_sexe_gender_scale.pack(side=tk.LEFT)

# Ajout d'une barre de séparation
separator = tk.ttk.Separator(container, orient=tk.VERTICAL)
separator.pack(side=tk.LEFT, padx=20, fill=tk.Y)

# Ajout de l'option pour choisir le ton de la réponse
tones_label = tk.Label(container, text="Choose the tone of the response:", bg='purple', fg='white')
tones_label.pack(side=tk.LEFT, padx=(20, 10), pady=10)

selected_tone_var = tk.StringVar(value=TONES[0])
tones_scale = tk.OptionMenu(container, selected_tone_var, *TONES, command=selected_tone_var.set)
tones_scale.pack(side=tk.LEFT)

# Ajout d'une autre barre de séparation
separator2 = tk.ttk.Separator(container, orient=tk.VERTICAL)
separator2.pack(side=tk.LEFT, padx=20, fill=tk.Y)

# Ajout de l'option pour choisir la température de la réponse
temperature_label = tk.Label(container, text="Choose the temperature of the response:", bg='purple', fg='white')
temperature_label.pack(side=tk.LEFT, padx=(20, 10), pady=10)

selected_temperature_var = tk.StringVar(value=list(TEMPERATURE.keys())[0])
temperature_scale = tk.OptionMenu(container, selected_temperature_var, *TEMPERATURE.keys(),
                                  command=selected_temperature_var.set)
temperature_scale.pack(side=tk.LEFT)

# Add the generate button
generate_button = tk.Button(root, text="😈Generate Review😈", command=generate_response, fg='blue')
generate_button.pack()



response_label = tk.Label(root, wraplength=800, bg='white', fg='black')
response_label.pack(pady=20)
response_label.pack()
# Add the copy button
copy_button = tk.Button(root, text="🎹 Copy to Clipboard 🎹  -  🪕 Copier La réponse 🪕", command=copy_response, bg='white',
                        fg='green')
copy_button.pack()

root.update_idletasks()
root.geometry(f"{root.winfo_width()}x{root.winfo_height()}")
root.minsize(root.winfo_width(), root.winfo_height())


# Run the GUI
root.mainloop()