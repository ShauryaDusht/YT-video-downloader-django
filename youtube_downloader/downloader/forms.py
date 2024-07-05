from django import forms

class URLForm(forms.Form):
    url = forms.URLField(label='YouTube URL', widget=forms.URLInput(attrs={'class': 'form-control'}))
    QUALITY_CHOICES = [
        ('240p', '240p'),
        ('360p', '360p'),
        ('480p', '480p'),
        ('720p', '720p'),
        ('1080p', '1080p'),
    ]
    quality = forms.ChoiceField(choices=QUALITY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    
