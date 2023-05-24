import tkinter as tk
import openai
import pyperclip
import os
import json
import clipboard

# os.environ['TK_SILENCE_DEPRECATION'] = '1'


# Initialise the API key
with open('api_key.txt', 'r') as file:
    api_key = file.read().strip()

openai.api_key = api_key

#faire un cache avec les réponse pour éviter de les générer à chaque fois
response_cache = {}

# Define the response mode article ou personnel pour le type review directe
# "article" pour le mode article, "personnel" pour le mode personnel -> les user ajoute en du
response_mode = tk.StringVar(value="personelle")  # Valeur par défaut : "ici"


def update_response_mode():
    mode = response_mode.get()


# Load the JSON file
with open('project_data.json') as file:
    data = json.load(file)

# Access the project types list
PROJECT = data['project_types']

#DEFINE THE TONE OF THE ANSWER WITH THE JSON FILE
TONES = data['tones']

#List of mixing quality
MIX_QUALITY =data['mixing_quality']

#List of mixing quality trouble
MIX_AMELIORATIONS =data['mixing_ameliorations']

#List of master quality
MASTERING_QUALITY =data['mastering_quality']

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


#List of available languages
LANGUAGES = data['LANGUAGES']

#Dictionary of engines for each language

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
#Define the function to generate the response

def generate_response():
    prompt = ""
    mode = response_mode
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
    temperature = float(temperature)
    engine = ENGINES[language]

    if mode == "article":
        prompt = f"Your Write under the name of {agency_name}, an objective music review for the latest {project} titled '{single}' by artist '{artist}' in the {genre} genre. The theme & mood revolves around '{theme}'. Describe the musical aspects such as production, arrangements, audio mix quality: {mix_quality}, mastering: {mastering_quality}, including {vocal_or_instrument} (if applicable), and provide advice to enhance the mix: {mix_ameliorations}. Analyze the strengths and weaknesses of the project and express your personal opinion on the overall musical value of the album, using a {tones} tone and in {language}. The writing format should be in the form of a {artist_sexe_gender} genre. Add emojis related to the musical theme to enrich your text."
    elif mode == "personnelle":
        prompt = f"Hey {artist}! I just listened to your latest project '{single}', and how, it's mind-blowing! I'm {agency_name}, and as a music professional, I wanted to give you a friend-to-friend review. The way you nailed the {genre} genre with the theme of '{theme}' is simply amazing. Your production skills and arrangements are top-notch, and the audio mix quality is {mix_quality}. The mastering on this track is {mastering_quality}, making it sound really professional. I must say, I was really impressed with how you incorporated {vocal_or_instrument} into the mix. The flow and energy of the track are on point, capturing the essence of {theme} perfectly. If I had one suggestion, it would be to consider {mix_ameliorations} to take the track to another level. Overall, I have to say, this single is pure genius, my friend! Keep up the great work! 🎵🎶😎"

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

# Define the function to copy the response to the clipboard
def copy_response():
    response = response_label["text"]
    clipboard.copy(response)

  #demande clef api
api_key = input("Enter your API key: ")
with open('api_key.txt', 'w') as file:
    file.write(api_key)

# Create the GUI window
root = tk.Tk()
root.title("Music Single Review Generator, le meilleur générateur de critique musicale et de moula")
root.configure(bg='#212845')

# Adjust size
root.geometry("800x800")

# Add the copy button in case of the bottom button disapear
copy_button = tk.Button(root, text="🎹 Copy to Clipboard 🎹  -  🪕 Copier La réponse 🪕", command=copy_response, bg='white', fg='green')
copy_button.pack()

# Add the option to choose the language of the response
language_label = tk.Label(root, text="Choisissez la langue de la réponse :", bg='purple', fg='white' , width=80, height=2)
language_label.pack()
language_var = tk.StringVar(value=LANGUAGES[1])
language_scale = tk.OptionMenu(root, language_var, *LANGUAGES, command=language_var.set)
language_scale.pack()



def update_response_mode(value):
    global response_mode
    response_mode = value


response_mode_article_button = tk.Radiobutton(root, text="Article", variable=response_mode, value="article", command=update_response_mode)
response_mode_personnel_button = tk.Radiobutton(root, text="Review Personnelle", variable=response_mode, value="personnelle", command=update_response_mode)

response_mode_article_button.pack()
response_mode_personnel_button.pack()



# Add the frame for project information and make it responsive
frame_project_information = tk.Frame(root)
frame_project_information.pack(fill=tk.X, padx=10, pady=10)

#add a title to the window information about the artist project
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

#Add the mood of the music
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
project_var = tk.StringVar(value=PROJECT [0])
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

#add a title to the window information about the artist project
title_label_project_information = tk.Label(root, text="🔇⬇️ MIX AND MASTER INFORMATIONS ⬇️ 🔇")
title_label_project_information.pack(fill=tk.X, padx=10, pady=10)

#Add a frame for the mix quality and mix quality trouble
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
mix_quality_trouble_scale = tk.OptionMenu(frame, mix_quality_trouble_var, *MIX_AMELIORATIONS, command=mix_quality_trouble_var.set)
mix_quality_trouble_scale.pack(side='left')

frame = tk.Frame(root)
frame.pack()
# Add the option to choose the mastering quality
mastering_quality = tk.Label(frame, text="Choose the mastering quality of the artist:")
mastering_quality.pack(side='left')
mastering_quality_var = tk.StringVar(value=MASTERING_QUALITY[0])
mastering_quality_scale = tk.OptionMenu(frame, mastering_quality_var, *MASTERING_QUALITY, command=mastering_quality_var.set)
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


# Add the option to choose the type of music
artist_sexe_gender_label = tk.Label(root, text="Choose The Type Of Bot Written:")
artist_sexe_gender_label.pack(fill=tk.X, padx=10, pady=10)

label = tk.Label(root, text="Choose the sexe gender for the style of writing:")
label.pack()

artist_sexe_gender_var = tk.StringVar(value=ARTIST_SEXE_GENDER[0])
artist_sexe_gender_scale = tk.OptionMenu(root, artist_sexe_gender_var, *ARTIST_SEXE_GENDER, command=artist_sexe_gender_var.set)
artist_sexe_gender_scale.pack()

# Add the option to choose the tone of the response
tones_label = tk.Label(root, text="Choose the tone of the response:", bg='purple', fg='white')
tones_label.pack()
selected_tone_var = tk.StringVar(value=TONES[0])
tones_scale = tk.OptionMenu(root, selected_tone_var, *TONES, command=selected_tone_var.set)
tones_scale.pack()

# Add the option to choose the temperature of the response
temperature_label = tk.Label(root, text="Choose the temperature of the response:", bg='purple', fg='white')
temperature_label.pack()
selected_temperature_var = tk.StringVar(value=list(TEMPERATURE.keys())[0])
temperature_scale = tk.OptionMenu(root, selected_temperature_var, *TEMPERATURE.keys(), command=selected_temperature_var.set)
temperature_scale.pack()



# Add the generate button
generate_button = tk.Button(root, text="😈Generate Review😈", command=generate_response, fg='blue')
generate_button.pack()



# Add the label to display the generated response
response_label = tk.Label(root, text="", bg='purple', fg='white', font=("Helvetica" , int(root.winfo_height() * 0.05)))
response_label.configure(font=("Helvetica", int(root.winfo_height() * 0.05), "bold"))
response_label.pack()



# Add the copy button
copy_button = tk.Button(root, text="🎹 Copy to Clipboard 🎹  -  🪕 Copier La réponse 🪕", command=copy_response, bg='white', fg='green')
copy_button.pack()

# Run the GUI
root.mainloop()