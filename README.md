# 🦠 Pneumonia Detector

A modern, interactive AI web app for detecting pneumonia from chest X-ray images.  
Built with **Python**, **Jupyter Notebooks**, and **Streamlit** for instant, reliable, and easy-to-understand results!

[![Live Demo](https://img.shields.io/badge/Streamlit-Live%20Demo-brightgreen?style=for-the-badge&logo=streamlit)](https://pneumonia-detector-kl9gnnxqhkhrvduhljdf7m.streamlit.app/)

---

## 🔎 What is this?

**Pneumonia Detector** lets you upload a chest X-ray image and get an AI-powered prediction:  
**Pneumonia** or **Normal** — with visual explanations (Grad-CAM) for every result.

- 🧑‍⚕️ Supports healthcare professionals & students
- 🖼️ Visual, user-friendly, and fast
- 🚀 Runs in your browser — no installations needed

---

## 🚀 Live Demo

Try it instantly (no sign-up needed):  
👉 [Launch Pneumonia Detector App](https://pneumonia-detector-kl9gnnxqhkhrvduhljdf7m.streamlit.app/)

---

## 🎬 Visual Demo

![AI X-ray Analysis Animation](https://github.com/Ramesh143-code/Pneumonia-Detector/blob/main/assets/animated-xray.gif)

*Above: Animated demo — upload your X-ray, get prediction with highlighted pneumonia zones!*

---

## 📸 Screenshots

<table>
  <tr>
    <td>
      <img width="400" alt="Upload X-ray" src="https://github.com/Ramesh143-code/Pneumonia-Detector/blob/main/assets/upload-xray.png">
      <br><i>Upload your chest X-ray</i>
    </td>
    <td>
      <img width="400" alt="Prediction Result" src="https://github.com/Ramesh143-code/Pneumonia-Detector/blob/main/assets/prediction-result.png">
      <br><i>See instant prediction</i>
    </td>
  </tr>
  <tr>
    <td>
      <img width="400" alt="Grad-CAM Explanation" src="https://github.com/Ramesh143-code/Pneumonia-Detector/blob/main/assets/gradcam-explain.png">
      <br><i>Visual AI explanation (Grad-CAM)</i>
    </td>
    <td>
      <img width="400" alt="Animated Overlay" src="https://github.com/Ramesh143-code/Pneumonia-Detector/blob/main/assets/animated-overlay.gif">
      <br><i>Animated overlay for clarity</i>
    </td>
  </tr>
</table>

---

## 🌟 Features

- **One-click Prediction:** Upload an X-ray, get a diagnosis.
- **AI Explainability:** Grad-CAM overlays show what the model "sees".
- **Beautiful UI:** Responsive, animated, and mobile-friendly.
- **Fast & Private:** All computations happen instantly; your images are never stored.
- **Open Source:** Reproducible code, notebooks, and models.

---

## 🛠️ Technology Stack

- **Python 3.8+**
- **Jupyter Notebook** (model training, EDA)
- **TensorFlow** / **Keras** for Deep Learning
- **Streamlit** (web app UI & deployment)
- **OpenCV, Pillow, matplotlib** (image processing & visualization)
- **scikit-learn**, **numpy**, **pandas** (data science)

---

## 📦 Installation

#### 1. Clone the repository

```bash
git clone https://github.com/Ramesh143-code/Pneumonia-Detector.git
cd Pneumonia-Detector
```

#### 2. Create a virtual environment & install dependencies

```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### 3. (Optional) Download dataset

- Use the [Chest X-Ray Pneumonia Dataset (Kaggle)](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia)
- Place files in `data/` as described below.

#### 4. Launch the Streamlit app

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
Pneumonia-Detector/
│
├── app.py                # Streamlit web app
├── requirements.txt      # Dependencies
├── model/                # Trained CNN model
├── notebooks/            # Training, EDA, explainability
├── data/                 # (User) X-ray images & datasets
├── assets/               # Screenshots, GIFs, Grad-CAM images
├── utils/                # Helper scripts
└── README.md
```

---

## 📝 Usage

1. Open the web app (`app.py`) locally, or use the [Live Demo](https://pneumonia-detector-kl9gnnxqhkhrvduhljdf7m.streamlit.app/)
2. Upload a chest X-ray image (JPG, PNG)
3. Click **Predict**
4. See your result:
    - **Normal** (🟢) — no signs of pneumonia
    - **Pneumonia** (🔴) — signs detected
5. Review Grad-CAM heatmap for model explanation

---

## 📊 How It Works

- **Input:** Chest X-ray image
- **Model:** Pre-trained deep convolutional neural network (e.g., MobileNetV2, ResNet)
- **Output:** Binary prediction (Pneumonia / Normal) + Grad-CAM visualization

### Example

| Image                | Prediction | Grad-CAM Overlay             |
|----------------------|------------|------------------------------|
| ![](assets/sample-xray.png) | Pneumonia  | ![](assets/sample-gradcam.png)   |

---

## 🧑‍🎓 For Developers & Researchers

- All training and evaluation notebooks are in `notebooks/`
- Easily swap model architectures in code
- Plug in your own X-ray data for retraining

---

## 🤝 Contributing

- Fork the repo
- Create a new branch (`git checkout -b feature-branch`)
- Make your changes
- Submit a Pull Request — feedback & collaboration welcome!

---

## 📄 License

MIT License

---

## 🙋‍♂️ Author

**Ramesh143-code**  
[GitHub Profile](https://github.com/Ramesh143-code)

---

## ⭐ Acknowledgements

- [Kaggle Chest X-Ray Pneumonia Dataset](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia)
- Streamlit, TensorFlow/Keras for amazing tools
- All contributors & the open-source medical AI community

---

## ⚠️ Disclaimer

**This tool is for research and educational purposes only. It is NOT a substitute for professional medical advice or diagnosis.**  
Always consult a qualified healthcare provider for clinical decisions.

---
