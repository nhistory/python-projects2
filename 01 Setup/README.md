### 1. Install selenium with `pip` package installer.

```shell
pip3 install selenium
```

### 2. Test the selenium setup.

```python
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://selenium.dev/')
```

Download [Chrome Driver](https://chromedriver.chromium.org/downloads) file and move into PATH location. If there is an ```“chromedriver” cannot be opened because the developer cannot be verified.``` error, you can fix this by [privacy](https://exerror.com/error-chromedriver-cannot-be-opened-because-the-developer-cannot-be-verified-unable-to-launch-the-chrome-browser/) setting.
