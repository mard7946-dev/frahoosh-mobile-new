[app]

title = Frahoosh Mobile
package.name = frahooshmobile
package.domain = ir.frahoosh

source.dir = mobile
source.include_exts = py,png,jpg,jpeg,svg,kv,json,txt,ttf
source.exclude_dirs = __pycache__,.git,bin,.buildozer,tests

version = 1.0.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0


# ============================================================
# Android
# ============================================================

android.api = 35
android.minapi = 24

android.ndk = 28c
android.ndk_api = 24

# فعلاً فقط معماری اصلی و پایدار اندروید
android.archs = arm64-v8a

android.permissions = INTERNET
android.accept_sdk_license = True
android.skip_update = 0


# ============================================================
# Python-for-Android
# ============================================================

# استفاده از Release پایدار، نه develop
p4a.branch = master
p4a.commit = 58d2114


# ============================================================
# Buildozer
# ============================================================

[buildozer]

log_level = 2
warn_on_root = 0

