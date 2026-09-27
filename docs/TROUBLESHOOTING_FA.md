# رفع اشکال سریع

## `jupyter: command not found`

ابتدا محیط مجازی را فعال و سپس اجرا کنید:

```bash
python -m pip install -r requirements.txt
python -m jupyter lab
```

## Persian text looks broken in terminal

ابتدا بررسی کنید فایل UTF-8 است. سپس:

```bash
python scripts/check_environment.py
```

در برخی terminalها مشکل فقط مربوط به نمایش RTL است و الزاماً به معنی خراب بودن Unicode string نیست.

## notebook سلول‌ها را با ترتیب عجیب اجرا کرده است

Kernel را restart و سپس **Run All** کنید. notebook پژوهشی باید از یک kernel تمیز از بالا به پایین اجرا شود.

## خروجی `len()` با تعداد «حروفی که می‌بینم» یکی نیست

`len()` تعداد code pointهای موجود در Python string را می‌شمارد، نه الزاماً تعداد graphemeهای ادراکی. combining marks و برخی توالی‌های Unicode می‌توانند تفاوت ایجاد کنند.

## `NFC`، `ي` را به `ی` تبدیل نکرد

این رفتار درست است. `ي` و `ی` دو code point مستقل‌اند و canonical equivalent نیستند. تبدیل آن‌ها یک تصمیم language-specific است.

## ZWNJ را نمی‌بینم

ZWNJ با کد `U+200C` یک نویسه‌ی نامرئی است. از `repr()` یا `ord()` و `unicodedata.name()` برای بررسی آن استفاده کنید.
