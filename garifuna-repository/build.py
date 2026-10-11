#!/usr/bin/env python3
"""Builds the static site from src/site.html into index.html + assets/. Run: python3 build.py
All paths are relative, so the site works at a domain root or under a GitHub Pages sub-path."""
import re, os, shutil
src = open('src/site.html', encoding='utf8').read()
shutil.rmtree('assets', ignore_errors=True)
os.makedirs('assets/css'); os.makedirs('assets/js')
css = re.findall(r'<style[^>]*>(.*?)</style>', src, re.S)
open('assets/css/site.css', 'w', encoding='utf8').write('\n'.join(css))
n = [0]
def st(m):
    n[0] += 1
    return '<link rel="stylesheet" href="assets/css/site.css">' if n[0] == 1 else ''
base = re.sub(r'<style[^>]*>.*?</style>', st, src, flags=re.S)
js = [0]
def sc(m):
    a, b = m.group(1), m.group(2)
    if 'ld+json' in a or len(b) < 300:
        return m.group(0)
    js[0] += 1
    fn = 'app-%d.js' % js[0]
    open('assets/js/' + fn, 'w', encoding='utf8').write(b)
    return '<script src="assets/js/%s"></script>' % fn
base = re.sub(r'<script([^>]*)>(.*?)</script>', sc, base, flags=re.S)
open('index.html', 'w', encoding='utf8').write(base)
open('.nojekyll', 'w').write('')
print('built index.html,', js[0], 'scripts')
