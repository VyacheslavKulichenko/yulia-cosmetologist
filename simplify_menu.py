#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
from pathlib import Path

# Визначити кодування для виводу
if sys.stdout.encoding is None:
    sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

# Базова директорія проекту
BASE_DIR = r"D:\3. My Projects\14. Front-end Projects\2. HTML template\2. Work Project\Dermatologist & Cosmetology\html"

# Список всіх файлів для обробки
HTML_FILES = [
    "index.html",
    "index-2.html",
    "index-3.html",
    "about.html",
    "services.html",
    "service-single.html",
    "blog.html",
    "blog-single.html",
    "contact.html",
    "book-appointment.html",
    "team.html",
    "team-single.html",
    "pricing.html",
    "case-study.html",
    "case-study-single.html",
    "testimonials.html",
    "image-gallery.html",
    "video-gallery.html",
    "faqs.html",
    "404.html"
]

# Стара навігація для пошуку
OLD_MENU_PATTERN = r'''<li class="nav-item submenu"><a class="nav-link" href="./">Головна</a>\s*<ul>\s*<li class="nav-item"><a class="nav-link" href="index\.html">Головна - Версія 1</a></li>\s*<li class="nav-item"><a class="nav-link" href="index-2\.html">Головна - Версія 2</a></li>\s*<li class="nav-item"><a class="nav-link" href="index-3\.html">Головна - Версія 3</a></li>\s*</ul>\s*</li>\s*<li class="nav-item"><a class="nav-link" href="about\.html">Про мене</a>\s*<li class="nav-item"><a class="nav-link" href="services\.html">Послуги</a></li>\s*<li class="nav-item"><a class="nav-link" href="blog\.html">Блог</a></li>\s*<li class="nav-item submenu"><a class="nav-link" href="#">Сторінки</a>\s*<ul>.*?</ul>\s*</li>\s*<li class="nav-item"><a class="nav-link" href="contact\.html">Контакти</a></li>\s*<li class="nav-item highlighted-menu"><a href="book-appointment\.html">Записатися на прийом</a></li>'''

# Нова навігація
NEW_MENU = '''<li class="nav-item"><a class="nav-link" href="index.html">Головна</a></li>
                                    <li class="nav-item"><a class="nav-link" href="services.html">Послуги</a></li>
                                    <li class="nav-item"><a class="nav-link" href="contact.html">Контакти</a></li>
                                    <li class="nav-item highlighted-menu"><a href="book-appointment.html">Записатися на прийом</a></li>'''

# Старий footer
OLD_FOOTER_QUICK_LINKS = r'''<h2>Швидкі посилання</h2>\s*<ul>\s*<li><a href="index\.html">Головна</a></li>\s*<li><a href="about\.html">Про мене</a></li>\s*<li><a href="services\.html">Послуги</a></li>\s*<li><a href="testimonials\.html">Відгуки</a></li>\s*<li><a href="contact\.html">Контакти</a></li>\s*</ul>'''

# Новий footer
NEW_FOOTER_QUICK_LINKS = '''<h2>Швидкі посилання</h2>
                            <ul>
                                <li><a href="index.html">Головна</a></li>
                                <li><a href="services.html">Послуги</a></li>
                                <li><a href="contact.html">Контакти</a></li>
                                <li><a href="book-appointment.html">Записатися на прийом</a></li>
                            </ul>'''

def simplify_menu(file_path):
    """Спрощує навігаційне меню у файлу"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Замінити навігацію - більш гнучкий підхід
    # Ищемо весь блок меню
    menu_pattern = r'<li class="nav-item submenu"><a class="nav-link" href="./">Головна</a>\s*<ul>\s*<li class="nav-item"><a class="nav-link" href="index\.html">Головна - Версія 1</a></li>\s*<li class="nav-item"><a class="nav-link" href="index-2\.html">Головна - Версія 2</a></li>\s*<li class="nav-item"><a class="nav-link" href="index-3\.html">Головна - Версія 3</a></li>\s*</ul>\s*</li>\s*<li class="nav-item"><a class="nav-link" href="about\.html">Про мене</a>\s*</li>?\s*<li class="nav-item"><a class="nav-link" href="services\.html">Послуги</a></li>\s*<li class="nav-item"><a class="nav-link" href="blog\.html">Блог</a></li>\s*<li class="nav-item submenu"><a class="nav-link" href="#">Сторінки</a>\s*<ul>.*?</ul>\s*</li>\s*<li class="nav-item"><a class="nav-link" href="contact\.html">Контакти</a></li>\s*<li class="nav-item highlighted-menu"><a href="book-appointment\.html">Записатися на прийом</a></li>'

    content = re.sub(menu_pattern, NEW_MENU, content, flags=re.DOTALL)

    # Замінити footer
    footer_pattern = r'<h2>Швидкі посилання</h2>\s*<ul>\s*<li><a href="index\.html">Головна</a></li>\s*<li><a href="about\.html">Про мене</a></li>\s*<li><a href="services\.html">Послуги</a></li>\s*<li><a href="testimonials\.html">Відгуки</a></li>\s*<li><a href="contact\.html">Контакти</a></li>\s*</ul>'

    content = re.sub(footer_pattern, NEW_FOOTER_QUICK_LINKS, content, flags=re.DOTALL)

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    print("=" * 80)
    print("SPROSHENNA NAVIGACIJNOHO MENU TA FOOTER")
    print("=" * 80)

    processed_files = []
    failed_files = []

    for html_file in HTML_FILES:
        file_path = os.path.join(BASE_DIR, html_file)

        if not os.path.exists(file_path):
            print(f"[ERROR] POMILKA: {html_file} - fail ne znajdeno")
            failed_files.append(html_file)
            continue

        try:
            if simplify_menu(file_path):
                print(f"[OK] USPISHNO: {html_file} - menu ta footer sprosheno")
                processed_files.append(html_file)
            else:
                print(f"[!!] PROPUSHENO: {html_file} - menu ne znajdeno (mozhlivo vzhe sprosheno)")
                failed_files.append(html_file)
        except Exception as e:
            print(f"[ERROR] POMILKA: {html_file} - {str(e)}")
            failed_files.append(html_file)

    print("\n" + "=" * 80)
    print("ZVIT")
    print("=" * 80)
    print(f"Vsogo failiv: {len(HTML_FILES)}")
    print(f"Uspishno obroblenо: {len(processed_files)}")
    print(f"Problemni failи: {len(failed_files)}")

    if processed_files:
        print("\nObroblenі failи:")
        for f in processed_files:
            print(f"  - {f}")

    if failed_files:
        print("\nProblemnі failу:")
        for f in failed_files:
            print(f"  - {f}")

    print("\n" + "=" * 80)

if __name__ == "__main__":
    main()
