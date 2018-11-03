# Markdown Image Uploader
This repo is a image uploader for markdown file. It upload all image in the .md file to Cloudinary and replace the path to the images URL.

## Requeirement
It use [Cloudinary](https://cloudinary.com/) to store image so you need a Cloudinary ID.
If it is the first time you use this uploader, you need to replace api information in the `config.py` file.

```python
cloudinary.config(
  cloud_name = your cload name,
  api_key = your api key,
  api_secret = your api secret
)
```

And Cloudinary library is needed.

```
pip install cloudinary
```

## Usage

 Open uploader in CMD.

```
python uploader.py
```
It will pop up a window.

![1541221684923](http://res.cloudinary.com/jiang/image/upload/v1541221901/rtd8zncvrt1luuxxcske.png)

After selecting the markdown files you want to uploaded, it will upload all image in the file to Cloudinary and  create a new markdown file with the images path replaced with URL.

![1541221762407](http://res.cloudinary.com/jiang/image/upload/v1541221901/c49fspg3asujtzjaufgp.png)
