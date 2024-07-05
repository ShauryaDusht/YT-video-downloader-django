import os
from django.shortcuts import render, redirect
from pytube import YouTube
from moviepy.editor import VideoFileClip, AudioFileClip
from .forms import URLForm

def download_video(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            quality = form.cleaned_data['quality']
            yt = YouTube(url)
            title = yt.title

            # Define download paths
            video_folder = 'downloads/videos'
            audio_folder = 'downloads/audios'
            merged_folder = 'downloads/merged'
            os.makedirs(video_folder, exist_ok=True)
            os.makedirs(audio_folder, exist_ok=True)
            os.makedirs(merged_folder, exist_ok=True)

            # Filter and download video stream based on selected quality
            video_stream = yt.streams.filter(res=quality, file_extension='mp4', progressive=False).first()
            if not video_stream:
                # Fallback to highest quality available if selected quality is not available
                video_stream = yt.streams.filter(file_extension='mp4', progressive=False).order_by('resolution').desc().first()
            audio_stream = yt.streams.filter(only_audio=True).first()

            video_path = os.path.join(video_folder, f"{title}_video.mp4")
            audio_path = os.path.join(audio_folder, f"{title}_audio.mp4")

            # Download video
            video_stream.download(output_path=video_folder, filename=f"{title}_video.mp4")

            # Download audio
            audio_stream.download(output_path=audio_folder, filename=f"{title}_audio.mp4")

            # Merge video and audio
            video_clip = VideoFileClip(video_path)
            audio_clip = AudioFileClip(audio_path)
            final_clip = video_clip.set_audio(audio_clip)
            final_path = os.path.join(merged_folder, f"{title}.mp4")
            final_clip.write_videofile(final_path, codec="libx264", progress_bar=False)

            # Clean up previous downloads
            os.remove(video_path)
            os.remove(audio_path)

            return redirect('download_success', title=title)
    else:
        form = URLForm()
    return render(request, 'downloader/download.html', {'form': form})


def download_success(request, title):
    return render(request, 'downloader/success.html', {'title': title})