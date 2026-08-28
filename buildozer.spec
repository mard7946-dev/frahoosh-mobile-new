[app]
title = Frahoosh Mobile
package.name = frahooshmobile
package.domain = ir.frahoosh
source.dir = mobile
source.include_exts = py,png,jpg,jpeg,svg,kv,json,txt,ttf
source.exclude_dirs = **pycache**,.git,bin,.buildozer,tests
version = 1.0.0
requirements = python3,kivy,requests
orientation = portrait
fullscreen = 0

[android]
android.api = 35
android.minapi = 23
android.ndk = 28c
android.ndk_api = 23
android.archs = arm64-v8a,armeabi-v7a
android.permissions = INTERNET
android.accept_sdk_license = True
android.skip_update = 0

p4a.branch = develop
p4a.commit = HEAD

[buildozer]
log_level = 2
warn_on_root = 0
