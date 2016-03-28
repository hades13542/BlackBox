from tkinter import filedialog
import sys
class Decoder:
    def __init__(self):
        try:
            file = filedialog.askopenfilename()
            self.time = []
            self.latitude = []
            self.longtude = []
            self.course = []
            self.speed = []
            self.feet = []
            self.file = open(file, 'r')
        except:
            print("Nie podano pliku z danymi")
            sys.exit()
        #for line in self.file:
        #    print(line)

    def getData(self):
        try:
            for line in self.file:
                temp = line.split('\t')
                self.time.append(temp[0])
                self.latitude.append(temp[1])
                self.longtude.append(temp[2])
                self.course.append(temp[3])
                self.speed.append(temp[6])
                self.feet.append(temp[7].replace(".", ""))

            return [self.time, self.latitude, self.longtude, self.course, self.speed, self.feet]
        except:
            print("Podany plik nie jest poprawnym plikiem z danymi")
            sys.exit()

    def print(self):
        print(self.time)
        print(self.latitude)
        print(self.longtude)
        print(self.course)
        print(self.speed)
        print(self.feet)
