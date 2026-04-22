import os
site = r'C:\Users\Administrator\github\fateandmethod-site'
hubs = [
    ('liuyao-index.html', 'liuyao.html'),
    ('meihua-index.html', 'meihua.html'),
    ('daliuren-index.html', 'daliuren.html'),
    ('xuankong-index.html', 'xuankong.html'),
    ('taiyi-index.html', 'taiyi.html'),
    ('xiaoliuren-index.html', 'xiaoliuren.html'),
]
for hub, article in hubs:
    fpath = os.path.join(site, hub)
    with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
        c = f.read()
    btn_search = '<a href="./' + hub + '" class="btn">'
    if btn_search in c:
        c = c.replace(btn_search, '<a href="./' + article + '" class="btn">')
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
        print('Fixed: ' + hub + ' btn -> ' + article)
    else:
        idx = c.find('class="btn"')
        if idx >= 0:
            snippet = c[max(0,idx-60):idx+40]
            print('Current btn in ' + hub + ': ' + repr(snippet))
        else:
            print('No btn found in ' + hub)
