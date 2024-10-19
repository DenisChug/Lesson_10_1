import threading
from threading import Thread
from time import sleep
from datetime import datetime

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

time_start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end = datetime.now()
print(f"Работа функций {time_end - time_start}")

time_start = datetime.now()

first_stream = Thread(target=write_words, args=(10, 'example5.txt'))
second_stream = Thread(target=write_words, args=(30, 'example6.txt'))
third_stream = Thread(target=write_words, args=(200, 'example7.txt'))
fourth_stream = Thread(target=write_words, args=(100, 'example8.txt'))

first_stream.start()
second_stream.start()
third_stream.start()
fourth_stream.start()

first_stream.join()
second_stream.join()
third_stream.join()
fourth_stream.join()

time_end = datetime.now()
print(f"Работа функций {time_end - time_start}")