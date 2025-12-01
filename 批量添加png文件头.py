import os
import glob

def add_png_header_to_images():
    """
    在当前目录下所有图片文件头部添加PNG文件头
    十六进制：89504E470D0A1A0A
    """
    # PNG文件头的十六进制数据
    png_header = bytes.fromhex('89504E470D0A1A0A')

    # 支持的图片文件扩展名
    image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp', '*.tiff', '*.webp']

    # 获取当前目录下所有图片文件
    image_files = []
    for ext in image_extensions:
        image_files.extend(glob.glob(ext))
        image_files.extend(glob.glob(ext.upper()))

    if not image_files:
        print("当前目录下未找到图片文件")
        return

    print(f"找到 {len(image_files)} 个图片文件:")
    for file in image_files:
        print(f"  - {file}")

    print("\n开始处理...")

    for filename in image_files:
        try:
            # 读取原文件内容
            with open(filename, 'rb') as f:
                original_content = f.read()
          
            # 检查文件是否已经有PNG头（避免重复添加）
            if original_content.startswith(png_header):
                print(f"跳过 {filename} - 已包含PNG文件头")
                continue
          
            # 写入新文件（先写PNG头，再写原内容）
            with open(filename, 'wb') as f:
                f.write(png_header)
                f.write(original_content)
          
            print(f"成功处理: {filename}")
          
        except Exception as e:
            print(f"处理 {filename} 时出错: {e}")

    print("\n处理完成！")

if __name__ == "__main__":
    # 确认操作
    response = input("此操作将在所有图片文件头部添加PNG文件头，可能会损坏文件。是否继续？(y/N): ")
    if response.lower() in ['y', 'yes']:
        add_png_header_to_images()
    else:
        print("操作已取消")