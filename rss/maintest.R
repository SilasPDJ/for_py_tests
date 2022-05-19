
library(decryptr)
file <- download_captcha("rfb", path = "./img")
print(file)
decrypt(file, model = "rfb")



# https://github.com/decryptr/decryptr
