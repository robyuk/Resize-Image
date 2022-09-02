import cv2
from pathlib import Path

rootDir=Path('images')
resizeDir=Path('resized')
resizePercent=20

def calculateDims(scalePercent, width, height):
  newHeight=int(height*scalePercent/100)
  newWidth=int(width*scalePercent/100)
  return (newWidth, newHeight)

def resize(imagePath, scalePercent, resizedPath):
  image=cv2.imread(imagePath)
  print(f'{imagePath}: Original Dimensions: {image.shape}')
  newDims=calculateDims(scalePercent,image.shape[1],image.shape[0])
  # Note:  image.shape is (h, w, d), 
  # but cv2.resize(image, (w, h)) so h and w are swapped!
  resizedImage=cv2.resize(image, newDims )
  print(f'{resizedPath}: New Dimensions: {newDims}')
  cv2.imwrite(resizedPath, resizedImage)

filePaths=rootDir.glob("*")

for path in filePaths:
  if path.is_file():
    #print(path,f'{resizeDir}/{path.name}')
    resize(str(path),resizePercent,f'{resizeDir}/{path.name}')