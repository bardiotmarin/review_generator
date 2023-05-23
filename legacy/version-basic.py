import tkinter as tk
import openai
import pyperclip
import os

os.environ['TK_SILENCE_DEPRECATION'] = '1'

#Initialise the API key
openai.api_key = "YOUR-API-KEY"

#Define the list of available project phaze
PROJECT = ['Single', 'Album', 'EP']

#Define the list of available music type
MUSIC_TYPE = ['Singular', 'Plural','Masculine', 'Feminine','Singular and Masculine','singular and feminine','Plural and Masculine','Plural and Feminine']

#Define the list of available music type
VOCAL_OR_INSTRUMENT = ['NO VOCAL ONLY INSTRUMENTS','Solo And Instrument', 'Only instrument', 'Only vocal', 'Band', 'music record in live','composed with analog instrument','guitar and voice','guitar and bass and drums','guitar and bass and drums and vocal','beatmakers','beatmaker and rapper','Rapper in Featuring','rapper','Dj','Dj Remixer']

#Define the list of available tones
TONES = ['Original', 'Repetitive', 'Deterministic', 'Creative', 'Imaginative', 'Sad', 'Serious', 'Happy', 'Sincere', 'Fearful', 'Hopeful']

#define the list of available themes
THEMES = ['Love','Girl','Relationship', 'Heartbreak', 'Nature', 'Urban Life', 'Racism', 'Politics', 'Religion', 'Family', 'Friendship', 'Success', 'Motivation', 'Inspiration', 'Struggle', 'Hardship', 'Overcoming Obstacles', 'Dreams', 'Fears', 'Society', 'Philosophy', 'Personal Growth', 'Art', 'Culture', 'Freedom', 'Peace', 'War', 'Loss', 'Grief', 'Depression', 'Anger', 'Happiness', 'Joy', 'Satisfaction', 'Empowerment', 'Encouragement', 'Hope', 'Change']

#Define the list of available STYLE
STYLE = ['Bass House','Conscious Hip Hop', 'Contemporary R&B', 'Country', 'Dance', 'Deep-house', 'Downtempo', 'Drill', 'Dubstep', 'East Coast Hip Hop', 'EMD', 'Electro', 'Electronica', 'Exercise', 'Folk', 'Funk', 'Funk R&B', 'Funk Soul', 'Gangsta Rap', 'Garage', 'Gospel', 'Gospel R&B', 'Gospel Soul', 'Golden Age Hip Hop', 'Hard Dance', 'Hardcore', 'Hardcore Rap', 'Hi-NRG / Eurodance', 'Hip Hop Soul', 'Hip-Hop', 'House', 'IDM', 'Industrial', 'Jazz', 'Jackin House', 'Jungle Drum n bass', 'Latin Rap', 'Metal', 'Minimal', 'Motown Soul', 'Neo Soul', 'Northern Soul', 'Old School Hip Hop', 'Old School Rap', 'Pop','Pop And Rap', 'Progressive','Rap Francais', 'Reggae', 'Rock','Rock / Punk', 'Smooth R&B', 'Soul', 'Soul Blues', 'Soul R&B', 'Southern Hip Hop', 'Synthwave', 'Techno', 'Trap', 'Trap Rap', 'Trance', 'Underground Hip Hop', 'Underground Rap', 'West Coast Hip Hop', 'West Coast Rap', 'Classic R&B', 'Classic Soul', 'Philly Soul']

#ajout de la langue
LANGUAGES = ['Albanian', 'Arabic', 'Armenian', 'Awadhi', 'Azerbaijani', 'Bashkir', 'Basque', 'Belarusian', 'Bengali', 'Bhojpuri', 'Bosnian', 'Brazilian Portuguese', 'Bulgarian', 'Cantonese', 'Catalan', 'Chhattisgarhi', 'Chinese', 'Croatian', 'Czech', 'Danish', 'Dogri', 'Dutch', 'English', 'Estonian', 'Faroese', 'Finnish', 'French', 'Galician', 'Georgian', 'German', 'Greek', 'Gujarati', 'Haryanvi', 'Hindi', 'Hungarian', 'Indonesian', 'Irish', 'Italian', 'Japanese', 'Javanese', 'Kannada', 'Kashmiri', 'Kazakh', 'Konkani', 'Korean', 'Kyrgyz', 'Latvian', 'Lithuanian', 'Macedonian', 'Maithili', 'Malay', 'Maltese', 'Mandarin', 'Mandarin Chinese', 'Marathi', 'Marwari', 'Min Nan', 'Moldovan', 'Mongolian', 'Montenegrin', 'Nepali', 'Norwegian', 'Oriya', 'Pashto', 'Farsi', 'Polish', 'Portuguese', 'Punjabi', 'Rajasthani', 'Romanian', 'Russian', 'Sanskrit', 'Santali', 'Serbian', 'Sindhi', 'Sinhala', 'Slovak', 'Slovene', 'Slovenian', 'Ukrainian', 'Urdu', 'Uzbek', 'Vietnamese', 'Welsh', 'Wu']

#Define the function to generate the response
def generate_response(): ton = ton_var.get()
language = language_var.get()
artist = artist_entry.get()
single = single_entry.get()
genre = music_genre_var.get()
project = project_var.get() music_type = music_type_var.get() vocal_or_instrument = vocal_or_instrument_var.get() theme = theme_var.get() engine = "" if language == "Albanian": engine = "text-davinci-003" elif language == "Arabic": engine = "text-davinci-003" elif language == "Azerbaijani": engine = "text-davinci-003" elif language == "Bashkir": engine = "text-davinci-003" elif language == "Basque": engine = "text-davinci-003" elif language == "Belarusian": engine = "text-davinci-003" elif language == "Bengali": engine = "text-davinci-003" elif language == "Bhojpuri": engine = "text-davinci-003" elif language == "Bosnian": engine = "text-davinci-003" elif language == "Brazilian Portuguese": engine = "text-davinci-003" elif language == "Bulgarian": engine = "text-davinci-003" elif language == "Cantonese (Yue)": engine = "text-davinci-003" elif language == "Catalan": engine = "text-davinci-003" elif language == "Chhattisgarhi": engine = "text-davinci-003" elif language == "Chinese": engine = "text-davinci-003" elif language == "Croatian": engine = "text-davinci-003" elif language == "Czech": engine = "text-davinci-003" elif language == "Danish": engine = "text-davinci-003" elif language == "Dogri": engine = "text-davinci-003" elif language == "Dutch": engine = "text-davinci-003" elif language == "English": engine = "text-davinci-003" elif language == "Estonian": engine = "text-davinci-003" elif language == "Faroese": engine = "text-davinci-003" elif language == "Finnish": engine = "text-davinci-003" elif language == "French": engine = "text-davinci-003" elif language == "Galician": engine = "text-davinci-003" elif language == "Georgian": engine = "text-davinci-003" elif language == "German": engine = "text-davinci-003" elif language == "Greek": engine = "text-davinci-003" elif language == "Gujarati": engine = "text-davinci-003" elif language == "Haryanvi": engine = "text-davinci-003" elif language == "Hindi": engine = "text-davinci-003" elif language == "Hungarian": engine = "text-davinci-003" elif language == "Icelandic": engine = "text-davinci-003" elif language == "Indonesian": engine = "text-davinci-003" elif language == "Italian": engine = "text-davinci-003" elif language == "Japanese": engine = "text-davinci-003" elif language == "Javanese": engine = "text-davinci-003" elif language == "Kannada": engine = "text-davinci-003" elif language == "Kazakh": engine = "text-davinci-003" elif language == "Khmer": engine = "text-davinci-003" elif language == "Korean": engine = "text-davinci-003" elif language == "Kurdish": engine = "text-davinci-003" elif language == "Kyrgyz": engine = "text-davinci-003" elif language == "Lao": engine = "text-davinci-003" elif language == "Latin": engine = "text-davinci-003" elif language == "Latvian": engine = "text-davinci-003" elif language == "Lithuanian": engine = "text-davinci-003" elif language == "Macedonian": engine = "text-davinci-003" elif language == "Malagasy": engine = "text-davinci-003" elif language == "Malay": engine = "text-davinci-003" elif language == "Malayalam": engine = "text-davinci-003" elif language == "Maltese": engine = "text-davinci-003" elif language == "Marathi": engine = "text-davinci-003" elif language == "Mongolian": engine = "text-davinci-003" elif language == "Nepali": engine = "text-davinci-003" elif language == "Norwegian": engine = "text-davinci-003" elif language == "Odia": engine = "text-davinci-003" elif language == "Pashto": engine = "text-davinci-003" elif language == "Persian": engine = "text-davinci-003" elif language == "Polish": engine = "text-davinci-003" elif language == "Portuguese": engine = "text-davinci-003" elif language == "Punjabi": engine = "text-davinci-003" elif language == "Romanian": engine = "text-davinci-003" elif language == "Russian": engine = "text-davinci-003" elif language == "Sanskrit": engine = "text-davinci-003" elif language == "Serbian": engine = "text-davinci-003" elif language == "Sinhala": engine = "text-davinci-003" elif language == "Slovak": engine = "text-davinci-003" elif language == "Slovenian": engine = "text-davinci-003" elif language == "Spanish": engine = "text-davinci-003" elif language == "Swahili": engine = "text-davinci-003" elif language == "Swedish": engine = "text-davinci-003" elif language == "Tamil": engine = "text-davinci-003" elif language == "Telugu": engine = "text-davinci-003" elif language == "Thai": engine = "text-davinci-003" elif language == "Turkish": engine = "text-davinci-003" elif language == "Ukrainian": engine = "text-davinci-003" elif language == "Urdu": engine = "text-davinci-003" elif language == "Uzbek": engine = "text-davinci-003" elif language == "Vietnamese": engine = "text-davinci-003" elif language == "Welsh": engine = "text-davinci-003" elif language == "Yiddish": engine = "text-davinci-003" elif language == "Yoruba": engine = "text-davinci-003" elif language == "Zulu": engine = "text-davinci-003" prompt = f"Rédigez une critique musicale objective pour le dernier {project} intitulé '{single}' composé par l'artiste '{artist}' dans le genre {genre}. Le thème tourne autour de '{theme}'. Décrivez les aspects musicaux tels que la production, les arrangements, le mixage et le mastering, en incluant {vocal_or_instrument} (le cas échéant). Analysez les forces et les faiblesses du projet et exprimez votre opinion personnelle sur la valeur musicale de l'album en général, en utilisant un ton {ton} et en {language}. Le format d'écriture doit être sous la forme de {music_type}. Ajoutez des emoji en lien avec le thème musical pour enrichir votre texte." completion = openai.Completion.create( engine=engine, prompt=prompt, max_tokens=2080, n=1, stop=None, temperature=TONES.index(ton) / 10, ) response = completion.choices[0].text response_label.config(text=response)

#Define the function to copy the response to the clipboard
def copy_response(): pyperclip.copy(response_label['text'])

#Create the GUI window
root = tk.Tk() root.title("Music Single Review Generator, le meilleur générateur de critique musicale et de moula") root.configure(bg='#334386')

#Adjust size
root.geometry("800x800")

#Add the option to choose the language of the response
language_label = tk.Label
(root, text="Choisissez la langue de la réponse :", bg='purple', fg='white' , width=80, height=2)
language_label.pack()
language_var = tk.StringVar(value=LANGUAGES[1])
language_scale = tk.OptionMenu
(root, language_var, *LANGUAGES, command=language_var.set)
language_scale.pack()

#add a title to the window information about the artist project title_label_project_information = tk.Label(root, text="🔇⬇️ PROJECT INFORMATIONS ⬇️ 🔇") title_label_project_information.pack(fill=tk.X, padx=10, pady=10)

#add the option to choose the genre of the response
music_genre_label = tk.Label(root, text="Choose the music genre of the artist:")
music_genre_label.pack()
music_genre_var = tk.StringVar(value=STYLE[0])
music_genre_scale = tk.OptionMenu(root, music_genre_var, *STYLE, command=music_genre_var.set)
music_genre_scale.pack()

#Add the mood of the music theme_label = tk.Label(root, text="Choose the music mood for your review:") theme_label.pack() theme_var = tk.StringVar(value=THEMES[0]) theme_scale = tk.OptionMenu(root, theme_var, *THEMES, command=theme_var.set) theme_scale.pack()

Add the option to choose the project of the response
project_label = tk.Label(root, text="is a single/album/ep ?:") project_label.pack() project_var = tk.StringVar(value=PROJECT [0]) project_scale = tk.OptionMenu(root, project_var, *PROJECT, command=project_var.set) project_scale.pack()

Add the title to the window information about the artist
title_label_artists_information = tk.Label(root, text="🔇⬇️ ARTIST INFORMATIONS ⬇️ 🔇") title_label_artists_information.pack(fill=tk.X, padx=10, pady=10)

Add input fields for the artist and single name
artist_label = tk.Label(root, text="Enter artist name:") artist_label.pack() artist_entry = tk.Entry(root, bg='grey') artist_entry.pack()

single_label = tk.Label(root, text="Enter single or album name:", bg='grey', fg='white') single_label.pack() single_entry = tk.Entry(root, bg='grey') single_entry.pack()

Add the option to choose the vocal or instrument
vocal_or_instrument_var = tk.StringVar() vocal_or_instrument_label = tk.Label(root, text="Vocal or Instrument") vocal_or_instrument_label.pack()

vocal_or_instrument_dropdown = tk.OptionMenu(root, vocal_or_instrument_var, *VOCAL_OR_INSTRUMENT) vocal_or_instrument_dropdown.pack()

Add the option to choose the type of music
music_type_label = tk.Label(root, text="Choose The Type Of Bot Written:") music_type_label.pack(fill=tk.X, padx=10, pady=10) music_type_var = tk.StringVar(value=MUSIC_TYPE[0]) music_type_scale = tk.OptionMenu(root, music_type_var, *MUSIC_TYPE, command=music_type_var.set) music_type_scale.pack()

Add the option to choose the tone of the response
ton_label = tk.Label(root, text="Choose the tone of the response:", bg='purple', fg='white') ton_label.pack() ton_var = tk.StringVar(value=TONES[0]) ton_scale = tk.OptionMenu(root, ton_var, *TONES, command=ton_var.set) ton_scale.pack()

Add the generate button
generate_button = tk.Button(root, text="😈Generate Review😈", command=generate_response, bg='purple', fg='blue') generate_button.pack()

Add the label to display the generated response
response_label = tk.Label(root, text="", bg='purple', fg='white', font=("Helvetica" , int(root.winfo_height() * 0.05))) response_label.configure(font=("Helvetica", int(root.winfo_height() * 0.05), "bold")) response_label.pack()

Add the copy button
copy_button = tk.Button(root, text="🎹 Copy to Clipboard 🎹 - 🪕 Copier La réponse 🪕", command=copy_response, bg='purple', fg='green') copy_button.pack()

Run the GUI
root.mainloop()