# Scrapdex
An Basic CLI Mangadex Scrapper to download Manga chapters without relying on the official Mangadex API, written in python

## Features
- Downloads manga from a given Mangadex URL([Mangadex](https://mangadex.org))
- Saves downloaded manga to the 'Mangadex' directory in the same directory as the script or executable
- Works correctly when run as a script or as a PyInstaller executable

## Dependencies
- [Python 3.10](https://www.python.org/downloads/release/python-3100/)
- [Firefox](https://www.mozilla.org/en-US/firefox/new/)
- [Geckodriver](https://github.com/mozilla/geckodriver/)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- [Selenium](https://www.selenium.dev)

## Installation
- Download Geckodriver by running this command in your powershell:
  ```shell
  # Get the latest geckodriver version
  $GECKO_VER = Invoke-RestMethod -Uri "https://api.github.com/repos/mozilla/geckodriver/releases/latest" | Select-Object -ExpandProperty tag_name
  
  # Choose the platform (win32, win64)
  $PLATFORM = "win64"
  
  # Construct the download URL
  $URL = "https://github.com/mozilla/geckodriver/releases/download/$GECKO_VER/geckodriver-$GECKO_VER-$PLATFORM.zip"
  
  # Download geckodriver
  Invoke-WebRequest -Uri $URL -OutFile "geckodriver-$GECKO_VER-$PLATFORM.zip"
  ```
- Extract the geckodriver.exe from the zip file.

1) For the python file:
- Clone the repository
- Put geckodriver.exe into the cloned folder
- Navigate to the cloned repository
- Install the required Python packages:
  ```shell
  pip install -r requirements.txt
  ```
- Run the script with Python:
  ```shell
  python Scrapdex.py
  ```
2) For Executable:
- After downloading Geckodriver and putting it into the cloned repository, run the executable from the bin folder normally.
- Geckodriver should be in the parent folder of the bin folder

## Note
- After the manga chapter has downloaded, it will take some time to close all the driver instances and it is necessary to free up some resources.
- So it is recommended to close the window after all the driver instances are closed.
- For now it only works in Windows. If anyone wants a version for linux, please make a new issue or reach out to me.
- For now, it only works with firefox. If a chrome version is needed, please make a new issue or reach out to me.

## Message from the maintainer
- Because I couldn't scrap directly from Mangadex by request(as it doesn't support javascript), I used selenium with firefox webdriver to do it.
- If there is any issue that is unknown, please create a new issue in the issues secion.

## Known Issues:
- Cannot download Webtoons/Vertical format comics
- Is a little slow because of usage of selenium webdriver

## Contributing
Want to add new features? Fix a bug? Made changes to help the app better and faster? Fork the repository and send the Pull Request.

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Disclaimer
Scrapdex and it's maintainer is not affiliated with MangaDex.
