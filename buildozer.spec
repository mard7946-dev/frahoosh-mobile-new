[app]

title = Frahoosh
package.name = frahoosh
package.domain = ir.frahoosh

source.dir = mobile

source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt,ttf,otf,ico

source.exclude_exts = spec

source.exclude_dirs = bin,.buildozer,.git,__pycache__,tests

version = 1.0.0

requirements = python3,kivy,requests

orientation = portrait

fullscreen = 0

android.api = 35
android.minapi = 24

android.ndk = 28c
android.ndk_api = 24

android.archs = arm64-v8a

android.private_storage = True

android.permissions = INTERNET,ACCESS_NETWORK_STATE

android.enable_androidx = True

android.entrypoint = org.kivy.android.PythonActivity

p4a.bootstrap = sdl2


[buildozer]

log_level = 2
warn_on_root = 1
