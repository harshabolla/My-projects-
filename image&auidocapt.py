# pip install cpatcha
from captcha.audio import AudioCaptcha
from captcha.image import ImageCaptcha
print('imported')
image = ImageCaptcha(width = 280, height = 90)
data = image.generate('HarshatejaBolla')
image.write("HarshatejaBolla",'harsha.png')

audio = AudioCaptcha()
print('auioimported')

data1 = audio.generate('123')
image.write("123",'harsha.wav')
print('auido generated')