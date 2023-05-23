import tkinter as tk
import openai
import pyperclip
import os


os.environ['TK_SILENCE_DEPRECATION'] = '1'

# Initialise the API key
openai.api_key = "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"

# Define the list of available project phaze
PROJECT = ['Single', 'Album', 'EP', 'Mixtape', 'Music Demos', 'Compilation', 'Live Album', 'Deluxe Edition', 'Box Set', 'Remix Album', 'Bootlegs']

#List of mixing quality
MIX_QUALITY =['good','bad','average','excellent','amazing','perfect','not good','not bad','not average','not excellent','not amazing','not perfect']

#List of mixing quality trouble
MIX_AMELIORATIONS =['Need More color on instruments','Need more colors on voice','need more color on the fx','too much saturation on the voice record','saturation on the lead voice','need more equalisation on instruments','need more equalisation on bass and sub ','need more equalisation on sub','the guitar quality','sound too much live','all instrument sound very good and the voice too','']

#List of master quality
MASTERING_QUALITY =['good','bad','average','excellent','amazing','perfect','not good','not bad','not average','not excellent','not amazing','not perfect']

# Define the list of available music type
ARTIST_SEXE_GENDER = ['Singular', 'Plural','Masculine', 'Feminine','Singular and Masculine','singular and feminine','Plural and Masculine','Plural and Feminine','lgbtq+','lgbtq+ and masculine','lgbtq+ and feminine','lgbtq+ and singular','lgbtq+ and plural','lgbtq+ and singular and masculine','lgbtq+ and singular and feminine','lgbtq+ and plural and masculine','lgbtq+ and plural and feminine']

# Define the list of available music type
VOCAL_OR_INSTRUMENT = ['women singer on beat','no vocal only instruments','Solo And Instrument', 'Only instrument', 'Only vocal', 'Band', 'music record in live','composed with analog instrument','guitar and voice','guitar and bass and drums','guitar and bass and drums and vocal','beatmakers','beatmaker and rapper','Rapper in Featuring','rapper','Dj','Dj Remixer']

# Define the list of available tones
TONES = ['Original', 'Repetitive', 'Deterministic', 'Creative', 'Imaginative', 'Sad', 'Serious', 'Happy', 'Sincere', 'Fearful', 'Hopeful']

# define the list of available themes
THEMES = ['Adventure', 'Anger', 'Art', 'Art and Freedom', 'Change', 'Comedy', 'Culture', 'Culture and Society', 'Depression', 'Discovery', 'Dreams', 'Encouragement', 'Empowerment', 'Family', 'Family and Tradition','Fell Lost', 'Fear', 'Freedom', 'Freedom and Politics', 'Friendship', 'Friendship and Heartwarming', 'Guerrilla Warfare', 'Girl', 'Grief', 'Heartbreak', 'Heartbreak and Relationships', 'Heartwarming', 'Happiness', 'Happiness and Joy', 'Hardship', 'Hope', 'Hope and Uplifting', 'Hardship and Overcoming Obstacles', 'Inspiration', 'Inspiration and Motivation', 'Joy', 'Lifestyle', 'Lifestyle and Urban Life', 'Loneliness', 'Loneliness and Nostalgia', 'Loss', 'Love', 'Love and Romance','Magie', 'Melancholy', 'Melancholy and Yearning', 'Motivation', 'Nature', 'Nature and Nostalgia', 'Overcoming Obstacles', 'Personal Growth', 'Personal Growth and Success', 'Philosophy', 'Philosophy and Religion', 'Politics', 'Relationship', 'Religion', 'Religion and Philosophy', 'Romance', 'Satisfaction', 'Society', 'Society and Culture', 'Struggle', 'Struggle and Overcoming Obstacles', 'Success', 'Success and Personal Growth','Toxic couple relation', 'Tradition', 'Tragedy', 'Tragedy and War', 'Uplifting', 'Urban Life', 'Urban Life and Lifestyle', 'War', 'Yearning']
# Define the list of available STYLE
STYLE = ['Bass House','fghfg','Conscious Hip Hop', 'Contemporary R&B', 'Country', 'Dance', 'Deep-house', 'Downtempo', 'Drill', 'Dubstep', 'East Coast Hip Hop', 'EMD', 'Electro', 'Electronica', 'Exercise', 'Folk', 'Funk', 'Funk R&B', 'Funk Soul', 'Gangsta Rap', 'Garage', 'Gospel', 'Gospel R&B', 'Gospel Soul', 'Golden Age Hip Hop', 'Hard Dance', 'Hardcore', 'Hardcore Rap', 'Hi-NRG / Eurodance', 'Hip Hop Soul', 'Hip-Hop', 'House', 'IDM', 'Industrial', 'Jazz', 'Jackin House', 'Jungle Drum n bass', 'Latin Rap', 'Metal', 'Minimal', 'Motown Soul', 'Neo Soul', 'Northern Soul', 'Old School Hip Hop', 'Old School Rap', 'Pop','Pop And Rap','Pop & latino', 'Progressive','Rap Francais', 'Reggae', 'Rock','Rock / Punk', 'Smooth R&B', 'Soul', 'Soul Blues', 'Soul R&B', 'Southern Hip Hop', 'Synthwave', 'Techno', 'Trap', 'Trap Rap', 'Trance', 'Underground Hip Hop', 'Underground Rap', 'West Coast Hip Hop', 'West Coast Rap', 'Classic R&B', 'Classic Soul', 'Philly Soul']


#List of available languages
LANGUAGES = ['English', 'French', 'Galician','Italian', 'Spanish', 'Portuguese', 'Dutch', 'Russian', 'Japanese', 'Chinese (Simplified)']

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
    ton = ton_var.get()
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
    engine = ENGINES[language]
    prompt = f"Write an objective music review for the latest {project} titled '{single}' by artist '{artist}' in the {genre} genre. The theme & mood revolves around '{theme}'. Describe the musical aspects such as production, arrangements,audio mix quality :{mix_quality}  ,  mastering :{mastering_quality} , including {vocal_or_instrument} (if applicable) and somes advice to arrange or not the mix :{mix_ameliorations} . Analyze the strengths and weaknesses of the project and express your personal opinion on the overall musical value of the album, using a {ton} tone and in {language}. The writing format should be in the form of a {artist_sexe_gender} genre. Add emoji related to the musical theme to enrich your text."
    completion = openai.Completion.create(
    engine=engine,
    prompt=prompt,
    max_tokens=2448,
    n=1,
    stop=None,
    temperature=TONES.index(ton) / 10,
    )
    response = completion.choices[0].text
    response_label.config(text=response)

# Define the function to copy the response to the clipboard
def copy_response():
    pyperclip.copy(response_label['text'])

    def generate_response(event=None):
        generate_response()

# Create the GUI window
root = tk.Tk()
root.title("Music Single Review Generator, le meilleur générateur de critique musicale et de moula")
root.configure(bg='#334386')

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



# Add the option to choose the type of music
artist_sexe_gender_label = tk.Label(root, text="Choose The Type Of Bot Written:")
artist_sexe_gender_label.pack(fill=tk.X, padx=10, pady=10)

label = tk.Label(root, text="Choose the sexe gender for the style of writing:")
label.pack()

artist_sexe_gender_var = tk.StringVar(value=ARTIST_SEXE_GENDER[0])
artist_sexe_gender_scale = tk.OptionMenu(root, artist_sexe_gender_var, *ARTIST_SEXE_GENDER, command=artist_sexe_gender_var.set)
artist_sexe_gender_scale.pack()

# Add the option to choose the tone of the response
ton_label = tk.Label(root, text="Choose the tone of the response:", bg='purple', fg='white')
ton_label.pack()
ton_var = tk.StringVar(value=TONES[0])
ton_scale = tk.OptionMenu(root, ton_var, *TONES, command=ton_var.set)
ton_scale.pack()



# Add the generate button
generate_button = tk.Button(root, text="😈Generate Review😈", command=generate_response, fg='blue')
generate_button.pack()



# Add the label to display the generated response
response_label = tk.Label(root, text="", bg='purple', fg='white', font=("Helvetica" , int(root.winfo_height() * 0.05)))
response_label.configure(font=("Helvetica", int(root.winfo_height() * 0.05), "bold"))
response_label.pack()



# Add the copy button
copy_button = tk.Button(root, text="🎹 Copy to Clipboard 🎹  -  🪕 Copier La réponse 🪕", command=copy_response, bg='purple', fg='green')
copy_button.pack()

# Run the GUI
root.mainloop()