#the standard code 
#v1
import tkinter as tk

import pyaudio

import wave


class App:

    def __init__(self, master):

        self.master = master
        self.master.title("WAV Player")
        self.master.geometry("300x200")
        self.create_widgets()
    

    def create_widgets(self):

        self.label = tk.Label(self.master, text="Enter the path to the WAV file:")
        self.label.pack()
        self.entry = tk.Entry(self.master, width=50)
        self.entry.pack()
        self.button = tk.Button(self.master, text="Play", command=self.play_wav)
        self.button.pack()
        self.status_label = tk.Label(self.master, text="")
        self.status_label.pack()
    

    def play_wav(self):

        path = self.entry.get()
        if path.endswith(".wav"):
            try:

                # To Open the WAV file
                with wave.open(path, "rb") as wav_file:
                    # To Get the audio format, number of channels, and sample rate from the WAV file
                    format = pyaudio.get_format_from_width(wav_file.getsampwidth())
                    channels = wav_file.getnchannels()
                    rate = wav_file.getframerate()
                

                    # To Create two output streams using the same audio format, number of channels, and sample rate
                    p = pyaudio.PyAudio()
                    output_devices = []
                    for i in range(p.get_device_count()):
                        if p.get_device_info_by_index(i)['maxOutputChannels'] > 0:
                            output_devices.append(i)
                    if len(output_devices) < 2:
                        self.status_label.config(text="Error: not enough output devices detected.")
                    else:
                        stream1 = p.open(format=format, channels=channels, rate=rate, output=True, output_device_index=output_devices[0])
                        stream2 = p.open(format=format, channels=channels, rate=rate, output=True, output_device_index=output_devices[1])
                        

                        # To Read audio data from the WAV file in chunks and write it to both output streams
                        chunk_size = 1024
                        data = wav_file.readframes(chunk_size)
                        while data:
                            stream1.write(data)
                            stream2.write(data)
                            data = wav_file.readframes(chunk_size)
                        

                        # To  Close the output streams and terminate the PyAudio session
                        stream1.stop_stream()
                        stream1.close()
                        stream2.stop_stream()
                        stream2.close()
                        p.terminate()
                        self.status_label.config(text="WAV file played successfully.")
            except FileNotFoundError:
                self.status_label.config(text="Error: file not found.")
        else:
            self.status_label.config(text="Error: not a WAV file.")
            


root = tk.Tk()
app = App(root)
root.mainloop()
