# راهنمای نصب و آماده‌سازی محیط

## گزینه‌ی پیشنهادی: محیط مجازی Python

از ریشه‌ی مخزن:

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

خروجی باید نسخه‌ی Python، encoding پیش‌فرض و چند بررسی Unicode را نشان دهد.

## چرا virtual environment؟

محیط مجازی باعث می‌شود وابستگی‌های این درس با پروژه‌های دیگر شما تداخل نداشته باشد و بازتولید محیط ساده‌تر شود.

## اگر از Google Colab استفاده می‌کنید

Notebook جلسه ۰۱ به کتابخانه‌ی خاصی خارج از Python Standard Library وابسته نیست، بنابراین از نظر محتوای Python قابل اجراست. با این حال، برای یادگیری workflow پژوهشی، استفاده از Jupyter و یک محیط محلی یا دانشگاهی توصیه می‌شود.

## Encoding فایل‌ها

تمام فایل‌های متنی این مخزن باید UTF-8 باشند. تنظیمات `.editorconfig` و `.gitattributes` نیز برای کاهش مشکلات encoding در مخزن قرار داده شده‌اند.
