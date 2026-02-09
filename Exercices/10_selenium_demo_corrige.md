Corrige - selenium_demo

1) Options
```python
options.add_argument('--disable-gpu')
```

2) Screenshot
```python
import time
name = f"example_{int(time.time())}.png"
driver.save_screenshot(name)
```

3) Selection CSS
```python
from selenium.webdriver.common.by import By
links = driver.find_elements(By.CSS_SELECTOR, 'a')
print([a.get_attribute('href') for a in links])
```

4) Firefox
```bash
BROWSER=firefox python run_headless.py
```

5) Test
```python
options = build_chrome_options(headless=True)
assert '--window-size=1280,800' in options.arguments
```

