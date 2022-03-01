# ASCIIpy
ASCIIpy is a Python CLI to convert images to ascii art.

## Install
```
git clone https://github.com/corr0si0n/asciipy.git
pip install -r requirements.txt
```


## Run
```
python cli.py ascii input_image.jpg
```

The intensity of the ascii fill can be adjusted with a `--size` flag. This defaults to 128. A larger number will make the ascii smaller and add more detail. A lower number will make the text more prominent and reduce detail.
```
python cli.py ascii input_image.jpg --size 64
```

The artwork often comes out best for images with subjects over a black background. If you run this against brighter images you can try the `--inverted` flag. This will invert the image before processing and can lead to more desirable results. The flag defaults to `False`.
```
python cli.py ascii input_image.jpg --inverted True
```



