#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для масової заміни у HTML файлах:
1. Заміна "Dermix" на "Юля косметолог"
2. Заміна всіх номерів телефонів на +38050-020-83-84
"""

import os
import re
from pathlib import Path

# Список файлів для обробки
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

def replace_dermix(content):
    """Заміна Dermix на Юля косметолог"""
    # Заміна "Dermix" (з великої літери)
    content = content.replace("Dermix", "Юля косметолог")
    # Заміна "dermix" (з малої літери)
    content = content.replace("dermix", "Юля косметолог")
    # Заміна "DERMIX" (всі великі)
    content = content.replace("DERMIX", "Юля косметолог")
    return content

def replace_phone_numbers(content):
    """Заміна всіх номерів телефонів на +38050-020-83-84"""

    # Словник замін для різних варіантів телефонів
    phone_replacements = {
        # Точні збіги у тексті
        "+123 456 789": "+38050-020-83-84",
        "+1 123 456 789": "+38050-020-83-84",
        "123 456 789": "+38050-020-83-84",
        "123456789": "+38050-020-83-84",

        # У атрибутах href
        "tel:123456789": "tel:+380500208384",
        "tel:+123456789": "tel:+380500208384",
        "tel:+1123456789": "tel:+380500208384",
    }

    # Виконуємо прості заміни
    for old_phone, new_phone in phone_replacements.items():
        content = content.replace(old_phone, new_phone)

    # Додаткові регулярні вирази для виявлення інших форматів телефонів
    # Шукаємо шаблони типу: +X XXX XXX XXX або подібні
    patterns = [
        (r'\+\d{1,3}\s?\d{3}\s?\d{3}\s?\d{3}', '+38050-020-83-84'),  # +X XXX XXX XXX
        (r'tel:\+?\d{9,15}', 'tel:+380500208384'),  # tel:XXXXXXXXX
    ]

    for pattern, replacement in patterns:
        # Перевіряємо, чи вже не замінили на наш номер
        matches = re.findall(pattern, content)
        for match in matches:
            if '+38050' not in match and '+380500208384' not in match:
                content = content.replace(match, replacement)

    return content

def process_html_file(file_path):
    """Обробка одного HTML файлу"""
    try:
        # Читаємо файл
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Виконуємо заміни
        content = replace_dermix(content)
        content = replace_phone_numbers(content)

        # Записуємо назад тільки якщо були зміни
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"[+] Updated: {os.path.basename(file_path)}")
            return True
        else:
            print(f"[o] No changes: {os.path.basename(file_path)}")
            return False

    except Exception as e:
        print(f"[x] Error processing {os.path.basename(file_path)}: {e}")
        return False

def main():
    """Головна функція"""
    print("=" * 60)
    print("Mass replacement in HTML files")
    print("=" * 60)
    print("\nTASK 1: Replace 'Dermix' -> 'Yulia kosmetoloh'")
    print("TASK 2: Replace phones -> '+38050-020-83-84'\n")
    print("-" * 60)

    # Отримуємо поточну директорію скрипта
    script_dir = Path(__file__).parent

    updated_count = 0

    # Обробляємо кожен файл
    for filename in HTML_FILES:
        file_path = script_dir / filename

        if file_path.exists():
            if process_html_file(file_path):
                updated_count += 1
        else:
            print(f"[x] File not found: {filename}")

    print("-" * 60)
    print(f"\nResult: Updated {updated_count} of {len(HTML_FILES)} files")
    print("=" * 60)

if __name__ == "__main__":
    main()
