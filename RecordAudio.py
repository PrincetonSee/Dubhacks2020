import sounddevice
import soundfile as sf
from scipy.io.wavfile import write


def get_recording(time):
    fs = 16000
    second = time
    # print("recording for {} seconds".format(second))
    record_voice = sounddevice.rec(int(second * fs), samplerate=fs, channels=2, blocking=True)
    # print("finished recording.")
    write("output.wav", fs, record_voice)
    record_voice, fs = sf.read("output.wav")
    sf.write("output.flac", record_voice, fs)

    return "output.flac"
