Description in English:
DiskSync is a Python script that synchronizes two folders from two different drives, automatically updating the data. The program copies files from one source folder to another and keeps them up to date by deleting outdated files and replacing them with newer versions.

Reason for creating the code:
After I accidentally formatted a flash drive containing important Obsidian notes, I decided to create a script that would sync my data not only on the flash drive but also on my hard drive. This ensures that all important data is always backed up and available.

Installation instructions:

    Download all 4 files from this repository.
    The main synchronization file is sync.py.
    In folder.py, specify the sours_target folder, which will receive the data to update the contents of the target_folder.
    In main.py, there's a function that checks if the specified program (Obsidian by default) is running. If needed, replace the program name with the one you want to use.
    Use the batch file start_obsidian_with_script.bat, which runs both the program and the synchronization script.

Example usage:

    The repository includes a .bat file that launches the program Obsidian and the sync script. If you need to use a script for another program, create a new bat file in which the program you need and the script itself will be launched
    Choose the .bat file as the launch object in your program's shortcut, so both the program and synchronization start at the same time.

Technologies and libraries:

    Python standard libraries: os, psutil, time
    The script works as follows:
        Every 20 seconds, it checks whether the specified program is running.
        If the program is not running, the synchronization process starts.
        Files from the sours_folder are copied to the target_folder.
        Files in the target_folder are updated if their version is outdated.
        If a file is missing in the sours_folder, it is deleted from the target_folder.

Important notice:
Be cautious and double-check the target_folder before running the script, as all files in this folder will be deleted and replaced with files from the sours_folder.
--- 
Описание на Русском:
DiskSync — это скрипт на Python, который синхронизирует две папки с двух разных дисков, автоматически обновляя данные. Программа копирует файлы с одного источника в другую папку, а также поддерживает их актуальность путем удаления старых файлов и замены их на более новые версии.

Причина написания кода:
После того как я случайно отформатировал флешку с важными записями в Obsidian, я решил создать скрипт, который бы синхронизировал мои данные не только на флешке, но и на жестком диске. Это позволяет гарантировать, что все важные данные всегда будут сохранены и доступны.

Инструкция по установке:

    Скачайте все 4 файла из этого репозитория.
    Основной файл для синхронизации — sync.py.
    В файле folder.py укажите папку sours_target, которая будет получать данные, чтобы изменить содержимое папки target_folder.
    В файле main.py есть функция для проверки, запущена ли указанная программа (по умолчанию Obsidian). Если необходимо, замените имя программы на нужное вам.
    Используйте файл разметки start_obsidian_with_script.bat, который запускает как программу, так и скрипт синхронизации.

Пример использования:

    В репозитории имеется .bat файл, который запускает программу Obsidian и скрипт синхронизации. Если вам нужно использовать скрипт для другой программы создайте новый bat файл в котором будет запускаться программа которая вам нужна и сам скрипт.
    Выберите .bat файл в ярлыке вашей программы, чтобы при запуске одновременно стартовали как программа, так и синхронизация.

Технологии и библиотеки:

    Стандартные библиотеки Python: os, psutil, time
    Скрипт работает следующим образом:
        Каждые 20 секунд проверяется, запущена ли указанная программа.
        Если программа не работает, запускается процесс синхронизации.
        Файлы с папки sours_folder копируются в папку target_folder.
        Файлы в target_folder обновляются, если их версия устарела.
        Если файл отсутствует в sours_folder, он удаляется из target_folder.

Важное замечание:
Будьте осторожны и несколько раз перепроверяйте папку target_folder, так как при запуске скрипта из этой папки будут удалены все файлы и заменены на файлы из папки sours_folder.
