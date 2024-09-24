import cv2
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

# ===================================Function 1=============================================


def color_balance(img, percent=1):
    # Tính toán giá trị cắt từ phần trăm đầu và cuối của mỗi kênh màu
    assert img.shape[2] == 3, "Ảnh phải có 3 kênh (BGR)"
    out_channels = []
    cumstops = [percent, 100-percent]

    # Lặp qua các kênh màu (B, G, R)
    for i in range(3):
        # Lấy kênh màu hiện tại
        channel = img[:, :, i]

        # Tính giá trị phần trăm cắt (cut-off values)
        low_val, high_val = np.percentile(channel, cumstops)

        # Cắt giá trị và co giãn lại để nằm trong khoảng 0-255
        channel = np.clip(channel, low_val, high_val)
        channel = np.uint8(255 * (channel - low_val) / (high_val - low_val))

        # Thêm kênh đã cân bằng vào danh sách
        out_channels.append(channel)

    # Gộp lại các kênh B, G, R đã điều chỉnh
    balanced_img = cv2.merge(out_channels)

    return balanced_img


# ===================================Function 2=============================================


def histogram_equalization(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    equalized_img = cv2.equalizeHist(img_gray)
    return img_gray, equalized_img

# ===================================Function 3=============================================


def median_filter(img, kernel_size=5):
    filtered_img = cv2.medianBlur(img, kernel_size)
    return filtered_img

# ===================================Function 4=============================================


def mean_filter(img, kernel_size=5):
    filtered_img = cv2.blur(img, (kernel_size, kernel_size))
    return filtered_img

# ===================================Function 5=============================================


def gaussian_smoothing(img, kernel_size=5, sigma=1):
    smoothed_img = cv2.GaussianBlur(img, (kernel_size, kernel_size), sigma)
    return smoothed_img



#note: python -m streamlit run .\app.py 
