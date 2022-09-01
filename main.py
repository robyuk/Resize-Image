import cv2

def calculateDims(scalePercent, width, height):
  newHeight=int(height*scalePercent/100)
  newWidth=int(width*scalePercent/100)
  return (newWidth, newHeight)

def resize(imagePath, scalePercent, resizedPath):
  image=cv2.imread(imagePath)
  print(f'Original Dimensions: {image.shape}')
  newDims=calculateDims(scalePercent,image.shape[1],image.shape[0])
  # Note:  image.shape is (h, w, d), 
  # but cv2.resize(image, (w, h)) so h and w are swapped!
  resizedImage=cv2.resize(image, newDims )
  print(f'New Dimensions: {newDims}')
  cv2.imwrite(resizedPath, resizedImage)

resize('galaxy.jpeg',20,'resized-galaxy.jpeg')