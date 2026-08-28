[app]

title = Frahoosh Mobile
package.name = frahooshmobile
package.domain = ir.frahoosh

source.dir = mobile
source.include_exts = py,png,jpg,jpeg,svg,kv,json,txt,ttf
source.exclude_dirs = __pycache__,.git,bin,.buildozer,tests

version = 1.0.0

# فقط وابستگی‌های لازم برای خود برنامه
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

android.archs = arm64-v8a,armeabi-v7a

android.permissions = INTERNET
android.accept_sdk_license = True
android.skip_update = 0


# ============================================================
# Python-for-Android
# ============================================================

p4a.branch = develop
p4a.commit = 0382d27


# ============================================================
# Buildozer
# ============================================================

[buildozer]

log_level = 2
warn_on_root = 0
