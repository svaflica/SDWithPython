import curses
import time 
from pygame import mixer
from faker import Faker
import sys

fake = Faker(locale='en')
text = fake.paragraph(nb_sentences=5)
errors = 0

def speed(stdscr):
    global text
    global errors

    
    mixer.init() 
    
    
    typed_text = []
    wpm = 0
    start_time = time.time()
    errors = 0
    curses.flushinp()

    while True:
        if not mixer.music.get_busy():
            mixer.music.load('src/shit_music.mp3')
            mixer.music.play()
        seconds_passed = max((time.time() - start_time), 1)
        cpm = int(len(typed_text) / (seconds_passed/60))
        wpm = round((cpm/5), 2)

        stdscr.clear()
        show_speed(stdscr, text, typed_text, cpm, wpm, seconds_passed)
        stdscr.refresh()

        if "".join(typed_text) == text:
            stdscr.nodelay(False)
            break
        
        try:
            stdscr.timeout(1)
            keyPress = stdscr.getkey()
        except:
            continue


        if len(typed_text) == len(text):
            break

        if ord(keyPress) == 27:
            walk_channel = mixer.Channel(2)
            walk_sound = mixer.Sound("src/snd_player_die.wav")
            walk_channel.play(walk_sound)
            time.sleep(2)
            sys.exit()
        
        if keyPress in ("KEY_BACKSPACE", '\b', '\x7f'):
            if len(typed_text) > 0:
                typed_text.pop()

        elif len(typed_text) < len(text):
            if keyPress != text[len(typed_text)]:
                walk_channel = mixer.Channel(2)
                walk_sound = mixer.Sound("src/ouch.wav")
                walk_channel.play(walk_sound)
                errors += 1
            typed_text.append(keyPress)


def show_speed(stdscr, text, typed_text, cpm, wpm, seconds_passed):
    global errors
    
    stdscr.addstr(6, 0, text)
    stdscr.addstr(0, 0, f"Typing Speed in words per minute (wpm): {wpm}")
    stdscr.addstr(1, 0, f"Typing Speed in characters per minute : {cpm}")
    stdscr.addstr(2, 0, f"Seconds elapsed : {round(seconds_passed, 2)} seconds") 
    stdscr.addstr(3, 0, f"Errors count : {errors}") 


    for index, letter in enumerate(typed_text):
        correct_char = text[index]
        if letter != correct_char:
            text_color = curses.color_pair(2)
        else:
            text_color = curses.color_pair(1)

        stdscr.addstr(6 + index // 123, index % 123, letter, text_color)
    



def main(stdscr):
    global text
    curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
    
    while True:
        speed(stdscr)

        #color blinking
        for i in range(0,2):
            stdscr.addstr(6, 0, text, curses.color_pair(2))
            stdscr.refresh()
            curses.napms(400)
            stdscr.addstr(6, 0, text, curses.color_pair(4))
            stdscr.refresh()
            curses.napms(400)
            stdscr.addstr(6, 0, text, curses.color_pair(1))
            stdscr.refresh()
            curses.napms(400)


        stdscr.addstr(4, 0, "Yay!! Press any key to continue. \nTo exit press the escape button.")

        curses.flushinp()
        keyPress = stdscr.getkey()
        
        #break if esc key is pressed
        stdscr.timeout(1000)
        if ord(keyPress) == 27:
            walk_channel = mixer.Channel(2)
            walk_sound = mixer.Sound("src/snd_player_die.wav")
            walk_channel.play(walk_sound)
            time.sleep(2)
            break

        text = fake.paragraph(nb_sentences=5)
curses.wrapper(main)