# 声纳图像像素值翻转

import numpy as np
import cv2
import os

# 图像路径（支持中文）
image_path = r"E:\homework\latex\hitszthesis\figures\各向异性.png"

# 检查文件是否存在
if not os.path.exists(image_path):
    print(f"错误：文件不存在！\n{image_path}")
    exit()

# 解决中文路径：二进制读取 + 解码为灰度图
with open(image_path, 'rb') as f:
    img_data = f.read()

img_array = np.frombuffer(img_data, np.uint8)
img = cv2.imdecode(img_array, cv2.IMREAD_GRAYSCALE)

if img is None:
    print("错误：无法解码图像，文件可能损坏。")
    exit()

# 像素值反转：255 - 每个像素值
inverted_img = 255 - img

# 写回原文件（支持中文路径）
success, encoded_img = cv2.imencode('.png', inverted_img)
if success:
    with open(image_path, 'wb') as f:
        f.write(encoded_img.tobytes())
    print(f"成功！像素值已反转（负片效果）并覆盖原文件：\n{image_path}")
else:
    print("错误：图像保存失败。")