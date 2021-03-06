import time
import speech_recognition as sr

def recognize_speech_from_mic(recognizer, microphone):
    # check that recognizer and microphone arguments are appropriate type
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    # adjust the recognizer sensitivity to ambient noise and record audio
    # from the microphone
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source,  phrase_time_limit=5)

    # set up the response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }
    # try recognizing the speech in the recording
    # if a RequestError or UnknownValueError exception is caught,
    #     update the response object accordingly
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        # speech was unintelligible
        response["error"] = "Unable to recognize speech"

    return response

def search_wiki(word):
   definition = wikipedia.summary(word, sentences = 1)
   return definition




if __name__ == "__main__":

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    instructions = ("Please say something!")
    print(instructions)
    time.sleep(2)
    print('You can talk now')
    voicecommand = recognize_speech_from_mic(recognizer, microphone)

    print("You said: {}".format(voicecommand["transcription"]))
    voicecommand = voicecommand["transcription"]

    lines = voicecommand.split()

    if lines[0].lower() == "wiki":
            search_wiki(lines[1])
    elif lines[0].lower() == 'math':
            search_formulas(lines[1])




