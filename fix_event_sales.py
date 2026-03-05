import re

with open('event_sales_old.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make a copy for backup
html_new = html

# Replace Title
html_new = re.sub(r'<title>.*?\| Simple Plan</title>', '<title>イベント出店 | Simple Plan</title>', html_new)

# Replace Home Link
html_new = re.sub(r'竊・n\s+繝帙・繝縺ｫ謌ｻ繧・', '←\n            ホームに戻る', html_new)

# Replace Hero Title
html_new = re.sub(r'<h2 class="hero-title[^>]*>.*?</h2>', '<h2 class="hero-title font-serif font-extrabold text-stone-900 mb-8 tracking-wider">イベント出店</h2>', html_new)

# Replace H3
html_new = re.sub(r'蜈ｨ蝗ｽ縺ｮ逧・ｧ倥∈縲・br>\s*縺薙□繧上ｊ縺ｮ蜻ｳ繧上＞繧堤峩謗･縺雁ｱ翫￠縲・', '地域に活気を。<br>\n                    「非日常」を彩る、薪窯ピッツァとお料理のライブ感。', html_new)

# Replace Paragraph
html_new = re.sub(r'鬮倡ｴ夐｣溘ヱ繝ｳ蟆る摩.*?讖滉ｼ壹〒縺吶€・', '街のマルシェ、地域のフェスティバル、企業主催の屋外イベントなど、人が集い笑顔が生まれる場所に、私たちが自慢の味とともに出向き、イベントの熱気をさらに高めます。<br><br>\n                    特にご好評いただいているのが、専用のキッチンカーに搭載した「薪窯」で焼き上げる本格ナポリピッツァ。香ばしい薪の香りと迫力のある炎、そして熱々のチーズがとろける様子は、訪れる人々の五感を刺激し、行列ができるほどの人気コンテンツとなります。', html_new, flags=re.DOTALL)

# Replace Info Header
html_new = re.sub(r'蜃ｺ蠎励・縺比ｾ晞ｼ繝ｻ縺雁撫縺・粋繧上○', 'イベント出店のご依頼・お問い合わせ', html_new)

# Replace Contact text
html_new = re.sub(r'蛯ｬ莠句・蠎励・縺比ｾ晞ｼ縺ｪ縺ｩ縺ｫ縺､縺阪∪縺励※縺ｯ縲√∪縺壹・縺企崕隧ｱ縺ｫ縺ｦ縺頑ｰ苓ｻｽ縺ｫ縺秘€｣邨｡縺上□縺輔＞縲・br>', 'イベント出店のご依頼などにつきましては、まずはお電話にてお気軽にご連絡ください。<br>', html_new)

html_new = re.sub(r'蜷・ヶ繝ｩ繝ｳ繝峨・譛€譁ｰ諠・ｱ縺ｯ蜈ｬ蠑終nstagram縺ｫ縺ｦ髫乗凾逋ｺ菫｡縺励※縺翫ｊ縺ｾ縺吶€・', '各ブランドの最新情報は公式Instagramにて随時発信しております。', html_new)

# Replace tags
html_new = html_new.replace('Prugna Pane 蜈ｬ蠑終G', 'Prugna Pane 公式IG')
html_new = html_new.replace('Torte No Sanpo 蜈ｬ蠑終G', 'Torte No Sanpo 公式IG')

with open('event_sales.html', 'w', encoding='utf-8') as f:
    f.write(html_new)
