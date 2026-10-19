# &#x2067;آزمایشگاه پردازش زبان — Language Processing Laboratory&#x2069;

> مخزن آموزشی دانشجویان | محتوای جلسات به‌تدریج در دسترس قرار می‌گیرد.

این مخزن برای آزمایشگاه کارشناسی پردازش زبان طراحی شده است. تمرکز درس بر یادگیری عملی، کدنویسی قابل بازتولید، تحلیل داده‌های زبانی و توجه ویژه به ویژگی‌های زبان فارسی است.

## جلسات منتشرشده

| محتوای جلسه | موضوع | جلسه |
| ---: | ---: | ---: |
| [01_foundations](sessions/01_foundations/session01_persian_nlp_foundations.ipynb) · [README](sessions/01_foundations/README.md) | &#x2067;مبانی پردازش متن فارسی: &#x2066;`Unicode`&#x2069;، &#x2066;`UTF-8`&#x2069;، &#x2066;`ZWNJ`&#x2069; و ممیزی داده&#x2069; | **۰۱** |
| [02_regex_preprocessing](sessions/02_regex_preprocessing/session02_persian_regex_preprocessing.ipynb) · [README](sessions/02_regex_preprocessing/README.md) | &#x2067;عبارت‌های منظم (&#x2066;`regex`&#x2069;)، استخراج الگو، مدیریت فاصله‌ها و پیش‌پردازش نظام‌مند متن فارسی&#x2069; | **۰۲** |
| [03_tokenization](sessions/03_tokenization/session03_persian_tokenization.ipynb) · [README](sessions/03_tokenization/README.md) | &#x2067;توکن‌سازی فارسی: فاصله‌به‌فاصله، مرز واژه، و BPE مبتنی بر بایت؛ مقایسهٔ واژه و زیرواژه&#x2069; | **۰۳** |

## شروع سریع

&#x2067;Python **3.10 یا جدیدتر** توصیه می‌شود. از ریشهٔ مخزن:&#x2069;

```bash
python -m pip install -r requirements.txt
python scripts/check_environment.py
jupyter lab
```

اگر برای اولین‌بار محیط را نصب می‌کنید: [راهنمای کامل نصب](docs/SETUP_FA.md).

&#x2067;**برای جلسهٔ ۰۲، فایل** &#x2066;`sessions/02_regex_preprocessing/data/raw_persian_messages.txt`&#x2069; **را در کنار notebook نگه دارید.** برای جلسهٔ ۰۳ هر دو فایل `sessions/03_tokenization/data/` باید موجود باشند. هر notebook را در JupyterLab از پوشهٔ خودش اجرا کنید.&#x2069;

## قوانین مهم دانشجو

1. &#x2067;فایل starter جلسهٔ مربوط را کامل کرده و با نام &#x2066;`STUDENT_ID_sessionXX.ipynb`&#x2069; ذخیره کنید (مانند &#x2066;`STUDENT_ID_session02.ipynb`&#x2069;).&#x2069;
2. &#x2067;قبل از تحویل، **Restart Kernel and Run All Cells** را اجرا کنید.&#x2069;
3. &#x2067;بخش‌های &#x2066;`TODO`&#x2069;، آزمون‌های عمومی و پاسخ‌های تشریحی را بررسی کنید.&#x2069;
4. &#x2067;**فایل حل‌شدهٔ خود را در GitHub عمومی منتشر نکنید.**&#x2069;
5. &#x2067;استفاده از منابع و AI باید مطابق سیاست درس اعلام شود.&#x2069;

راهنماها:

- [روش تحویل](docs/SUBMISSION_FA.md)
- &#x2067;[سیاست استفاده از AI](docs/AI_USE_POLICY_FA.md)&#x2069;
- [صداقت علمی](docs/ACADEMIC_INTEGRITY_FA.md)
- [رفع اشکال](docs/TROUBLESHOOTING_FA.md)
- [واژه‌نامهٔ درس](docs/GLOSSARY_FA.md)
- [گزارش اشکال و پیشنهاد اصلاح](CONTRIBUTING.md)

---

## English summary

A public student repository for a **120-minute-per-session undergraduate Language Processing Laboratory** focused on Persian NLP. Only released materials are available. Session 01 teaches Unicode/ZWNJ/data hygiene; Session 02 teaches regular expressions and reproducible, task-aware preprocessing. Session 03 compares whitespace, Unicode/Persian word boundaries and byte-level BPE with distinct word-span and subword evaluation protocols.

Student submissions and solution notebooks must **not** be posted publicly.
