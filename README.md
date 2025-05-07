# YouTube Video Downloader

This repository provides a Python script to download YouTube videos in high quality. The downloaded video and audio are merged seamlessly to ensure the best experience.

## Prerequisites

Before using this repository, you **must** install `ffmpeg`. `ffmpeg` is required to merge the downloaded video and audio files. Without this, the downloaded content won't be properly combined.

### Install `ffmpeg`

1. Download the `ffmpeg` essentials build from the following link:
   [https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip)

2. Extract the downloaded zip file to a directory of your choice.

3. Add the `bin` folder from the extracted directory to your system's PATH environment variable.

   - **Windows:**
     - Open the Start Menu, search for "Environment Variables", and click "Edit the system environment variables".
     - In the System Properties window, click "Environment Variables".
     - Select the `Path` variable and click "Edit".
     - Add the path to the `bin` folder from the extracted `ffmpeg` directory.

   - **macOS/Linux:**
     - Add the following line to your `.bashrc` or `.zshrc` file:
       ```bash
       export PATH="/path/to/ffmpeg/bin:$PATH"
       ```
     - Replace `/path/to/ffmpeg/bin` with the actual path to the `bin` folder.

4. Verify the installation by running the following command in your terminal or command prompt:
   ```bash
   ffmpeg -version
   ```
   If installed correctly, it will display the version of `ffmpeg`.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/aditya-kr86/youtube-video-downloader.git
   ```

2. Change into the repository directory:
   ```bash
   cd youtube-video-downloader
   ```

3. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:
   ```bash
   python yt-downloader.py
   ```

2. Follow the on-screen instructions to enter the URL of the YouTube video you want to download.

3. The script will download the video and audio, then use `ffmpeg` to merge them into a single file.

## Notes

- Ensure `ffmpeg` is installed and properly configured before running the script.
- This script is intended for educational purposes only. Please ensure you comply with YouTube's terms of service when using this tool.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
