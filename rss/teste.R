# if (!require(devtools)) install.packages("devtools")
# https://github.com/decryptr/decryptr

# tensorflow::install_tensorflow()
# keras::install_keras()

# devtools::install_github("decryptr/decryptr")

# library(decryptr)
# file <- download_captcha("rfb", path = "./img")
# decrypt(file, model = model)
args = commandArgs(trailingOnly=TRUE)

# myfl <- file.path(args[1], "myfile.txt")

print(args[1])
print(args[2])
print(length(args))
gete <- "teste de cascatads.sdstxt"
cat(gete, file = args[2])
# print(myfl)