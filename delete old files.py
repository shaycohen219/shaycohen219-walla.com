import os
import datetime

# write the path of the specific folder
dir_path = "file/to/folder"
# write down the number of days that if the date of the last created file is greater than that number of days
# from a particular file, the file will be deleted
days_number = 0


def remove_old_files(path, difference_days_number):
    """
    The function check if the file creation date is old relative to the creation time of the last file that was created
    in the specific folder and if it is old the function remove the file from the folder.
    :param path: The folder path.
    :param difference_days_number: The number of days that if the date of the last created file is greater than that
     number of days from a particular file, the file will be deleted.
    :return: The function does not return nothing.
    """
    dir_files = os.listdir(path)
    for file in dir_files:
        file_path = f"{path}/{file}"
        create_time_byte = os.path.getctime(file_path)
        create_file_time = datetime.datetime.fromtimestamp(create_time_byte)
        the_last_create_file = os.path.getmtime(path)
        the_last_create_file_time = datetime.datetime.fromtimestamp(the_last_create_file)
        difference = the_last_create_file_time - create_file_time
        if difference.days > difference_days_number:
            os.remove(file_path)


if __name__ == '__main__':
    remove_old_files(dir_path, days_number)
