# add shebang line
#!/usr/bin/env python3

# import necessary modules
import os, sys
from PIL import Image

for root, dirs, files in os.walk("."):
# iterate through each file
  for file in files:
  image, f = os.path.splitext(file)
  new_path = '/opt/icons/' + image
  try:
    Image.open(file).rotate(-90).resize((128,128)).convert("RGB").save(new_path, 'JPEG')
  except IOError:
    print('cannot convert', file)
