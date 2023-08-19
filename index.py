import requests
import os

def download_post(url, format="mp4"):
  """Downloads a social media post from the given URL.

  Args:
    url: The URL of the social media post.
    format: The format of the video to download. Supported formats are:
      mp4, webm, ogg, 3gp, flv.

  Returns:
    The path to the downloaded file.
  """

  resp = requests.get(url)
  resp.raise_for_status()

  filename = os.path.basename(url)
  if format == "mp4":
    ext = ".mp4"
  elif format == "webm":
    ext = ".webm"
  elif format == "ogg":
    ext = ".ogg"
  elif format == "3gp":
    ext = ".3gp"
  elif format == "flv":
    ext = ".flv"
  else:
    raise ValueError("Invalid format: %s" % format)

  filepath = os.path.join("downloads", filename + ext)
  with open(filepath, "wb") as f:
    f.write(resp.content)

  return filepath

def main():
  """Downloads a social media post from the given URL."""

  url = request.args.get("url")
  format = request.args.get("format")

  filepath = download_post(url, format)
  print("The video has been downloaded to: %s" % filepath)

if __name__ == "__main__":
  main()
