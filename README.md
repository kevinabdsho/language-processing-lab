# آزمایشگاه پردازش زبان — Language Processing Laboratory

> مخزن عمومی دانشجویان — **فقط مطالب منتشرشده‌ی درس در این مخزن قرار می‌گیرد.**

این مخزن برای آزمایشگاه کارشناسی پردازش زبان طراحی شده است. تمرکز درس بر یادگیری عملی، کدنویسی قابل بازتولید، تحلیل داده‌های زبانی و توجه ویژه به ویژگی‌های زبان فارسی است.

## جلسه‌ی منتشرشده

### جلسه ۰۱ — مبانی پردازش متن فارسی

**Foundations for Persian NLP: Jupyter, UTF-8, Unicode, and Data Hygiene**

فایل اصلی:

[`sessions/01_foundations/session01_persian_nlp_foundations.ipynb`](sessions/01_foundations/session01_persian_nlp_foundations.ipynb)

در این جلسه با موارد زیر کار می‌کنید:

- اجرای قابل‌بازتولید کد در Jupyter؛
- تفاوت `str`، `bytes`، Unicode و UTF-8؛
- تفاوت نویسه‌های فارسی و عربی مانند `ی/ي` و `ک/ك`؛
- نرمال‌سازی Unicode و تفاوت آن با نرمال‌سازی زبانی؛
- نیم‌فاصله / ZWNJ (`U+200C`)؛
- طراحی یک نرمال‌ساز کوچک، شفاف و قابل‌آزمون؛
- ممیزی کیفیت یک پیکره‌ی کوچک فارسی؛
- `token`، `type` و Type–Token Ratio؛
- تصمیم‌گیری آگاهانه درباره‌ی preprocessing.

## شروع سریع

اگر Python و Jupyter را نصب دارید:

```bash
python -m pip install -r requirements.txt
jupyter lab
```

سپس notebook جلسه ۰۱ را باز کنید.

راهنمای کامل نصب:

[`docs/SETUP_FA.md`](docs/SETUP_FA.md)

بررسی محیط:

```bash
python scripts/check_environment.py
```

## قوانین مهم دانشجو

1. نسخه‌ی starter را تغییر دهید و با نام `STUDENT_ID_session01.ipynb` ذخیره کنید.
2. قبل از تحویل، **Restart Kernel and Run All Cells** را اجرا کنید.
3. notebook نهایی باید بدون خطای syntax اجرا شود.
4. پاسخ‌های تشریحی باید نشان‌دهنده‌ی فهم خود شما باشند.
5. **فایل حل‌شده‌ی خود را در GitHub عمومی منتشر نکنید.**
6. استفاده از منابع و ابزارهای هوش مصنوعی باید مطابق سیاست درس اعلام شود.

راهنماها:

- [روش تحویل](docs/SUBMISSION_FA.md)
- [سیاست استفاده از AI](docs/AI_USE_POLICY_FA.md)
- [صداقت علمی](docs/ACADEMIC_INTEGRITY_FA.md)
- [رفع اشکال](docs/TROUBLESHOOTING_FA.md)
- [واژه‌نامه‌ی جلسه ۰۱](docs/GLOSSARY_FA.md)

## انتشار تدریجی

این مخزن عمداً فقط شامل مطالبی است که مدرس منتشر کرده است. پوشه‌ی جلسه‌های آینده از قبل در مخزن قرار نمی‌گیرد و branch عمومیِ مخفی برای آن‌ها ساخته نمی‌شود.

برای دیدن تغییرات منتشرشده:

[`CHANGELOG.md`](CHANGELOG.md)

## نیازمندی‌ها

برای **خودِ محتوای جلسه ۰۱** فقط Python Standard Library لازم است. `JupyterLab` صرفاً برای اجرای notebook نصب می‌شود.

نسخه‌ی پیشنهادی Python: **3.10 یا جدیدتر**.

## کیفیت مخزن

این مخزن دارای بررسی خودکار GitHub Actions است که:

- ساختار انتشار عمومی را بررسی می‌کند؛
- از وجود نام‌های رایج فایل‌های solution/instructor در commit عمومی جلوگیری می‌کند؛
- notebook را از نظر JSON و syntax بررسی می‌کند؛
- starter notebook را در محیط تمیز اجرا می‌کند.

این بررسی‌ها جایگزین بازبینی مدرس نیستند، اما احتمال اشتباه در انتشار عمومی را کم می‌کنند.

---

## English summary

This is the public student repository for an undergraduate **Language Processing Laboratory** with a strong Persian-NLP component. Only released material is included. Session 01 covers reproducibility, UTF-8/Unicode, Persian-vs-Arabic character variants, ZWNJ, conservative normalization, and corpus-quality auditing.

**Students should not publish completed solution notebooks in public repositories.**
