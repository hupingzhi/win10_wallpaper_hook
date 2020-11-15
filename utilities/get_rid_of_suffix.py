import os


# 配置壁纸路径
wallpaper_path = 'D:/Person/hupz/Pictures/手机背景'


def main():

    os.chdir(wallpaper_path)
    src_file_list = os.listdir(wallpaper_path)

    for filename in src_file_list:
        os.rename(filename, filename[0:-4])


if __name__ == '__main__':
    main()
