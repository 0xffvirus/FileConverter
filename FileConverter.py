import docx2pdf, sys
import moviepy.editor as movpy
from PIL import Image
def convertdocxpdf(file):
    docx2pdf.convert(file)
    docx2pdf.convert(file, f"{file}.pdf") # convert file to pdf
    print("File Converted Done! | DOCX --> PDF")

def convertjpg(file):
    imag = Image.open(file) # open the image in script
    imgformat = imag.format 
    file = file.split(".") # split name and format of the file
    if imag.mode != "RGB":
        imag = imag.convert('RGB') # convert image to RGB 
        imag.save(f"{file[0]}.jpg") # convert image to JPG
        print(f"File Converted Done! | {imgformat} --> JPG")
    else:
        imag.save(f"{file[0]}.jpg")
        print(f"File Converted Done! | {imgformat} --> JPG")
def convertmkvmp4(file):
    vid = movpy.VideoFileClip(file) # open mkv file 
    file = file.split(".")
    vid.write_videofile(f"{file[0]}.mp4", codec="libx264",audio_codec="aac") # convert mkv file to mp4


def Options():
    print("[ Github : 0xffvirus ]")
    print("[1] DOCX TO PDF")
    print("[2] Image TO JPG")
    print("[3] MKV TO MP4")
    opt = int(input("Select Option : ")) # user options 
    if opt == 1:
        file = str(input("DOCX File Path: "))
        convertdocxpdf(file)
    elif opt == 2:
        file = str(input("Image File Path: "))
        convertjpg(file)
        an = int(input("Another Photo [ 1 YES , 0 NO ] ?  ")) # another photo user option
        if an == 1:
            file = str(input("Image File Path: "))
            convertjpg(file)
        else:
            sys.exit() # close script
    elif opt == 3:
        file = str(input("Video File Path: "))
        convertmkvmp4(file)
    else:
        print("Sorry, select another number.") # no number in the options

Options()
