from PIL import Image
import os
import shutil


# 配置壁纸路径
wallpaper_path = 'C:/Users/dongmei/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets'
work_path = 'D:/Person/hupz/Pictures'
desktop_wallpaper_dir = '桌面背景'
mobile_wallpaper_dir = '手机背景'


def create_dir_if_not_exist(tgt_dir):
    if not os.path.exists(tgt_dir):
        print('配置文件目录不存在，创建目录...')
        os.makedirs(tgt_dir)
        print('创建配置文件目录成功！')


def main():

    os.chdir(work_path)

    create_dir_if_not_exist(desktop_wallpaper_dir)
    create_dir_if_not_exist(mobile_wallpaper_dir)

    src_file_list = os.listdir(wallpaper_path)

    desktop_file_list = os.listdir(desktop_wallpaper_dir)
    desktop_file_list = [i[0:-4] for i in desktop_file_list]

    mobile_file_list = os.listdir(mobile_wallpaper_dir)
    mobile_file_list = [i[0:-4] for i in mobile_file_list]

    for filename in src_file_list:
        img = Image.open(wallpaper_path+os.sep+filename)
        img_width = img.width
        img_height = img.height
        img_format = img.format
        if img_format in ('JPEG', 'JPG'):
            img_format = 'jpg'
        else:
            img_format = img_format.lower()

        if img_width > img_height > 1000:
            # print(img_size, img_width, img_height, img_format)
            src_filepath = wallpaper_path+os.sep+filename
            tgt_filepath = desktop_wallpaper_dir + os.sep + filename + '.' + img_format
            # print(src_filepath, tgt_filepath)
            if filename not in desktop_file_list:
                shutil.copyfile(src_filepath, tgt_filepath)
                print('已拷贝%s.%s至桌面背景' % (filename, img_format))
        elif img_height > img_width > 1000:
            src_filepath = wallpaper_path + os.sep + filename
            tgt_filepath = mobile_wallpaper_dir + os.sep + filename + '.' + img_format

            if filename not in mobile_file_list:
                shutil.copyfile(src_filepath, tgt_filepath)
                print('已拷贝%s.%s至手机背景' % (filename, img_format))


if __name__ == '__main__':
    main()
