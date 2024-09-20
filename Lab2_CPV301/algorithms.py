import cv2
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

# ===================================Function 1=============================================


def color_balance(img, clip_limit, grid_size):
    # Chuyển đổi ảnh sang không gian màu LAB
    img_lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    l_channel, a_channel, b_channel = cv2.split(img_lab)

    # Áp dụng CLAHE để cân bằng kênh L (độ sáng) với các tham số từ slider
    clahe = cv2.createCLAHE(clipLimit=clip_limit,
                            tileGridSize=(grid_size, grid_size))
    cl = clahe.apply(l_channel)

    # Kết hợp lại các kênh và chuyển đổi lại sang không gian BGR
    limg = cv2.merge((cl, a_channel, b_channel))
    balanced_img = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

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
