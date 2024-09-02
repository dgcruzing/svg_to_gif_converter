# SVG to GIF Converter

This tool converts animated SVG files to GIF format with customizable resolution and animation settings.

## Setup

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Ensure you have ChromeDriver installed and in your system PATH

## Usage

Run `python svg_to_gif_converter.py` and follow the GUI prompts.

# SVG to GIF Converter - Windows Instructions

## System Requirements
- Windows 7 or later
- Google Chrome browser installed
- ChromeDriver matching your Chrome version

## Installation
1. Download the `svg_to_gif_converter.exe` file from the provided release link.
2. Download ChromeDriver that matches your Google Chrome version from [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads).
3. Place the ChromeDriver executable (chromedriver.exe) in the same folder as `svg_to_gif_converter.exe`.

## Using the Converter
1. Double-click on `svg_to_gif_converter.exe` to run the program.
2. In the application window:
   - Click "Browse" next to "Select SVG file" to choose your input SVG file.
   - Click "Browse" next to "Select output GIF file" to specify where to save the output GIF.
   - Choose a resolution from the dropdown menu, or select "Custom" to enter your own dimensions.
   - If you selected "Custom", enter the desired width and height in pixels.
   - Adjust the "Duration (ms)" to set how long the animation should last (in milliseconds).
   - Set the number of "Frames" to control how smooth the animation will be.
3. Click "Convert" to start the conversion process.
4. Wait for the conversion to complete. A success message will appear when finished.

## Running from Source (for developers)
1. Ensure Python 3.7 or later is installed.
2. Clone the repository or download the source code.
3. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Ensure ChromeDriver is in your system PATH or in the script's directory.
5. Run the script:
   ```
   python svg_to_gif_converter.py
   ```

## Troubleshooting
- If you get an error about ChromeDriver, make sure it's in the same folder as the .exe and matches your Chrome version.
- If the application doesn't open, try running it as administrator.
- For any issues, check the console output for error messages.

## Notes
- The first run may take longer as Windows security checks the application.
- Some antivirus software may flag the .exe. This is a false positive due to how PyInstaller packages Python applications.

For further assistance ask claude :-)
