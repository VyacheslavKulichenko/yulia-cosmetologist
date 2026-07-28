#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для замены текстов с обращения от группы на обращение от одного косметолога
Автор: Юлія Антіпова
"""

import os
import re
from pathlib import Path

# Список файлов для обработки
HTML_FILES = [
    'index.html', 'index-2.html', 'index-3.html', 'about.html',
    'services.html', 'service-single.html', 'blog.html', 'blog-single.html',
    'contact.html', 'book-appointment.html', 'team.html', 'team-single.html',
    'pricing.html', 'case-study.html', 'case-study-single.html',
    'testimonials.html', 'image-gallery.html', 'video-gallery.html',
    'faqs.html', '404.html'
]

# Словарь замен (порядок важен!)
REPLACEMENTS = [
    # Специальные фразы (должны быть первыми, до простых замен)
    (r'\bНаша команда\b', 'Я'),
    (r'\bнаша команда\b', 'я'),
    (r'\bкоманда спеціалістів\b', 'досвідчений косметолог'),
    (r'\bКоманда спеціалістів\b', 'Досвідчений косметолог'),
    (r'\bЕкспертні дерматологи\b', 'Професійний косметолог'),
    (r'\bекспертні дерматологи\b', 'професійний косметолог'),
    (r'\bдосвідчені спеціалісти\b', 'досвідчений спеціаліст'),
    (r'\bДосвідчені спеціалісти\b', 'Досвідчений спеціаліст'),

    # Существительные (множественное → единственное)
    (r'\bнаша клініка\b', 'мій кабінет'),
    (r'\bНаша клініка\b', 'Мій кабінет'),
    (r'\bспеціалісти\b', 'спеціаліст'),
    (r'\bСпеціалісти\b', 'Спеціаліст'),
    (r'\bексперти\b', 'експерт'),
    (r'\bЕксперти\b', 'Експерт'),
    (r'\bдерматологи\b', 'косметолог'),
    (r'\bДерматологи\b', 'Косметолог'),

    # Footer
    (r'\bПро клініку\b', 'Про мене'),
    (r'\bпро клініку\b', 'про мене'),

    # Местоимения
    (r'\bМи\b', 'Я'),
    (r'\bми\b', 'я'),
    (r'\bНаші\b', 'Мої'),
    (r'\bнаші\b', 'мої'),
    (r'\bнаших\b', 'моїх'),
    (r'\bНаших\b', 'Моїх'),
    (r'\bнас\b', 'мене'),
    (r'\bНас\b', 'Мене'),
    (r'\bнами\b', 'мною'),
    (r'\bНами\b', 'Мною'),
    (r'\bнам\b', 'мені'),
    (r'\bНам\b', 'Мені'),

    # Глаголы (множественное → единственное)
    (r'\bпропонуємо\b', 'пропоную'),
    (r'\bПропонуємо\b', 'Пропоную'),
    (r'\bнадаємо\b', 'надаю'),
    (r'\bНадаємо\b', 'Надаю'),
    (r'\bвикористовуємо\b', 'використовую'),
    (r'\bВикористовуємо\b', 'Використовую'),
    (r'\bвіддані\b', 'віддана'),
    (r'\bВіддані\b', 'Віддана'),
    (r'\bпишаємося\b', 'пишаюся'),
    (r'\bПишаємося\b', 'Пишаюся'),
    (r'\bпоєднуємо\b', 'поєдную'),
    (r'\bПоєднуємо\b', 'Поєдную'),
    (r'\bмаємо\b', 'маю'),
    (r'\bМаємо\b', 'Маю'),
    (r'\bзабезпечуємо\b', 'забезпечую'),
    (r'\bЗабезпечуємо\b', 'Забезпечую'),
    (r'\bпрацюємо\b', 'працюю'),
    (r'\bПрацюємо\b', 'Працюю'),
    (r'\bдопомагаємо\b', 'допомагаю'),
    (r'\bДопомагаємо\b', 'Допомагаю'),
    (r'\bстворюємо\b', 'створюю'),
    (r'\bСтворюємо\b', 'Створюю'),
    (r'\bпрагнемо\b', 'прагну'),
    (r'\bПрагнемо\b', 'Прагну'),
    (r'\bдбаємо\b', 'дбаю'),
    (r'\bДбаємо\b', 'Дбаю'),
    (r'\bвірімо\b', 'вірю'),
    (r'\bВірімо\b', 'Вірю'),
    (r'\bпропонуєм\b', 'пропоную'),
    (r'\bзнаємо\b', 'знаю'),
    (r'\bЗнаємо\b', 'Знаю'),
    (r'\bрозуміємо\b', 'розумію'),
    (r'\bРозуміємо\b', 'Розумію'),

    # Клініка → Кабінет (только в контексте "наш/моя")
    (r'\bклініка\b', 'кабінет'),
    (r'\bКлініка\b', 'Кабінет'),
    (r'\bклініці\b', 'кабінеті'),
    (r'\bКлініці\b', 'Кабінеті'),
    (r'\bклінікою\b', 'кабінетом'),
    (r'\bКлінікою\b', 'Кабінетом'),
    (r'\bклініку\b', 'кабінет'),
    (r'\bКлініку\b', 'Кабінет'),
]


def process_file(file_path):
    """Обрабатывает один HTML файл"""
    try:
        # Читаем файл
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        replacements_made = 0

        # Применяем все замены
        for pattern, replacement in REPLACEMENTS:
            new_content = re.sub(pattern, replacement, content)
            if new_content != content:
                # Подсчитываем количество замен
                replacements_made += len(re.findall(pattern, content))
                content = new_content

        # Сохраняем только если были изменения
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, replacements_made
        else:
            return False, 0

    except Exception as e:
        print(f"Ошибка при обработке {file_path}: {e}")
        return False, 0


def main():
    """Основная функция"""
    import sys
    import io

    # Устанавливаем UTF-8 для вывода в консоль
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    print("=" * 80)
    print("СКРИПТ ЗАМЕНЫ ТЕКСТОВ: ГРУППА -> ОДНО ЛИЦО")
    print("Косметолог: Юлія Антіпова")
    print("=" * 80)
    print()

    # Получаем текущую директорию
    base_dir = Path(__file__).parent

    total_files = 0
    processed_files = 0
    total_replacements = 0
    missing_files = []

    # Обрабатываем каждый файл
    for filename in HTML_FILES:
        file_path = base_dir / filename

        if not file_path.exists():
            print(f"[!] ОТСУТСТВУЕТ: {filename}")
            missing_files.append(filename)
            continue

        total_files += 1
        modified, replacements = process_file(file_path)

        if modified:
            processed_files += 1
            total_replacements += replacements
            print(f"[+] ОБРАБОТАН: {filename} ({replacements} замен)")
        else:
            print(f"[-] БЕЗ ИЗМЕНЕНИЙ: {filename}")

    # Итоговый отчет
    print()
    print("=" * 80)
    print("ОТЧЕТ О ВЫПОЛНЕНИИ")
    print("=" * 80)
    print(f"Всего файлов найдено: {total_files}")
    print(f"Файлов изменено: {processed_files}")
    print(f"Всего замен выполнено: {total_replacements}")

    if missing_files:
        print(f"\nОтсутствующие файлы ({len(missing_files)}):")
        for filename in missing_files:
            print(f"  - {filename}")

    print()
    print("Все тексты успешно переделаны с обращения от группы на обращение")
    print("от одного косметолога - Юлії Антіпової!")
    print("=" * 80)


if __name__ == "__main__":
    main()
