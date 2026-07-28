#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys

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

# Нова навігація
NEW_MENU = '''<li class="nav-item"><a class="nav-link" href="index.html">Головна</a></li>
                                    <li class="nav-item"><a class="nav-link" href="services.html">Послуги</a></li>
                                    <li class="nav-item"><a class="nav-link" href="contact.html">Контакти</a></li>
                                    <li class="nav-item highlighted-menu"><a href="book-appointment.html">Записатися на прийом</a></li>'''

# Новий footer
NEW_FOOTER_QUICK_LINKS = '''<h2>Швидкі посилання</h2>
                            <ul>
                                <li><a href="index.html">Головна</a></li>
                                <li><a href="services.html">Послуги</a></li>
                                <li><a href="contact.html">Контакти</a></li>
                                <li><a href="book-appointment.html">Записатися на прийом</a></li>
                            </ul>'''

def simplify_menu(file_path):
    """Спрощує навігаційне меню та footer у файлу"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    menu_found = False
    footer_found = False

    # ===== Замінити навігацію =====
    # Використовуємо greedy match від першого li до останнього
    menu_pattern = r'<li class="nav-item submenu"><a class="nav-link" href="./">Головна</a>.*?<li class="nav-item highlighted-menu"><a href="book-appointment\.html">Записатися на прийом</a></li>'

    if re.search(menu_pattern, content, re.DOTALL):
        menu_found = True
        content = re.sub(menu_pattern, NEW_MENU, content, count=1, flags=re.DOTALL)

    # ===== Замінити footer =====
    footer_pattern = r'<h2>Швидкі посилання</h2>\s*<ul>\s*<li><a href="index\.html">Головна</a></li>\s*<li><a href="about\.html">Про мене</a></li>\s*<li><a href="services\.html">Послуги</a></li>\s*<li><a href="testimonials\.html">Відгуки</a></li>\s*<li><a href="contact\.html">Контакти</a></li>\s*</ul>'

    if re.search(footer_pattern, content, re.DOTALL):
        footer_found = True
        content = re.sub(footer_pattern, NEW_FOOTER_QUICK_LINKS, content, count=1, flags=re.DOTALL)

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return menu_found, footer_found

    return False, False

def main():
    print("=" * 80)
    print("SPROSHENNA NAVIGACIJNOHO MENU TA FOOTER")
    print("=" * 80)
    print()

    processed_files = []
    failed_files = []

    for html_file in HTML_FILES:
        file_path = os.path.join(BASE_DIR, html_file)

        if not os.path.exists(file_path):
            print("[ERROR] {0} - fail ne znajdeno".format(html_file))
            failed_files.append(html_file)
            continue

        try:
            menu_found, footer_found = simplify_menu(file_path)
            if menu_found or footer_found:
                parts = []
                if menu_found:
                    parts.append("menu")
                if footer_found:
                    parts.append("footer")
                print("[OK] {0} - sprosheno: {1}".format(html_file, ", ".join(parts)))
                processed_files.append(html_file)
            else:
                print("[!!] {0} - nichogo ne zaminyeno".format(html_file))
                failed_files.append(html_file)
        except Exception as e:
            print("[ERROR] {0} - {1}".format(html_file, str(e)))
            failed_files.append(html_file)

    print()
    print("=" * 80)
    print("ZVIT")
    print("=" * 80)
    print("Vsogo failiv: {0}".format(len(HTML_FILES)))
    print("Uspishno obrobleno: {0}".format(len(processed_files)))
    print("Problemni failи: {0}".format(len(failed_files)))
    print()

    if processed_files:
        print("Obrobleni failы:")
        for f in processed_files:
            print("  [OK] {0}".format(f))
        print()

    if failed_files:
        print("Problemnі failу (ne obrobleni):")
        for f in failed_files:
            print("  [!!] {0}".format(f))
        print()

    print("=" * 80)

if __name__ == "__main__":
    main()
