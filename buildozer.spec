[app]

title = Frahoosh
package.name = frahoosh
package.domain = ir.frahoosh

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,json,atlas,ttf,otf

version = 1.0.0

requirements = python3==3.11.10,kivy

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


[buildozer]

log_level = 2
warn_on_root = 1
