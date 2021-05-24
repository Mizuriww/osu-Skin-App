import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import *   

from pathlib import Path

import configparser

import os
import os.path
import shutil

global config_gameplay
global config_design
global config_new

app = tk.Tk()
app.title("osu! Skin Mixer")
app.geometry("390x280")
#app.resizable(width=False, height=False)
#app.iconbitmap('img\osu_ico.ico')

print ("------------------------------------------------------------------")

def browse_skins_folder():
    global path_base
    global osu_skin_directory

    osu_skin_directory = filedialog.askdirectory(parent=app,initialdir="/",title='Please select your osu! skins directory')
    path_base.set(osu_skin_directory)
    print("osu! skins folder: ", osu_skin_directory, "\n------------------------------------------------------------------")

osu_skin_directory = str()
path_base = StringVar()

label_osu_skin_directory = Label(master=app, textvariable=path_base)
label_osu_skin_directory.place(x=110, y=25)

# Browse in files and aske user to select a directory for his osu skins folder
def output_folder():
    button3 = Button(text="Choose your osu! \nskins folder", command=browse_skins_folder)
    button3.place(x=10, y=10, width=100, height=50)

# Browse in files and aske user to select a directory for gameplay part
def browse_gameplay_skin():
    global src_gameplay
    global path_gameplay

    src_gameplay = filedialog.askdirectory(parent=app,initialdir="/",title='Please select your osu! skins directory')

    path_gameplay.set(src_gameplay)
    print("Gameplay skin: ", src_gameplay,"\n------------------------------------------------------------------")
    
path_gameplay = StringVar()
src_gameplay = str()

# Browse in files and aske user to select a directory for design part
def browse_design_skin():
    global src_design
    global path_design

    src_design = filedialog.askdirectory(parent=app,initialdir="/",title='Please select your osu! skins directory')
    path_design.set(src_design)
    print("Design skin: ", src_design,"\n------------------------------------------------------------------")


def browse_button1():
    button1 = Button(text="Gameplay skin", command=browse_gameplay_skin)
    button1.place(x=10, y=70, width=100, height=50)

label_gameplay = Label(master=app,textvariable=path_gameplay)
label_gameplay.place(x=110, y=85)
    
def browse_button2():
    button2 = Button(text="Design Skin", command=browse_design_skin)
    button2.place(x=10, y=130, width=100, height=50)

src_design = str()
path_design = StringVar()
label_design = Label(master=app,textvariable=path_design)
label_design.place(x=110, y=145)

def process_command():
    global new_skin
    global answer_skin_name

    answer_skin_name = ""
    while answer_skin_name == "":
        answer_skin_name = simpledialog.askstring("Input", "How do you want to name the skin?")
    
    new_skin = os.path.join(osu_skin_directory, answer_skin_name)
    print("new skin directory: ", new_skin, "\n-----------------------------------------------------------------")
    os.mkdir(new_skin)
    copy_gameplay()
    copy_design()
    skin_ini_manage_func()
    print ("-----------------------------------------------------------------\nYour skin", answer_skin_name,"is ready! Press Ctrl+Shift+Alt+S in game to reload your skin folder!\n-----------------------------------------------------------------")

new_skin =str()
list_to_ignore = ['cursor', 'default', 'slider','approachcircle', 'hitcircle', 'followpoint', 'reversearrow', 'spinner', 'hit', 'particle', 'lighting', 'taiko', 'pippi', 'comboburst', 'fruit', 'mania', 'target', 'drum', 'soft', 'normal', 'nightcore', 'metronomelow', 'combobreak']
list_2 = ['default']
list_3 = ['score', 'combo']
def copy_gameplay():
    for filename_b in os.listdir(src_gameplay):
        pathfile = (src_gameplay + "/" + filename_b)

        if filename_b == "skin.ini":
            pass

        if filename_b.startswith(tuple(list_to_ignore)):
            shutil.copy(pathfile, new_skin)
            print("Copying:", filename_b, "from gameplay skin")

        if (os.path.isdir(pathfile) == True):
            for filename_b2 in os.listdir(pathfile):
                pathfile2 = (pathfile + "/" + filename_b2)

                if (os.path.isdir(pathfile2) == True):
                    for filename_b3 in os.listdir(pathfile2):
                        pathfile3 = (pathfile2 + "/" + filename_b3)

                        if filename_b3.startswith(tuple(list_2)):
                            shutil.copy(pathfile3, new_skin)
                            print ('Copying:', filename_b3, 'from gameplay skin')

                        else:
                            pass


                elif (os.path.isfile(pathfile2) == True):
                    if filename_b2.startswith(tuple(list_2)):
                        shutil.copy(pathfile2, new_skin)
                        print ('Copying:', filename_b2, 'from gameplay skin')
                    else:
                        pass
                
                else:
                    pass


def copy_design():
    for filename_b in os.listdir(src_design):
        pathfile = (src_design + "/" + filename_b)

        if filename_b == "skin.ini":
            pass

        if filename_b.startswith(tuple(list_to_ignore)):
            pass
        
        else:
            try:
                shutil.copy(pathfile, new_skin)
                print ('Copying:', filename_b,'from design skin')
            except:
                pass

        if (os.path.isdir(pathfile) == True):
            for filename_b2 in os.listdir(pathfile):
                pathfile2 = (pathfile + "/" + filename_b2)

                if (os.path.isdir(pathfile2) == True):
                    for filename_b3 in os.listdir(pathfile2):
                        pathfile3 = (pathfile2 + "/" + filename_b3)

                        if filename_b3.startswith(tuple(list_3)):
                            shutil.copy(pathfile3, new_skin)
                            print ('Copying:', filename_b3, 'from gameplay skin')

                        else:
                            pass


                elif (os.path.isfile(pathfile2) == True):
                    if filename_b2.startswith(tuple(list_3)):
                        shutil.copy(pathfile2, new_skin)
                        print ('Copying:', filename_b2, 'from gameplay skin')

                    else:
                        pass
                    
                else:
                    pass

def process_button():
    button_process = Button(text="Click here\n to process", command=process_command)
    button_process.place(x=10, y=200, width=370, height=70)

label_design = Label(master=app)
label_design.place(x=10, y=90)

config_design = configparser.ConfigParser(allow_no_value=True, comment_prefixes='//', strict=False)
config_gameplay = configparser.ConfigParser(allow_no_value=True, comment_prefixes='//', strict=False)
config_new = configparser.ConfigParser(allow_no_value=True, comment_prefixes='//', strict=False, delimiters=":")

# Keep Case
config_new.optionxform = lambda option : option

def skin_ini_manage_func():
    filename_ini = "skin.ini"
    filepath_new_ini = (new_skin + "/" + filename_ini)
    filepath_gameplay_ini = (src_gameplay + "/" + filename_ini)
    filepath_design_ini = (src_design + "/" + filename_ini)

    f = open(filepath_new_ini, "w", encoding='utf-8') 
    
    #config.read = parse the .ini filez
    config_new.read(filepath_new_ini, encoding='utf-8')

    try:
        config_gameplay.read(filepath_gameplay_ini, encoding= 'utf_8')
    except (UnicodeDecodeError):
        try:
            config_gameplay.read(filepath_gameplay_ini, encoding= 'utf_8_sig')
        except (UnicodeDecodeError):
            try:
                config_gameplay.read(filepath_gameplay_ini, encoding= 'utf_7')
            except (UnicodeDecodeError):
                try:
                    config_gameplay.read(filepath_gameplay_ini, encoding= 'utf_16')
                except (UnicodeDecodeError):
                    try:
                        config_gameplay.read(filepath_gameplay_ini, encoding= 'utf_16_be')
                    except (UnicodeDecodeError):
                        try:
                            config_gameplay.read(filepath_gameplay_ini, encoding= 'utf_16_le')
                        except (UnicodeDecodeError):
                            try:
                                config_gameplay.read(filepath_gameplay_ini, encoding= 'utf_32')
                            except (UnicodeDecodeError):
                                try:
                                    config_gameplay.read(filepath_gameplay_ini, encoding= 'utf_32_be')
                                except (UnicodeDecodeError):
                                    try:
                                        config_gameplay.read(filepath_gameplay_ini, encoding= 'utf_32_le')
                                    except (UnicodeDecodeError):
                                        print ('Send me a message on discord Mizuri#3303')

    try:
        config_design.read(filepath_design_ini, encoding= 'utf_8')
    except (UnicodeDecodeError):
        try:
            config_design.read(filepath_design_ini, encoding= 'utf_8_sig')
        except (UnicodeDecodeError):
            try:
                config_design.read(filepath_design_ini, encoding= 'utf_7')
            except (UnicodeDecodeError):
                try:
                    config_design.read(filepath_design_ini, encoding= 'utf_16')
                except (UnicodeDecodeError):
                    try:
                        config_design.read(filepath_design_ini, encoding= 'utf_16_be')
                    except (UnicodeDecodeError):
                        try:
                            config_design.read(filepath_design_ini, encoding= 'utf_16_le')
                        except (UnicodeDecodeError):
                            try:
                                config_design.read(filepath_design_ini, encoding= 'utf_32')
                            except (UnicodeDecodeError):
                                try:
                                    config_design.read(filepath_design_ini, encoding= 'utf_32_be')
                                except (UnicodeDecodeError):
                                    try:
                                        config_design.read(filepath_design_ini, encoding= 'utf_32_le')
                                    except (UnicodeDecodeError):
                                        print ('Send me a message on discord Mizuri#3303')

    # STARTING

# [General]
    config_new.add_section('General')

    # Name
    try:
        config_new.set('General', 'Name', answer_skin_name)
    except:
        pass
    
    # Author
    try:
        author_d = config_design.get ('General', 'Author')
        author_g = config_gameplay.get ('General', 'Author')
        config_new.set ('General', 'Author', author_d + " and " + author_g)
    except:
        pass

    # Version
    version_g = config_design.get ('General', 'Version')
    config_new.set ('General', 'Version', version_g)

    # CursorExpand
    try:
        cursor_expand_g = config_gameplay.get('General', 'CursorExpand')
        config_new.set ('General', 'CursorExpand', cursor_expand_g)
    except:
        pass

    # CursorCentre
    try:
        cursor_centre_g = config_gameplay.get('General', 'CursorCentre')
        config_new.set('General', 'CursorCentre', cursor_centre_g)
    except:
        pass

    # CursorRotate
    try:
        cursor_rotate_g = config_gameplay.get('General', 'CursorRotate')
        config_new.set('General', 'CursorRotate', cursor_rotate_g)
    except:
        pass

    # CursorTrailRotate
    try:
        cursortrail_rotate_g = config_gameplay.get('General', 'CursorTrailRotate')
        config_new.set('General', 'CursorTrailRotate', cursortrail_rotate_g)
    except:
        pass
    
    # AnimationFramerate
    try:
        animation_framerate_g = config_gameplay.get ('General', 'AnimationFramerate')
        config_new.set ('General', 'AnimationFramerate', animation_framerate_g)
    except:
        pass
        
    # LayeredHitSounds
    try:
        layered_hitsounds_g = config_gameplay.get('General', 'LayeredHitSounds')
        config_new.set('General', 'LayeredHitSounds', layered_hitsounds_g)
    except:
        pass

    # ComboBurstRandom
    try:
        comboburst_random_d = config_design.get('General', 'ComboBurstRandom')
        config_new.set ('General', 'ComboBurstRandom', comboburst_random_d)
    except:
        pass

    # CustomComboBurstSounds
    try:
        custom_comboburst_sounds_g = config_gameplay.get('General', 'CustomComboBurstSounds')
        config_new.set ('General', 'CustomComboBurstSounds', custom_comboburst_sounds_g)
    except:
        pass

    # HitCircleOverlayAboveNumber
    try:
        hitcircle_overlay_above_number_g = config_gameplay.get ('General', 'HitCircleOverlayAboveNumber')
        config_new.set ('General', 'HitCircleOverlayAboveNumber', hitcircle_overlay_above_number_g)
    except:
        pass

    # SliderStyle (Fallback only lol)
    try:
        slider_style_g = config_gameplay.get ('General', 'SliderStyle')
        config_new.set ('General', 'SliderStyle', slider_style_g)
    except:
        pass

    # SliderBallFlip
    try:
        sliderball_flip_g = config_gameplay.get ('General', 'SliderBallFlip')
        config_new.set ('General', 'SliderBallFlip', sliderball_flip_g)
    except:
        pass

    # AllowSliderBallTint
    try:
        allow_sliderball_tint = config_gameplay.get ('General', 'AllowSliderBallTint')
        config_new.set ('General', 'AllowSliderBallTint', allow_sliderball_tint)
    except:
        pass
    
    # SpinnerNoBlink
    try:
        spinner_no_blink_g = config_gameplay.get ('General', 'SpinnerNoBlink')
        config_new.set ('General', 'SpinnerNoBlink', spinner_no_blink_g)
    except:
        pass

    # SpinnerFadePlayfield
    try:
        spinner_fade_playfield = config_gameplay.get ('General', 'SpinnerFadePlayfield')
        config_new.set ('General', 'SpinnerFadePlayfield',  spinner_fade_playfield )
    except:
        pass

    # SpinnerFrequencyModulate
    try:
        spinner_frequency_modulate = config_gameplay.get ('General', 'SpinnerFrequencyModulate')
        config_new.set ('General', 'SpinnerFrequencyModulate',  spinner_frequency_modulate )
    except:
        pass

# [Colours]
    config_new.add_section('Colours')

    # Combo Colours
    # Combo2
    try:
        Combo1 = config_gameplay.get ('Colours', 'Combo1')
        config_new.set ('Colours', 'Combo1', Combo1)
    except:
        pass
    
    # Combo2
    try:
        Combo2 = config_gameplay.get ('Colours', 'Combo2')
        config_new.set ('Colours', 'Combo2', Combo2)
    except:
        pass
    
    # Combo3
    try:
        Combo3 = config_gameplay.get ('Colours', 'Combo3')
        config_new.set ('Colours', 'Combo3', Combo3)
    except:
        pass

    # Combo4
    try:
        Combo4 = config_gameplay.get ('Colours', 'Combo4')
        config_new.set ('Colours', 'Combo4', Combo4)
    except:
        pass

    # Combo5
    try:
        Combo5 = config_gameplay.get ('Colours', 'Combo5')
        config_new.set ('Colours', 'Combo5', Combo5)
    except:
        pass

    # Combo6
    try:
        Combo6 = config_gameplay.get ('Colours', 'Combo6')
        config_new.set ('Colours', 'Combo6', Combo6)
    except:
        pass

    # Combo7
    try:
        Combo7 = config_gameplay.get ('Colours', 'Combo7')
        config_new.set ('Colours', 'Combo7', Combo7)
    except:
        pass

    # Combo8
    try:
        Combo8 = config_gameplay.get ('Colours', 'Combo8')
        config_new.set ('Colours', 'Combo8', Combo8)
    except:
        pass

    # Empty Line
    config_new.set ('Colours', '', None)

    # SongSelectActiveText
    try:
        song_select_active_text_d = config_design.get ('Colours', 'SongSelectActiveText')
        config_new.set ('Colours', 'SongSelectActiveText',  song_select_active_text_d)
    except:
        pass

    # SongSelectInactiveText
    try:
        song_select_inactive_text_d = config_design.get ('Colours', 'SongSelectInactiveText')
        config_new.set ('Colours', 'SongSelectInactiveText',  song_select_inactive_text_d)
    except:
        pass
    
    # MenuGlow
    try:
        menu_glow_d = config_design.get ('Colours', 'MenuGlow')
        config_new.set ('Colours', 'Menuglow', menu_glow_d)
    except:
        pass

    # StarBreakAdditive
    try:
        star_break_additive_d = config_design.get ('Colours', 'StarBreakAdditive')
        config_new.set ('Colours', 'StarBreakAdditive', star_break_additive_d)
    except:
        pass

    # InputOverlayText
    try:
        input_overlay_text_d = config_design.get ('Colours', 'InputOverlayText')
        config_new.set ('Colours', 'InputOverlayText', input_overlay_text_d)
    except:
        pass

    # SliderBall
    try:
        sliderball_g = config_gameplay.get ('Colours', 'SliderBall')
        config_new.set ('Colours', 'SliderBall', sliderball_g)
    except:
        pass

    # SliderTrackOverride
    try:
        slider_track_override_g = config_gameplay.get ('Colours', 'SliderTrackOverride')
        config_new.set ('Colours', 'SliderTrackOverride', slider_track_override_g)
    except:
        pass

    # SliderBorder
    try:
        slider_border_g = config_gameplay.get ('Colours', 'SliderBorder')
        config_new.set ('Colours', 'SliderBorder', slider_border_g)
    except:
        pass

    # SpinnerBackground
    try:
        spinner_background_d = config_design.get ('Colours', 'SpinnerBackground')
        config_new.set ('Colours', 'SpinnerBackground', spinner_background_d)
    except:
        pass

# [Fonts]
    config_new.add_section('Fonts')

    # HitCirclePrefix
        #ignore for now
    
    # HitCircleOverlap
    try:
        hitcircle_overlap_g = config_gameplay.get ('Fonts', 'HitCircleOverlap')
        config_new.set ('Fonts', 'HitCircleOverlap', hitcircle_overlap_g)
    except:
        pass

    # ScorePrefix
    try:
        score_prefix_d = config_design.get ('Fonts', 'ScorePrefix')
        config_new.set ('Fonts', 'ScorePrefix', score_prefix_d)
    except:
        pass

    # ScoreOverlap
    try:
        score_overlap_d = config_design.get ('Fonts', 'ScoreOverlap')
        config_new.set ('Fonts', 'ScoreOverlap', score_overlap_d)
    except:
        pass

    # ComboPrefix
    try:
        combo_prefix_d = config_design.get ('Fonts', 'ComboPrefix')
        config_new.set ('Fonts', 'ComboPrefix', combo_prefix_d)
    except:
        pass

    # ComboOverlap
    try:
        combo_overlap_d = config_design.get ('Fonts', 'ComboOverlap')
        config_new.set ('Fonts', 'ComboOverlap', combo_overlap_d)
    except:
        pass

    # Don't touch VVV
    # Save to the new skin.ini  
    with open(filepath_new_ini, 'w') as configfile:
        config_new.write(configfile)

process_button()
output_folder()
browse_button1()
browse_button2()

app.mainloop()