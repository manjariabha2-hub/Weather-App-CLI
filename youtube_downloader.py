import yt_dlp
import os


DOWNLOAD_FOLDER = "Downloads"


if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)



def download():

    url = input(
        "Enter YouTube URL: "
    )


    options = {

        "format": "best",

        "outtmpl":
        f"{DOWNLOAD_FOLDER}/%(title)s.%(ext)s"

    }


    try:

        print("\nDownloading...\n")


        with yt_dlp.YoutubeDL(options) as ydl:

            ydl.download([url])


        print(
            "\nDownload completed!"
        )


    except Exception as e:

        print(
            "Error:",
            e
        )




print("""
============================
   YOUTUBE DOWNLOADER
============================
""")


while True:


    print("""
1. Download Video
2. Exit
""")


    choice=input(
        "Choose: "
    )


    if choice=="1":

        download()


    elif choice=="2":

        break


    else:

        print(
            "Wrong option"
        )