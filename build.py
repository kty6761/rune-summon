"""runes/ 폴더의 PNG를 WebP base64로 변환해 src 템플릿에 넣고, dist/index.html 한 파일로 만듭니다.
사용: pip install pillow  →  python build.py
"""
import base64, io, json, os
from PIL import Image

ROOT = os.path.dirname(os.path.abspath(__file__))
imgs = {}
for f in sorted(os.listdir(os.path.join(ROOT, 'runes'))):
    if not f.lower().endswith('.png'):
        continue
    im = Image.open(os.path.join(ROOT, 'runes', f)).convert('RGBA').resize((168, 168), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, 'WEBP', quality=86, method=6)
    imgs[f[:-4]] = 'data:image/webp;base64,' + base64.b64encode(buf.getvalue()).decode()

src = open(os.path.join(ROOT, 'src', 'index.template.html'), encoding='utf-8').read()
assert '/*__IMG__*/{}' in src, '템플릿에 /*__IMG__*/{} 자리표시자가 없습니다'
out = src.replace('/*__IMG__*/{}', json.dumps(imgs, ensure_ascii=False))
os.makedirs(os.path.join(ROOT, 'dist'), exist_ok=True)
open(os.path.join(ROOT, 'dist', 'index.html'), 'w', encoding='utf-8').write(out)
print(f'{len(imgs)}개 룬 이미지 포함 → dist/index.html ({len(out)//1024} KB)')
