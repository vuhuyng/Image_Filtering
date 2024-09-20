import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt


def plot_histogram(image, title):
    fig, ax = plt.subplots()
    ax.hist(image.ravel(), bins=256, range=[0, 256])
    ax.set_title(title)
    ax.set_xlabel('Pixel Intensity')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)


def icon():
    st.markdown("""
    <style>
    .arrow-container {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 100%;
        margin-top: 300px;
        margin-bottom: 10px;
    }
    .arrow {
        font-size: 60px;
        color: #2ecc71;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        animation: bounce 1s infinite;
    }
    @keyframes bounce {
        0%, 100% {
            transform: translateY(0);
        }
        50% {
            transform: translateY(-10px);
        }
    }
    </style>
    <div class="arrow-container">
        <span class="arrow">➔</span>
    </div>
    """, unsafe_allow_html=True)


def header(logo_path, student_name, student_id):
    # Set up the modern page layout and configuration
    st.set_page_config(layout="wide")

    # Advanced CSS for a professional, modern, and tech-inspired design
    st.markdown("""
        <style>
        /* Entire background */
        body {
            background: linear-gradient(135deg, #001f3f 20%, #001020 80%);
            color: white;
            font-family: 'Orbitron', sans-serif;
        }

        /* Glow effect around the container */
        .outer-container::before {
            content: '';
            position: absolute;
            top: -10px;
            left: -10px;
            right: -10px;
            bottom: -10px;
            border: 2px solid rgba(39, 174, 96, 0.7);
            z-index: -1;
            animation: glow 3s infinite alternate;
        }

        @keyframes glow {
            0% { box-shadow: 0 0 15px rgba(39, 174, 96, 0.5); }
            100% { box-shadow: 0 0 30px rgba(39, 174, 96, 0.8); }
        }

        /* Gentle pulse effect */
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }

        /* Circuit line with glowing light effect */
        .circuit-line-container {
            position: relative;
            width: 100%;
            height: 60px;
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 30px;
        }

        .circuit-line {
            width: 80%;
            height: 4px;
            background: linear-gradient(to right, rgba(0, 255, 153, 0.2), rgba(0, 255, 153, 1), rgba(0, 255, 153, 0.2));
            background-size: 200% 100%;
            animation: circuitGlow 4s linear infinite;
            position: absolute;
            top: 50%; /* Center the line vertically */
        }

        @keyframes circuitGlow {
            0% { background-position: 0 0; }
            100% { background-position: 200% 0; }
        }

        /* Eye icon in the center of the circuit line */
        .vision-icon {
            position: relative;
            font-size: 50px;
            color: #00ff99;
            text-shadow: 0 0 10px rgba(0, 255, 153, 0.7);
            animation: iconPulse 2s ease-in-out infinite alternate;
            z-index: 2; /* Ensure the icon is above the circuit line */
        }

        @keyframes iconPulse {
            from { text-shadow: 0 0 10px rgba(0, 255, 153, 0.7); }
            to { text-shadow: 0 0 20px rgba(0, 255, 153, 1); }
        }

        /* Tech container for title and subtitle */
        .tech-container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 20px;
            position: relative;
        }

        .tech-title {
            font-size: 52px;
            font-weight: bold;
            color: #00ff99;
            text-shadow: 0 0 15px rgba(0, 255, 153, 0.7), 0 0 30px rgba(0, 255, 153, 0.4);
            font-family: 'Orbitron', sans-serif;
            letter-spacing: 2px;
            position: relative;
            z-index: 2;
            animation: textGlow 2s ease-in-out infinite alternate;
        }

        /* Glowing effect for the title */
        @keyframes textGlow {
            from { text-shadow: 0 0 15px rgba(0, 255, 153, 0.7), 0 0 30px rgba(0, 255, 153, 0.4); }
            to { text-shadow: 0 0 30px rgba(0, 255, 153, 1), 0 0 50px rgba(0, 255, 153, 0.6); }
        }

        .tech-subtitle {
            font-size: 24px;
            color: #cccccc;
            margin-top: 10px;
            font-family: 'Arial', sans-serif;
            position: relative;
            z-index: 2;
        }

        /* Student information box with modern floating effect */
        .info-box {
            border: 2px solid #27ae60;
            border-radius: 20px;
            padding: 20px;
            background: linear-gradient(145deg, #1e1e1e, #2c2c2c);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.7), 0 0 20px rgba(39, 174, 96, 0.5);
            font-family: 'Orbitron', sans-serif;
            color: #ecf0f1;
            max-width: 400px;
            margin: auto;
            text-align: center;
            position: relative;
            overflow: hidden;
            animation: float 3s ease-in-out infinite;
        }

        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0px); }
        }

        .info-box h2 {
            font-size: 28px;
            margin-bottom: 15px;
            color: #2ecc71;
            text-transform: uppercase;
            letter-spacing: 2px;
            text-shadow: 0 0 8px rgba(39, 174, 96, 0.7);
        }

        .info-box p {
            font-size: 18px;
            margin: 5px 0;
            color: #bdc3c7;
            text-shadow: 0 0 4px rgba(255, 255, 255, 0.1);
        }

        .info-box p b {
            color: #ffffff;
            text-shadow: 0 0 6px rgba(39, 174, 96, 0.5);
        }
        </style>
    """, unsafe_allow_html=True)

    logo = Image.open(logo_path)

    # Create modern container around the title, subtitle, and logo
    with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])

        with col1:
            st.image(logo, width=280)

        with col2:
            st.markdown("""
                <div class="tech-container">
                    <h1 class="tech-title">Lab 2 - Image Filtering</h1>
                    <p class="tech-subtitle">Apply filters and enhance your images</p>
                </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
            <div class="info-box">
                <h2>Student Information</h2>
                <p><b>Name:</b> {student_name}</p>
                <p><b>Student ID:</b> {student_id}</p>
            </div>
            """, unsafe_allow_html=True)

    # Circuit line and eye icon in the center
    st.markdown("""
        <div class="circuit-line-container">
            <div class="circuit-line"></div>
            <div class="vision-icon">&#128065;</div> <!-- Eye icon -->
        </div>
    """, unsafe_allow_html=True)


def footer(topic, author_name, hotline, email, education_unit):
    # CSS for the footer
    st.markdown(f"""
        <style>
        /* Footer Container */
        .footer {{
            text-align: center;
            padding: 30px;
            margin-top: 50px;
            color: #ecf0f1;
            background: linear-gradient(145deg, #0d0d0d, #1a1a1a);
            border-top: 2px solid #27ae60;
            box-shadow: 0 -4px 8px rgba(0, 0, 0, 0.7);
            animation: floatFooter 3s ease-in-out infinite;
            font-family: 'Orbitron', sans-serif;
        }}

        .footer p {{
            margin: 10px 0;
            font-size: 16px;
            color: #ecf0f1;
            letter-spacing: 1px;
            font-weight: 300;
        }}

        .footer p b {{
            color: #2ecc71;
            font-size: 18px;
            font-weight: 500;
        }}

        .footer p a {{
            color: #2ecc71;
            text-decoration: none;
            font-weight: bold;
            transition: color 0.3s ease;
        }}

        .footer p a:hover {{
            color: #1abc9c;
            text-decoration: underline;
        }}

        .footer p.topic {{
            font-size: 20px;
            font-weight: 600;
            color: #f1c40f;
            letter-spacing: 1.5px;
            margin-bottom: 20px;
        }}

        .footer p.copyright {{
            font-size: 14px;
            color: #bdc3c7;
            margin-top: 20px;
            font-style: italic;
        }}

        /* Footer floating animation */
        @keyframes floatFooter {{
            0% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(-5px); }}
            100% {{ transform: translateY(0px); }}
        }}
        </style>

        <div class="footer">
            <p class="topic">{topic}</p>
            <p><b>Author:</b> {author_name}</p>
            <p><b>Zalo:</b> <a href="tel:{hotline}">{hotline}</a></p>
            <p><b>Email:</b> <a href="mailto:{email}">{email}</a></p>
            <p><b>Educational:</b> {education_unit}</p>
            <p class="copyright">© September 2024 - All rights reserved. No copying allowed. Developed by Nguyen Vu Huy.</p>
        </div>
    """, unsafe_allow_html=True)


# note: python -m streamlit run .\app.py
