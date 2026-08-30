[app]

title = Frahoosh
package.name = frahoosh
package.domain = ir.frahoosh

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,json,atlas,ttf,otf

version = 1.0.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.api = 35
android.minapi = 24

android.ndk = 28c
android.ndk_api = 24

android.archs = arm64-v8a

android.accept_sdk_license = True

android.permissions = INTERNET,ACCESS_NETWORK_STATE

android.enable_androidx = True

p4a.bootstrap = sdl2

# ============================================================
# IMPORTANT:
# Fix for charset-normalizer / Python 3.14 Android wheels
# Merged upstream in python-for-android PR #3366
# ============================================================

p4a.fork = kivy
p4a.branch = develop
p4a.commit = 5865575

[buildozer]

log_level = 2
warn_on_root = 1
