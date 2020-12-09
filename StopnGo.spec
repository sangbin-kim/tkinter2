# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['StopnGo_Main.py'],
             pathex=['C:\\Users\\LG\\Desktop\\python\\venv\\StopnGo'],
             binaries=[],
             datas=[("C:/Users/LG/Desktop/python/venv/Lib/site-packages/plotly/package_data/", "./plotly/package_data")],
             hiddenimports=['pandas', 'tkinter', 'plotly', 'pkg_resources.py2_warn'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='StopnGo_v3.2',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True)
