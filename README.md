# Frahoosh Mobile — New Foundation

نسخه جدید مستقل موبایل فراهوش. این پروژه از صفر به‌صورت تمیز و مستقل ساخته شده و برای اتصال به Backend مشترک Frahoosh طراحی شده است.

## اصول
- Android client مستقل از Web
- Backend مشترک با Frahoosh Web
- فقط Supabase publishable/anon key در Client؛ هرگز service_role key داخل APK قرار نمی‌گیرد.
- Login با Supabase Auth
- Session محلی برای حفظ ورود
- ساختار قابل توسعه برای پنل‌های نقش‌محور
- مرکز به‌روزرسانی داخل برنامه

## اجرا
```bash
python -m venv .venv
# activate the venv
pip install -r requirements.txt
python -m mobile.main
```

## تنظیم Backend
متغیرهای `.env.example` را در محیط Build تنظیم کنید. برای اجرای محلی می‌توانید آن‌ها را در محیط shell تعریف کنید.

## Android
```bash
buildozer android debug
```

برای CI، متغیرهای Supabase را به صورت GitHub Actions Secrets/Variables تنظیم کنید و هرگز Secret را commit نکنید.

## وضعیت
این Repository پایه جدید Mobile است. مرحله بعدی، بعد از آماده شدن Supabase Web، تکمیل Role/Profile API و پنل‌های واقعی هر نقش است.
