import os
import shutil
import re
import glob
import sys

folder_name = ['images', 'documents', 'audio', 'video', 'archives', 'other']
IMAGES = "images"
DOCUMENTS = "documents"
AUDIO = "audio"
VIDEO = "video"
ARCHIVES = "archives"
OTHER = "other"
extensions = {
    "jpeg": IMAGES,
    "png": IMAGES,
    "jpg": IMAGES,
    "svg": IMAGES,
    "avi": VIDEO,
    "mp4": VIDEO,
    "mov": VIDEO,
    "mkv": VIDEO,
    "ogg": AUDIO,
    "wav": AUDIO,
    "amr": AUDIO,
    "mp3": AUDIO,
    "doc": DOCUMENTS,
    "docx": DOCUMENTS,
    "txt": DOCUMENTS,
    "pdf": DOCUMENTS,
    "xlsx": DOCUMENTS,
    "pptx": DOCUMENTS,
    "zip": ARCHIVES,
    "gz": ARCHIVES,
    "tar": ARCHIVES
    # "*":OTHER
}
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r",
               "s", "t", "u", "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def normalize(file_name):
    m = re.match(r"^(.+)\.([\w\d]{2,4})$", file_name)
    file_name = m.group(1)
    extension = m.group(2)
    translated_name = ""
    for let in file_name:
        if TRANS.get(ord(let)):
            translated_name += TRANS[ord(let)]
        else:
            translated_name += let
    translated_name = re.sub(r"[^\w\d]", "_", translated_name)
    return f"{translated_name}.{extension}"


def sort_folders(path):
    files = os.listdir(path)
    print(files)
    for file_item in files:
        if not os.path.isdir(file_item):
            extension = re.match(r".+\.([\w\d]{2,4})$", file_item)
            if extension:
                target_path = extensions.get(extension.group(1), OTHER)
                shutil.move(os.path.join(path, file_item), os.path.join(
                    path, f"{target_path}/{normalize(file_item)}"))


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    for folder in folder_name:
        print(os.path.join(path, folder))
        if not os.path.exists(os.path.join(path, folder)):
            os.makedirs(os.path.join(path, folder))
    for path in glob.glob(path, recursive=True):
        print(path)
    sort_folders(path=path)


if __name__ == '__main__':
    main()
