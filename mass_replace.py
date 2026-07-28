#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Масова заміна текстів у всіх HTML файлах
Переписування від клініки до особистого кабінету Юлії Антіпової
"""

import os
import glob

# Словник замін
replacements = {
    # Основні
    "Ми надаємо": "Я надаю",
    "ми надаємо": "я надаю",
    "Ми пропонуємо": "Я пропоную",
    "ми пропонуємо": "я пропоную",
    "Ми віддані": "Я віддана",
    "ми віддані": "я віддана",
    "Ми використовуємо": "Я використовую",
    "ми використовуємо": "я використовую",
    "Ми пишаємося": "Я пишаюся",
    "ми пишаємося": "я пишаюся",
    "Наші послуги": "Мої послуги",
    "наші послуги": "мої послуги",
    "Наших послуг": "Моїх послуг",
    "наших послуг": "моїх послуг",
    "Про нас": "Про мене",
    "про нас": "про мене",
    "Наша команда": "Я, Юлія Антіпова",
    "наша команда": "я, Юлія Антіпова",
    "нашими спеціалістами": "зі мною",
    "наших спеціалістів": "мене",
    "наших досвідчених спеціалістів": "мене",
    "Наші досвідчені спеціалісти": "Я",
    "наші досвідчені спеціалісти": "я",
    "досвідчені спеціалісти": "досвідчений косметолог",
    "Досвідчені спеціалісти": "Досвідчений косметолог",
    "експертні дерматологи": "професійний косметолог",
    "Експертні дерматологи": "Професійний косметолог",
    "Чому обирають нас": "Чому обирають мене",
    "чому обирають нас": "чому обирають мене",
    "пацієнтів": "клієнтів",
    "пацієнти": "клієнти",
    "Пацієнтів": "Клієнтів",
    "Пацієнти": "Клієнти",
    "задоволених пацієнтів": "задоволених клієнтів",
    "Задоволених пацієнтів": "Задоволених клієнтів",
    "Задоволення пацієнтів": "Задоволення клієнтів",
    "задоволення пацієнтів": "задоволення клієнтів",
    "Про клініку": "Косметологічний кабінет Юлії Антіпової",
    "про клініку": "косметологічний кабінет Юлії Антіпової",
    "клініку": "кабінет",
    "клініки": "кабінету",
    "клініці": "кабінеті",
    "клініка": "кабінет",
    "Зв'яжіться з нашими": "Зв'яжіться зі мною",
    "зв'яжіться з нашими": "зв'яжіться зі мною",
    "Проконсультуйтеся з нашими спеціалістами": "Запишіться на консультацію",
    "проконсультуйтеся з нашими спеціалістами": "запишіться на консультацію",
    "Зв'яжіться з нами": "Зв'яжіться зі мною",
    "зв'яжіться з нами": "зв'яжіться зі мною",
    "команди": "косметолога",
    "Команди": "Косметолога",
    "Деталі команди": "Детальніше",
    "деталі команди": "детальніше",
    "Наша": "Моя",
    "наша": "моя",
    "Наші": "Мої",
    "наші": "мої",
    "Наших": "Моїх",
    "наших": "моїх",
    "Нашу": "Мою",
    "нашу": "мою",
    "нашої": "моєї",
    "Нашої": "Моєї",
    "персоналізованого догляду": "індивідуального підходу до кожного клієнта",
    "Персоналізованого догляду": "Індивідуального підходу до кожного клієнта",
    "персоналізовані": "індивідуальні",
    "Персоналізовані": "Індивідуальні",
    "персоналізований": "індивідуальний",
    "Персоналізований": "Індивідуальний",
    "дерматологічні": "косметологічні",
    "Дерматологічні": "Косметологічні",
    "дерматології": "косметології",
    "Дерматології": "Косметології",
    "дерматологу": "косметологу",
    "Дерматологу": "Косметологу",
    "We are": "Я",
    "we are": "я",
    "Our team": "Я",
    "our team": "я",
    "We offer": "Я пропоную",
    "we offer": "я пропоную",
    "We provide": "Я надаю",
    "we provide": "я надаю",
    "Our services": "Мої послуги",
    "our services": "мої послуги",
    "About Us": "Про мене",
    "about us": "про мене",
    "Our clinic": "Мій кабінет",
    "our clinic": "мій кабінет",
    "Contact us": "Зв'яжіться зі мною",
    "contact us": "зв'яжіться зі мною",
}

# Список HTML файлів для обробки
html_files = [
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

def replace_in_file(file_path, replacements):
    """Виконує заміну тексту у файлі"""
    try:
        # Читаємо файл
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        replacements_made = 0

        # Виконуємо всі заміни
        for old_text, new_text in replacements.items():
            count = content.count(old_text)
            if count > 0:
                content = content.replace(old_text, new_text)
                replacements_made += count

        # Записуємо назад тільки якщо були зміни
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return replacements_made

        return 0

    except Exception as e:
        print(f"[ERROR] Pomilka pry obrobci {file_path}: {e}")
        return 0

def main():
    """Головна функція"""
    print("=" * 70)
    print("MASOVA ZAMINA TEKSTIV U HTML FAYLAX")
    print("Perepysuvannya vid kliniky do kabinetu Yulii Antipovoyi")
    print("=" * 70)
    print()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    total_replacements = 0
    processed_files = 0

    for filename in html_files:
        file_path = os.path.join(script_dir, filename)

        if os.path.exists(file_path):
            replacements_count = replace_in_file(file_path, replacements)
            if replacements_count > 0:
                print(f"[OK] {filename:30} - {replacements_count:3} zamin")
                processed_files += 1
                total_replacements += replacements_count
            else:
                print(f"[--] {filename:30} - bez zmin")
        else:
            print(f"[!!] {filename:30} - fayl ne znayideno")

    print()
    print("=" * 70)
    print(f"ZAVERSHENO!")
    print(f"Obrobleno fayliv: {processed_files}/{len(html_files)}")
    print(f"Vsogo zamin: {total_replacements}")
    print("=" * 70)

if __name__ == "__main__":
    main()
