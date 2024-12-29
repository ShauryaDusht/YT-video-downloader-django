# YT-video-downloader-django

A **Django-based web application** that allows users to download YouTube videos in various quality formats. The application handles the download process by separately fetching video and audio streams, then merging them to provide the best possible quality.

---

## ✨ Features
- 🖥️ **Clean and responsive web interface**
- 📺 **Multiple video quality options** (240p to 1080p)
- 🔄 **Automatic fallback** to the highest available quality if the selected quality is unavailable
- 🎵 **Separate video and audio stream processing** for better quality
- 🧹 **Automatic cleanup** of temporary files after processing

---

## 🛠️ Prerequisites
- ✅ Python 3.x
- ✅ Django 3.2+
- ✅ [pytube](https://pytube.io/)
- ✅ [moviepy](https://zulko.github.io/moviepy/)

---

## 🚀 Installation

### 1️⃣ Clone the repository:
```
git clone https://github.com/ShauryaDusht/YT-video-downloader-django/
cd youtube-downloader
```

### 2️⃣ Create a virtual environment and activate it:
```
python -m venv venv  
source venv/bin/activate  
```
### 3️⃣ Install the required packages:
```
pip install django pytube moviepy  
```
### 4️⃣ Apply database migrations:
```
python manage.py migrate  
```
### 5️⃣ Run the development server:
```
python manage.py runserver  
```

---

## 📖 Usage

1. Open your web browser and navigate to [http://localhost:8000](http://localhost:8000).
2. Paste a **valid YouTube video URL** into the input field.
3. Select your desired **video quality** from the dropdown menu.
4. Click the **"Download"** button.
5. Wait for the processing to complete.
6. Your video will be saved in the `downloads/merged` directory.

---

## ⚠️ Limitations

- ⚠️ **Copyrighted content** and music videos may not be downloadable due to YouTube's restrictions.
- 📹 Some videos might not be available in all quality formats.
- 🕒 Download speed depends on your **internet connection** and the video size.

## 🔒 Security Notes

- 🚨 The provided `SECRET_KEY` in `settings.py` is for **development/educational purposes only**.
- For **production deployment**, ensure to:
  - 🔑 Change the `SECRET_KEY`.
  - ⚙️ Set `DEBUG = False`.
  - 🖥️ Update `ALLOWED_HOSTS`.
  - ✅ Implement proper error handling.
  - 📂 Configure proper static file serving.
