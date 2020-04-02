import os
import datetime

# write the path of the specific folder
dir_path = "file/to/folder"
# write down the number of days that if the date of the last created file is greater than that number of days
# from a particular file, the file will be deleted
days_number = 0


def remove_old_files(path, difference_days_number):
    """
    The function check if the files in the folder is old if it is the function remove the file from the folder.
    :param path: The folder path.
    :param difference_days_number: The number of days that if the date of the last created file is greater than that
     number of days from a particular file, the file will be deleted.
    :return: The function does not return nothing.
    """
    dir_files = os.listdir(path)
    for file in dir_files:
        file_path = f"{path}/{file}"
        create_time_byte = os.path.getctime(file_path)
        create_time = datetime.datetime.fromtimestamp(create_time_byte)
        if is_old_file(create_time, difference_days_number, path) is True:
            os.remove(file_path)


def is_old_file(create_time, difference_days_number, path):
    """
    The function check if the file creation date is old relative to the creation time of the last file that was created
    in the specific folder.
    :param create_time: The creation time of the specific file.
    :param difference_days_number: The number of days that if the date of the last created file is greater than that
     number of days from a particular file, the file will be deleted.
    :param path: The folder path.
    :return: The function return true if the difference between the last file that was created and the create time of
    the specific file bigger than the difference_days_number.
    """
    the_last_file = os.path.getmtime(path)
    the_last_file_time = datetime.datetime.fromtimestamp(the_last_file)
    difference = the_last_file_time - create_time
    if difference.days <= difference_days_number:
        return False
    return True


if __name__ == '__main__':
    remove_old_files(dir_path, days_number)
