from PIL import Image
import os
import shutil
import configparser


# 读取配置文件内容
file = 'configuration.ini'
con = configparser.ConfigParser()
con.read(file, encoding='utf-8')
sections = con.sections()
file_path = dict(con.items('file_path'))
wallpaper_path = file_path['wallpaper_path']
store_path = file_path['store_path']
desktop_wallpaper_dir = file_path['desktop_wallpaper_dir']
mobile_wallpaper_dir = file_path['mobile_wallpaper_dir']


def create_dir_if_not_exist(tgt_dir):
    if not os.path.exists(tgt_dir):
        print('配置文件目录不存在，创建目录...')
        os.makedirs(tgt_dir)
        print('创建配置文件目录成功！')


def main():

    create_dir_if_not_exist(store_path)
    os.chdir(store_path)

    create_dir_if_not_exist(desktop_wallpaper_dir)
    create_dir_if_not_exist(mobile_wallpaper_dir)

    src_file_list = os.listdir(wallpaper_path)

    desktop_file_list = os.listdir(desktop_wallpaper_dir)
    desktop_file_list = [i[0:-4] for i in desktop_file_list]

    mobile_file_list = os.listdir(mobile_wallpaper_dir)
    mobile_file_list = [i[0:-4] for i in mobile_file_list]

    cp_cnt = 0
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
                cp_cnt += 1
                print('已拷贝%s.%s(%s,%s)至桌面背景' % (filename, img_format, img_width, img_height))
        elif img_height > img_width > 1000:
            src_filepath = wallpaper_path + os.sep + filename
            tgt_filepath = mobile_wallpaper_dir + os.sep + filename + '.' + img_format

            if filename not in mobile_file_list:
                shutil.copyfile(src_filepath, tgt_filepath)
                cp_cnt += 1
                print('已拷贝%s.%s(%s,%s)至手机背景' % (filename, img_format, img_width, img_height))

    if cp_cnt > 0:
        print('总计拷贝 %s 张新壁纸' % cp_cnt)
    else:
        print('未发现新壁纸')


if __name__ == '__main__':
    main()
