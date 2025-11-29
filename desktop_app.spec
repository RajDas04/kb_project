<<<<<<< HEAD
from PyInstaller.utils.hooks import collect_data_files
datas = collect_data_files('ckeditor')

block_cipher = None

a = Analysis(['desktop_app.py'],
             pathex=[],
             binaries=[],
             datas=datas,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             cipher=block_cipher)
pyz = PYZ(a.pure)
exe = EXE(pyz, a.scripts, a.binaries, a.zipfiles, a.datas,
=======
from PyInstaller.utils.hooks import collect_data_files
datas = collect_data_files('ckeditor')

block_cipher = None

a = Analysis(['desktop_app.py'],
             pathex=[],
             binaries=[],
             datas=datas,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             cipher=block_cipher)
pyz = PYZ(a.pure)
exe = EXE(pyz, a.scripts, a.binaries, a.zipfiles, a.datas,
>>>>>>> 40a0b34 (update- adding the desktop app)
          name='desktop_app', debug=False, strip=False, upx=True)