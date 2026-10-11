# راهنمای نصب و آماده‌سازی محیط

## &#x2067;گزینهٔ پیشنهادی: محیط مجازی Python&#x2069;

از ریشهٔ مخزن:

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
jupyter lab
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
jupyter lab
```

## بررسی سریع

```bash
python scripts/check_environment.py
```

&#x2067;پیش‌نیاز: Python **3.10 یا جدیدتر**؛ خروجی باید بررسی Unicode و اطلاعات نسخهٔ Python را نشان دهد.&#x2069;

## اجرای جلسهٔ ۰۲

&#x2067;Notebook را در JupyterLab از مسیر &#x2066;`sessions/02_regex_preprocessing/`&#x2069; باز کنید. فایل &#x2066;`data/raw_persian_messages.txt`&#x2069; باید زیر همان پوشه وجود داشته باشد؛ مسیر داخل notebook نسبت به **working directory notebook** نوشته شده است.&#x2069;

&#x2067;در Google Colab فایل داده به‌طور خودکار همراه notebook آپلود نمی‌شود؛ باید فایل داده را نیز در پوشهٔ &#x2066;`data/`&#x2069; در محیط Colab کپی/آپلود کنید، یا با اتصال Google Drive مسیر را مطابق نیاز تنظیم کنید. راه پیشنهادی این درس **JupyterLab محلی** است.&#x2069;

## &#x2067;چرا virtual environment؟&#x2069;

&#x2067;وابستگی‌های درس با پروژه‌های دیگر تداخل نمی‌کنند و بازتولید اجرا آسان‌تر می‌شود. جلسهٔ ۰۱ و ۰۲ در سطح محتوا فقط از Python Standard Library استفاده می‌کنند؛ JupyterLab برای اجرای notebook نصب می‌شود.&#x2069;

## &#x2067;Encoding فایل‌ها&#x2069;

&#x2067;تمام فایل‌های متنی مخزن UTF-8 هستند؛ &#x2066;`.editorconfig`&#x2069; و &#x2066;`.gitattributes`&#x2069; برای استانداردسازی تنظیم شده‌اند.&#x2069;
