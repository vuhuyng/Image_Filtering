import streamlit as st
from PIL import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

from algorithms import color_balance, histogram_equalization, median_filter, mean_filter, gaussian_smoothing


from template import header, footer, plot_histogram, icon


# Sử dụng đường dẫn này trong hàm header
header('logo.png', "Nguyễn Vũ Huy", "CE180384")


# Phần 1: Xử lý Color Balance
st.markdown("## 1. Xử lý Color Balance")
uploaded_file_cb = st.file_uploader("Chọn một ảnh để áp dụng Color Balance", type=[
                                    "jpg", "jpeg", "png"], key="color_balance")

if uploaded_file_cb is not None:
    try:
        # Đọc file đã upload và chuyển đổi định dạng OpenCV
        image_cb = Image.open(uploaded_file_cb)
        img_np_cb = np.array(image_cb)
        img_cv_cb = cv2.cvtColor(img_np_cb, cv2.COLOR_RGB2BGR)

        # Thêm slider để điều chỉnh phần trăm cắt cho Color Balance
        percent = st.slider("Chọn phần trăm cắt cho Color Balance",
                            min_value=0, max_value=10, value=1, step=1)

        # Áp dụng hàm color_balance với phần trăm từ slider
        balanced_img = color_balance(img_cv_cb, percent)

        # Chuyển đổi ảnh OpenCV (BGR) sang định dạng RGB để hiển thị trên Streamlit
        balanced_img_rgb = cv2.cvtColor(balanced_img, cv2.COLOR_BGR2RGB)

        # Hiển thị ảnh gốc và ảnh sau khi áp dụng Color Balance
        col1, col2, col3 = st.columns([4, 1, 4])
        with col1:
            st.image(image_cb, caption="Ảnh gốc", use_column_width=True)

        with col2:
            # Bạn có thể thay đổi thành biểu tượng tùy ý hoặc bỏ nếu không cần.
            icon()

        with col3:
            st.image(
                balanced_img_rgb, caption="Ảnh sau khi áp dụng Color Balance", use_column_width=True)

            # Chuyển đổi ảnh sang định dạng PNG để tải về
            balanced_img_pil = Image.fromarray(balanced_img_rgb)
            buffered = BytesIO()
            balanced_img_pil.save(buffered, format="PNG")
            img_download = buffered.getvalue()

            # Thêm nút tải ảnh đã áp dụng Color Balance
            st.download_button(
                label="Tải ảnh đã áp dụng Color Balance",
                data=img_download,
                file_name="color_balanced_image.png",
                mime="image/png"
            )

    except Exception as e:
        st.error(f"Lỗi khi xử lý ảnh: {e}")


st.write('---')


# Phần 2: Xử lý Histogram Equalization
st.markdown("## 2. Xử lý Histogram Equalization")
uploaded_file_he = st.file_uploader("Chọn một ảnh để áp dụng Histogram Equalization", type=[
                                    "jpg", "jpeg", "png"], key="histogram_equalization")

if uploaded_file_he is not None:
    try:
        # Đọc file đã upload và chuyển đổi định dạng OpenCV
        image_he = Image.open(uploaded_file_he)
        img_np_he = np.array(image_he)
        img_cv_he = cv2.cvtColor(img_np_he, cv2.COLOR_RGB2BGR)

        # Áp dụng hàm histogram_equalization
        img_gray, equalized_img = histogram_equalization(img_cv_he)

        # Hiển thị ảnh gốc và ảnh đã qua xử lý cùng với histogram
        col1, col2, col3 = st.columns([4, 1, 4])
        with col1:
            st.image(img_gray, caption="Ảnh gốc (Grayscale)",
                     use_column_width=True)
            plot_histogram(img_gray, "Histogram của ảnh gốc")

        with col2:
            icon()

        with col3:
            st.image(
                equalized_img, caption="Ảnh sau khi cân bằng Histogram", use_column_width=True)
            plot_histogram(equalized_img, "Histogram sau khi cân bằng")

            # Chuyển đổi ảnh đã cân bằng Histogram thành định dạng PNG để tải xuống
            equalized_img_pil = Image.fromarray(equalized_img)
            buffered = BytesIO()
            equalized_img_pil.save(buffered, format="PNG")
            img_download = buffered.getvalue()

            # Thêm nút tải ảnh đã cân bằng Histogram
            st.download_button(
                label="Tải ảnh đã cân bằng Histogram",
                data=img_download,
                file_name="equalized_image.png",
                mime="image/png"
            )

    except Exception as e:
        st.error(f"Lỗi khi xử lý ảnh: {e}")

st.write('---')


# Phần 3: Xử lý Median Filter
st.markdown("## 3. Xử lý Median Filter")
uploaded_file_mf = st.file_uploader("Chọn một ảnh để áp dụng Median Filter", type=[
                                    "jpg", "jpeg", "png"], key="median_filter")

if uploaded_file_mf is not None:
    try:
        # Đọc file đã upload và chuyển đổi định dạng OpenCV
        image_mf = Image.open(uploaded_file_mf)
        img_np_mf = np.array(image_mf)
        img_cv_mf = cv2.cvtColor(img_np_mf, cv2.COLOR_RGB2BGR)

        # Thêm slider để chọn kernel_size
        kernel_size = st.slider(
            "Chọn kích thước kernel cho Median Filter", min_value=3, max_value=100, value=3, step=2)

        # Áp dụng hàm median_filter với kernel_size từ slider
        median_filtered_img = cv2.medianBlur(img_cv_mf, kernel_size)

        # Chuyển đổi ảnh OpenCV (BGR) sang định dạng RGB để hiển thị trên Streamlit
        median_filtered_img_rgb = cv2.cvtColor(
            median_filtered_img, cv2.COLOR_BGR2RGB)

        # Hiển thị ảnh gốc và ảnh sau khi áp dụng Median Filter
        col1, col2, col3 = st.columns([4, 1, 4])
        with col1:
            st.image(image_mf, caption="Ảnh gốc", use_column_width=True)

        with col2:
            icon()  # Placeholder for icon

        with col3:
            st.image(median_filtered_img_rgb,
                     caption="Ảnh sau khi áp dụng Median Filter", use_column_width=True)

            # Convert the filtered image to PNG format for download
            median_filtered_img_pil = Image.fromarray(median_filtered_img_rgb)
            buffered = BytesIO()
            median_filtered_img_pil.save(buffered, format="PNG")
            img_download = buffered.getvalue()

            # Add download button
            st.download_button(
                label="Tải ảnh đã áp dụng Median Filter",
                data=img_download,
                file_name="median_filtered_image.png",
                mime="image/png"
            )

    except Exception as e:
        st.error(f"Lỗi khi xử lý ảnh: {e}")


st.write('---')


# Phần 4: Xử lý Mean Filter
st.markdown("## 4. Xử lý Mean Filter")
uploaded_file_mean = st.file_uploader("Chọn một ảnh để áp dụng Mean Filter", type=[
                                      "jpg", "jpeg", "png"], key="mean_filter")

if uploaded_file_mean is not None:
    try:
        # Đọc file đã upload và chuyển đổi định dạng OpenCV
        image_mean = Image.open(uploaded_file_mean)
        img_np_mean = np.array(image_mean)
        img_cv_mean = cv2.cvtColor(img_np_mean, cv2.COLOR_RGB2BGR)

        # Thêm slider để chọn kernel_size
        kernel_size = st.slider(
            "Chọn kích thước kernel cho Mean Filter", min_value=3, max_value=100, value=3, step=2)

        # Áp dụng hàm mean_filter với kernel_size từ slider
        mean_filtered_img = mean_filter(img_cv_mean, kernel_size)

        # Chuyển đổi ảnh OpenCV (BGR) sang định dạng RGB để hiển thị trên Streamlit
        mean_filtered_img_rgb = cv2.cvtColor(
            mean_filtered_img, cv2.COLOR_BGR2RGB)

        # Hiển thị ảnh gốc và ảnh sau khi áp dụng Mean Filter
        col1, col2, col3 = st.columns([4, 1, 4])
        with col1:
            st.image(image_mean, caption="Ảnh gốc", use_column_width=True)

        with col2:
            icon()

        with col3:
            st.image(mean_filtered_img_rgb,
                     caption="Ảnh sau khi áp dụng Mean Filter", use_column_width=True)

            # Convert the filtered image to PNG format for download
            mean_filtered_img_pil = Image.fromarray(mean_filtered_img_rgb)
            buffered = BytesIO()
            mean_filtered_img_pil.save(buffered, format="PNG")
            img_download = buffered.getvalue()

            # Add download button
            st.download_button(
                label="Tải ảnh đã áp dụng Mean Filter",
                data=img_download,
                file_name="mean_filtered_image.png",
                mime="image/png"
            )

    except Exception as e:
        st.error(f"Lỗi khi xử lý ảnh: {e}")

st.write('---')


# Phần 5: Xử lý Gaussian Smoothing
st.markdown("## 5. Xử lý Gaussian Smoothing")
uploaded_file_gaussian = st.file_uploader("Chọn một ảnh để áp dụng Gaussian Smoothing", type=[
                                          "jpg", "jpeg", "png"], key="gaussian_smoothing")

if uploaded_file_gaussian is not None:
    try:
        # Đọc file đã upload và chuyển đổi định dạng OpenCV
        image_gaussian = Image.open(uploaded_file_gaussian)
        img_np_gaussian = np.array(image_gaussian)
        img_cv_gaussian = cv2.cvtColor(img_np_gaussian, cv2.COLOR_RGB2BGR)

        # Slider cho kernel size và sigma
        kernel_size = st.slider(
            "Chọn kích thước Kernel (phải là số lẻ)", min_value=3, max_value=100, step=2, value=5)
        sigma = st.slider("Chọn giá trị Sigma", min_value=0.0,
                          max_value=100.0, step=0.1, value=1.0)

        # Áp dụng hàm gaussian_smoothing với kernel_size và sigma từ slider
        gaussian_filtered_img = gaussian_smoothing(
            img_cv_gaussian, kernel_size, sigma)

        # Chuyển đổi ảnh OpenCV (BGR) sang định dạng RGB để hiển thị trên Streamlit
        gaussian_filtered_img_rgb = cv2.cvtColor(
            gaussian_filtered_img, cv2.COLOR_BGR2RGB)

        # Hiển thị ảnh gốc và ảnh sau khi áp dụng Gaussian Smoothing
        col1, col2, col3 = st.columns([4, 1, 4])
        with col1:
            st.image(image_gaussian, caption="Ảnh gốc", use_column_width=True)

        with col2:
            icon()

        with col3:
            st.image(gaussian_filtered_img_rgb,
                     caption="Ảnh sau khi áp dụng Gaussian Smoothing", use_column_width=True)

            # Convert the filtered image to PNG format for download
            gaussian_filtered_img_pil = Image.fromarray(
                gaussian_filtered_img_rgb)
            buffered = BytesIO()
            gaussian_filtered_img_pil.save(buffered, format="PNG")
            img_download = buffered.getvalue()

            # Add download button
            st.download_button(
                label="Tải ảnh đã áp dụng Gaussian Smoothing",
                data=img_download,
                file_name="gaussian_smoothed_image.png",
                mime="image/png"
            )

    except Exception as e:
        st.error(f"Lỗi khi xử lý ảnh: {e}")


# ======================================================================================


footer('Lab 2 - Image Filtering', 'Nguyễn Vũ Huy', '0379 943 607',
       'huynvce180384@fpt.edu.vn', 'FPT University CanTho Campus')


# note: python -m streamlit run .\app.py
