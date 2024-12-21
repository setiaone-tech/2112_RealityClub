import sys
import time

# Lirik intro "She said to me..." dari lagu 2112 oleh Reality Club
intro = "She said to me, and I said to her"
intro2 = "to hold back each other's true fate is not of our nature"
intro3 = "let's be mature"
intro4 = "maybe you weren't made for me"
intro5 = "nor I for you"
intro6 = "but I'd be damn lying if I think that that's true"

intro7 = "We were young and we were old"
intro8 = "life was warm then life was cold"
intro9 = "it gets harder, yes, you'll see"
intro10 = "but were we ever meant to be?"

def running_text(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)  # Menulis karakter ke terminal
        sys.stdout.flush()  # Memastikan karakter muncul langsung
        time.sleep(delay)  # Menunggu beberapa detik sebelum karakter berikutnya
    print()  # Menambahkan baris baru setelah selesai

# Menjalankan program dengan teks lirik lagu intro
running_text(intro, delay=0.1)
time.sleep(2)
running_text(intro2, delay=0.05)
time.sleep(1)
running_text(intro3, delay=0.05)
time.sleep(5)
running_text(intro4, delay=0.1)
time.sleep(1)
running_text(intro5, delay=0.1)
time.sleep(5)
running_text(intro6, delay=0.05)
time.sleep(5)
running_text(intro7, delay=0.1)
time.sleep(1)
running_text(intro8, delay=0.1)
time.sleep(1)
running_text(intro9, delay=0.1)
time.sleep(1)
running_text(intro10, delay=0.1)
