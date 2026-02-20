# save-stream-ts-to-mp4-with-python
# Using Python to save videos from a stream URL (TS format)

## INSTALL FFMPEG

MacOS:
```
brew install ffmpeg
```

## PYTHON ENVIRONMENT

```bash
python3 -m venv ./env/
source env/bin/activate
```

## DEPENDENCIES

### For main.py (download and convert TS streams to MP4)

```bash
pip3 install requests
pip3 install python-ffmpeg-video-streaming
```

### For m3u8info.py (resolve relative paths in M3U8 playlists)

```bash
pip3 install requests
pip3 install m3u8
pip3 install regex
```

## CONFIGURATION

1. **Authentication (optional):** Fill in `do_login()` in `main.py` with your site's login CURL request.
   - Use Chrome > Inspector > Network, copy the login request as cURL.
   - Import it into Postman, then export as Python code to get the headers and payload.

2. **Video URLs:** Replace the placeholder entries in `links` (in `main.py` or `m3u8info.py`) with your actual `.m3u8` URLs.
   - Find these URLs via Chrome > Inspector > Network > filter by `m3u8`.

3. **Output filename:** Edit the `output_name` pattern in `convert_mp4()` inside `main.py` to match your preferred naming convention.

## RUN

### Download and convert streams to MP4

```bash
python3 main.py
```

### Resolve M3U8 relative paths to absolute URLs (optional pre-step)

```bash
python3 m3u8info.py
```

