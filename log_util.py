import logging

FORMAT = ("{asctime} - {levelname}: {msg}")

logging.basicConfig(filename='zd15t03_file_list.txt', filemode='w', format=FORMAT, style='{', level=logging.NOTSET)
common_log = logging.getLogger()

if __name__ == '__main__':
    print("Not for separate use")