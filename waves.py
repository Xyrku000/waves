# import statements
import wave  # wave module allows Python to read the audio files
import winsound  # sound module allows Python to play audio files
from collections import deque  # stack module
import heapq  # heap module

# audio file set-up
myVoice = "empty.wav"  # an empty audio file
dragonVoice = "empty2.wav"  # another empty audio file
myArray = bytearray()  # the bytearray version of myVoice; data structure 1: bytearray
dragonArray = bytearray()  # the bytearray version of dragonVoice
mySound = wave.open(myVoice, 'wb')  # opened myVoice with write permissions
mySound.setnchannels(2)  # sets required default parameters
mySound.setsampwidth(2)  # " "
mySound.setframerate(44100)  # " "
dragonSound = wave.open(myVoice, 'wb')  # opened dragonVoice with write permissions
dragonSound.setnchannels(2)  # sets required default parameters
dragonSound.setsampwidth(2)  # " "
dragonSound.setframerate(44100)  # " "

# Using bytearrays to construct unique sounds
print("Welcome to the Chicane Facility, Clara.")  # You have entered the Facility
myFirstName = input("Clara, what is your real first name?:")  # The Dragon calls to you from a distance.
myLastName = input("And what is your real last name?:")  # It is ascertaining your Signal.
encodedFirstName = bytes(myFirstName, encoding='utf8')
encodedLastName = bytes(myLastName, encoding='utf8')  # Note: 'Clara' is just a nickname for the user (used below)
for i in range(0, 10000):  # iterates to 10000 (length of sound)
    byteFirst = bytearray(encodedFirstName).hex()  # converts bytes into array and in hex format
    byteLast = bytearray(encodedLastName).hex()  # " "
    byteDragon = byteFirst + byteLast  # combines byteFirst and byteLast to create 2-digit hex variable
    myArray.extend(bytearray.fromhex(byteDragon))  # fills in myVoice array with byteName credentials
mySound.writeframes(myArray)  # writes filled-in myVoice array into mySound


def myVoicePlay(numTimes):  # plays myVoice
    for j in range(numTimes):  # parameter 'numTimes' says how many times to play
        winsound.PlaySound(myVoice, winsound.SND_ALIAS)  # plays myVoice (with mySound filled in)


myVoicePlay(2)  # plays myVoice twice
print("The sound you just heard is your audio signal. Keep it with you.")

Answer1 = input("Say your first name to advance to the next room:")
while True:
    if Answer1 == myFirstName:  # player must type in their name
        myVoicePlay(2)  # Such a powerful signal is telekinetic and takes Clara to the next room
        break

dragonName = bytes("THE_GREAT_CHICANE_DRAGON", encoding='utf8')  # constructs dragon sound
for i in range(0, 10000):  # fills dragonArray
    byteDragon = bytearray(dragonName).hex()
    dragonArray.extend(bytearray.fromhex(byteDragon))
dragonSound.writeframes(dragonArray)  # writes filled-in dragonArray to create dragonSound


def dragonVoicePlay(numTimes):  # counterpart to myVoicePlay
    for k in range(numTimes):
        winsound.PlaySound(dragonVoice, winsound.SND_ALIAS)


print("Something whispers in the dark.")
dragonVoicePlay(2)  # first non-user sound

Answer2 = input("'Yes' or 'No': Was that last sound the sound Clara's own footprints?:")
if Answer2 != "No":  # Clara dies if she does not believe the signal is not hers.
    dragonVoicePlay(3)
    print("the dragon of Chicane...")
    print("...it has devoured Clara!")
    exit()  # when Clara dies, the dragonVoice dissolves her Signal in three waves.
print("Clara has escaped from the Dragon of Chicane for now. She advances to a closet.")
SoundCounter = deque()  # data structure 2: stack
print("The dragon's signal mimics Clara's voice. Listen closely.")


def closetSequence():  # makes sure Answer3 is an integer
    try:  # tries first to find an integer
        answerFor3 = int(input("Now how many seconds will Clara stay in the closet?:"))
        return answerFor3
    except:  # if not an integer, except clause is triggered
        closetSequence()  # runs again until input is an integer


while True:  # Closet sequence loops until she leaves.
    Answer3 = closetSequence()  # finds Answer3
    for ll in range(0, Answer3):
        if Answer3 % 2 == 0:
            SoundCounter.append(myVoice)  # even-numbered seconds add myVoice to stack
        else:
            SoundCounter.append(dragonVoice)  # odd-numbered seconds add dragonVoice to stack
    winsound.PlaySound(SoundCounter[-1], winsound.SND_ALIAS)  # plays voice at the top of the stack
    Answer4 = input("Now should Clara exit the closet?:")  # Clara should not leave if Chicane Dragon is right next to the door.
    if Answer4 == "Yes" and SoundCounter[-1] == myVoice:  # Clara leaves the closet at the sound of her voice.
        print("You run for your life across the Facility to the other side.")  # Clara escapes.
        break
    elif Answer4 == "Yes" and SoundCounter[-1] == dragonVoice:  # Clara leaves the closet at the sound of the Dragon's voice.
        dragonVoicePlay(3)
        print("the dragon of Chicane...")
        print("...it has devoured Clara!")
        exit()  # Clara dies.
    SoundCounter.clear()  # stack cleared to prepare for the next loop.
print("Whew! The Chicane Facility exit is right around the corner.")
Answer5 = input("Proceed?:")
if Answer5 == "No":
    dragonVoicePlay(1)  # Clara is detected but not devoured (yet).
    print("The dragon may have heard you. You look at the locked door.")

print("The Dragon: 'One human, two arms, eight joints, and nine organs! Yum.'")  # Dragon prepares to devour Clara.
Select = [9, 8, 2, 1]  # list/min heap of Clara's targeted body parts; data structure 3: heap
print("Clara: Ah, that must be the lock code!")  # Dragon unknowingly speaks the door code.
heapq.heappushpop(Select, 9)  # Dragon pops the smallest number and replaces it with 9, resetting the code.
print("Clara: 'Foolish dragon! It is not just me. We are Nine Humans!'")
heapq.heappushpop(Select, 9)
print("Clara: 'Foolish dragon! It is not just my two arms. We are Nine Arms!'")
heapq.heappushpop(Select, 9)
print("Clara: 'Foolish dragon! It is not just my eight joints. We are Nine Joints!'")
print("And Clara reminds herself that she has Nine Organs herself.")  # Clara figures out that the code has been reset.
Answer6 = input("What four numbers concatenated together unlock the padlock?:")
if Answer6 == '9999':  # The code is 9999.
    print('Clara escapes from Chicane Facility with only the slightest burn on her shoulder.')
    # Clara survives!
else:  # Clara hesitates and dies.
    dragonVoicePlay(3)
    print("the dragon of Chicane...")
    print("...it has devoured Clara!")
    exit()

mySound.close()  # closes mySound
dragonSound.close()  # closes dragonSound
