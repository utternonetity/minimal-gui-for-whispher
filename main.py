import sys

from interface import Ui_MainWindow
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from docx import Document

from pydub import AudioSegment

import whisper



class ProgressHandler(QtCore.QThread):
    mySignal = QtCore.pyqtSignal(list)

    def __init__(self, input_file, output_folder, output_path_file, parent = None):
        super().__init__(parent)
        self.input_file=input_file
        self.output_folder = output_folder
        self.output_path_file = output_path_file
    
    def run(self):

        def split_audio(input_file, output_folder, segment_legth = 30):
            count=0 
            audio_file = AudioSegment.from_file(input_file) 
            segment_legth_ms = segment_legth * 1000 
 
            for i, start_time in enumerate(range(0, len(audio_file), segment_legth_ms)): 
                segment = audio_file[start_time:start_time+segment_legth_ms] 
 
                output_file = f"{output_folder}/segment_{i + 1}.wav" 
                segment.export(output_file, format="wav") 
                count+=1 
            return count 
        
        count = split_audio(self.input_file, self.output_folder)

        result_file = open(self.output_path_file, "w")

        model = whisper.load_model("large-v3")

        for step in range(count):

            audio = whisper.load_audio(f"output_folder/segment_{step + 1}.wav") 
            audio = whisper.pad_or_trim(audio) 

            mel = whisper.log_mel_spectrogram(audio, n_mels=128).to(model.device)
            options = whisper.DecodingOptions()

            result = whisper.decode(model, mel, options)
            result_file.write("\n")
            result_file.write(result.text)
            self.mySignal.emit(["progress_increment", ((step+1)*100)//count])

            doc = Document()

            with open( self.output_path_file, 'r', encoding='utf-8') as f:
                text = f.read()
                doc.add_paragraph(text)
            
            dotindex = self.output_path_file.rindex('.')


        #for step in range (0, 101):
            #self.mySignal.emit(["progress_increment", step])
            #time.sleep(0.03)



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.progressBar.setValue(0)

        self.ui.choose_file_bt.clicked.connect(lambda: self.ui.progressBar.setValue(0))
        self.ui.choose_file_bt.clicked.connect(self.transcribe_audio)

    def transcribe_audio(self):
        input_audio_path = QFileDialog.getOpenFileName(self, "Выберите аудиофайл", "", "Audio Files (*.wav *.mp3 *.flac)")
        dotindex = input_audio_path[0].rindex('.')
        output_result_file = input_audio_path[0][:dotindex] + '.txt'
        output_folder_path = "output_folder"

       
       
        self.transcriber_thread = ProgressHandler(input_audio_path[0], output_folder_path, output_result_file)
        self.transcriber_thread.mySignal.connect(self.signal_handler)
        self.transcriber_thread.start()

        
        

        

    def signal_handler(self, value):

        if value[0] == "progress_increment":
            current_value = self.ui.progressBar.value()
            self.ui.progressBar.setValue(value[1])
        
        if value[1] == 100:
            self.ui.label.setText("Завершено!")
            media_player = QMediaPlayer()
            file_path = "1.mp3"  
            url = QUrl.fromLocalFile(file_path)
            media_content = QMediaContent(url)
            media_player.setMedia(media_content)
            media_player.play()
            return
        
    


if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())