# -*- coding: utf-8 -*-
"""
Автоматичний переклад повторюваних елементів у всіх HTML файлах
"""
import os
import sys
import io

# Встановлюємо UTF-8 для консолі
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Список всіх файлів для обробки
FILES = [
    'index.html', 'index-2.html', 'index-3.html', 'about.html',
    'services.html', 'service-single.html', 'blog.html', 'blog-single.html',
    'contact.html', 'book-appointment.html', 'team.html', 'team-single.html',
    'pricing.html', 'case-study.html', 'case-study-single.html',
    'testimonials.html', 'image-gallery.html', 'video-gallery.html',
    'faqs.html', '404.html'
]

# Повний словник перекладів (точні відповідності)
TRANSLATIONS = {
    # Lang attribute
    '<html lang="zxx">': '<html lang="uk">',

    # Navigation - Main menu items
    '<li class="nav-item submenu"><a class="nav-link" href="./">Home</a>': '<li class="nav-item submenu"><a class="nav-link" href="./">Головна</a>',
    '<li class="nav-item"><a class="nav-link" href="index.html">Home - Version 1</a></li>': '<li class="nav-item"><a class="nav-link" href="index.html">Головна - Версія 1</a></li>',
    '<li class="nav-item"><a class="nav-link" href="index-2.html">Home - Version 2</a></li>': '<li class="nav-item"><a class="nav-link" href="index-2.html">Головна - Версія 2</a></li>',
    '<li class="nav-item"><a class="nav-link" href="index-3.html">Home - Version 3</a></li>': '<li class="nav-item"><a class="nav-link" href="index-3.html">Головна - Версія 3</a></li>',
    '<li class="nav-item"><a class="nav-link" href="about.html">About Us</a>': '<li class="nav-item"><a class="nav-link" href="about.html">Про нас</a>',
    '<li class="nav-item"><a class="nav-link" href="services.html">Services</a></li>': '<li class="nav-item"><a class="nav-link" href="services.html">Послуги</a></li>',
    '<li class="nav-item"><a class="nav-link" href="blog.html">Blog</a></li>': '<li class="nav-item"><a class="nav-link" href="blog.html">Блог</a></li>',
    '<li class="nav-item submenu"><a class="nav-link" href="#">Pages</a>': '<li class="nav-item submenu"><a class="nav-link" href="#">Сторінки</a>',
    '<li class="nav-item"><a class="nav-link" href="service-single.html">Service Details</a></li>': '<li class="nav-item"><a class="nav-link" href="service-single.html">Деталі послуги</a></li>',
    '<li class="nav-item"><a class="nav-link" href="blog-single.html">Blog Details</a></li>': '<li class="nav-item"><a class="nav-link" href="blog-single.html">Деталі блогу</a></li>',
    '<li class="nav-item"><a class="nav-link" href="case-study.html">Case Study</a></li>': '<li class="nav-item"><a class="nav-link" href="case-study.html">Кейси</a></li>',
    '<li class="nav-item"><a class="nav-link" href="case-study-single.html">Case Study Details</a></li>': '<li class="nav-item"><a class="nav-link" href="case-study-single.html">Деталі кейсу</a></li>',
    '<li class="nav-item"><a class="nav-link" href="team.html">Our Team</a></li>': '<li class="nav-item"><a class="nav-link" href="team.html">Наша команда</a></li>',
    '<li class="nav-item"><a class="nav-link" href="team-single.html">Team Details</a></li>': '<li class="nav-item"><a class="nav-link" href="team-single.html">Деталі команди</a></li>',
    '<li class="nav-item"><a class="nav-link" href="pricing.html">Pricing Plan</a></li>': '<li class="nav-item"><a class="nav-link" href="pricing.html">Ціни</a></li>',
    '<li class="nav-item"><a class="nav-link" href="testimonials.html">Testimonials</a></li>': '<li class="nav-item"><a class="nav-link" href="testimonials.html">Відгуки</a></li>',
    '<li class="nav-item"><a class="nav-link" href="image-gallery.html">Image Gallery</a></li>': '<li class="nav-item"><a class="nav-link" href="image-gallery.html">Галерея фото</a></li>',
    '<li class="nav-item"><a class="nav-link" href="video-gallery.html">Video Gallery</a></li>': '<li class="nav-item"><a class="nav-link" href="video-gallery.html">Галерея відео</a></li>',
    '<li class="nav-item"><a class="nav-link" href="faqs.html">FAQs</a></li>': '<li class="nav-item"><a class="nav-link" href="faqs.html">Питання</a></li>',
    '<li class="nav-item"><a class="nav-link" href="contact.html">Contact Us</a></li>': '<li class="nav-item"><a class="nav-link" href="contact.html">Контакти</a></li>',
    '<li class="nav-item highlighted-menu"><a href="book-appointment.html">Book An Appointment</a></li>': '<li class="nav-item highlighted-menu"><a href="book-appointment.html">Записатися на прийом</a></li>',

    # Header top bar
    '<li><a href="#">Help</a></li>': '<li><a href="#">Допомога</a></li>',
    '<li><a href="#">support</a></li>': '<li><a href="#">Підтримка</a></li>',
    '<li><a href="contact.html">contact</a></li>': '<li><a href="contact.html">Контакти</a></li>',

    # Buttons - Common variations
    'Book An Appointment': 'Записатися на прийом',
    'Book an appointment': 'Записатися на прийом',
    'Book Appointment': 'Записатися на прийом',
    '>Read More<': '>Читати далі<',
    'class="readmore-btn">Read More</a>': 'class="readmore-btn">Читати далі</a>',
    'View All Services': 'Дивитися всі послуги',
    'View All Blogs': 'Дивитися всі публікації',
    'Get Started': 'Почати',
    'Get Consultation': 'Отримати консультацію',
    'Get in Touch': "Зв'яжіться з нами",
    'Learn More': 'Дізнатися більше',
    'Learn More About': 'Дізнатися більше',

    # Contact phrases
    'Contact Us!': "Зв'яжіться з нами!",

    # Form labels
    '<label>Full Name': '<label>Повне ім\'я',
    '<label>Email Address': '<label>Email адреса',
    '<label>Phone Number': '<label>Номер телефону',
    '<label>Appointment Date:': '<label>Дата прийому:',
    '<label>Message': '<label>Повідомлення',
    '<label>Your Name': '<label>Ваше ім\'я',
    '<label>Your Email': '<label>Ваш Email',

    # Form placeholders
    'placeholder="Enter Full Name': 'placeholder="Введіть повне ім\'я',
    'placeholder="Enter Email Address': 'placeholder="Введіть email адресу',
    'placeholder="Enter Phone Number': 'placeholder="Введіть номер телефону',
    'placeholder="Write Message Here': 'placeholder="Напишіть повідомлення тут',
    'placeholder="Enter Your Name': 'placeholder="Введіть ваше ім\'я',
    'placeholder="Enter Your Email': 'placeholder="Введіть ваш email',

    # Footer - Quick Links
    '<h2>Quick Links</h2>': '<h2>Швидкі посилання</h2>',
    '<li><a href="index.html">Home</a></li>': '<li><a href="index.html">Головна</a></li>',
    '<li><a href="index-2.html">Home</a></li>': '<li><a href="index-2.html">Головна</a></li>',
    '<li><a href="index-3.html">Home</a></li>': '<li><a href="index-3.html">Головна</a></li>',
    '<li><a href="about.html">About Us</a></li>': '<li><a href="about.html">Про нас</a></li>',
    '<li><a href="services.html">Our Services</a></li>': '<li><a href="services.html">Наші послуги</a></li>',
    '<li><a href="services.html">Services</a></li>': '<li><a href="services.html">Послуги</a></li>',
    '<li><a href="blog.html">Blogs</a></li>': '<li><a href="blog.html">Блог</a></li>',
    '<li><a href="testimonials.html">Testimonials</a></li>': '<li><a href="testimonials.html">Відгуки</a></li>',

    # Footer - Our Services section
    '<h2>Our Services</h2>': '<h2>Наші послуги</h2>',
    '<li><a href="service-single.html">Acne Scar Treatment</a></li>': '<li><a href="service-single.html">Лікування шрамів від акне</a></li>',
    '<li><a href="service-single.html">Dark Spot Removal</a></li>': '<li><a href="service-single.html">Видалення темних плям</a></li>',
    '<li><a href="service-single.html">Scalp Therapy</a></li>': '<li><a href="service-single.html">Терапія шкіри голови</a></li>',
    '<li><a href="service-single.html">Laser Hair Removal</a></li>': '<li><a href="service-single.html">Лазерна епіляція</a></li>',
    '<li><a href="service-single.html">Skin Rejuvenation</a></li>': '<li><a href="service-single.html">Омолодження шкіри</a></li>',
    '<li><a href="service-single.html">Pigmentation Treatment</a></li>': '<li><a href="service-single.html">Лікування пігментації</a></li>',
    '<li><a href="service-single.html">Chemical Peels</a></li>': '<li><a href="service-single.html">Хімічні пілінги</a></li>',

    # Footer - Working Hours
    '<h2>Working Hours</h2>': '<h2>Години роботи</h2>',
    '<span>Mon - Friday:-</span>': '<span>Пон - П\'ятниця:-</span>',
    '<span>Monday - Friday: </span>': '<span>Понеділок - П\'ятниця: </span>',
    '<span>Saturday:-</span>': '<span>Субота:-</span>',
    '<span>Saturday: </span>': '<span>Субота: </span>',
    '<span>Sunday:-</span>Closed': '<span>Неділя:-</span>Вихідний',
    '<span>Sunday: </span> Closed': '<span>Неділя: </span> Вихідний',

    # Footer - Follow Us / Social
    '<h2>Follow Us</h2>': '<h2>Слідкуйте за нами</h2>',
    '<h2>Subscribe Newsletters</h2>': '<h2>Підписатися на розсилку</h2>',

    # Footer - Copyright
    '<p>Copyright © 2026 All Rights Reserved.</p>': '<p>© 2026 Всі права захищені.</p>',
    'Copyright © 2026 All Rights Reserved.': '© 2026 Всі права захищені.',

    # Footer - Privacy links
    '<li><a href="#">Privacy  Policy</a></li>': '<li><a href="#">Політика конфіденційності</a></li>',
    '<li><a href="#">Privacy Policy</a></li>': '<li><a href="#">Політика конфіденційності</a></li>',
    "<li><a href=\"#\">Term's & Condition</a></li>": '<li><a href="#">Умови та положення</a></li>',
    '<li><a href="#">Terms & Conditions</a></li>': '<li><a href="#">Умови та положення</a></li>',
}

def translate_file(filepath):
    """Перекладає один файл"""
    try:
        # Читаємо файл
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        replacements_made = 0

        # Застосовуємо всі переклади
        for eng, ukr in TRANSLATIONS.items():
            count = content.count(eng)
            if count > 0:
                content = content.replace(eng, ukr)
                replacements_made += count

        # Зберігаємо тільки якщо були зміни
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True, replacements_made
        else:
            return False, 0

    except Exception as e:
        print(f"ERROR {filepath}: {e}")
        return False, 0

def main():
    """Головна функція - обробляє всі файли"""
    print("=" * 70)
    print("AVTOMATYCHNYI PEREKLAD HTML FAILIV")
    print("=" * 70)
    print()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    total_files = 0
    total_replacements = 0
    processed_files = []
    skipped_files = []

    for filename in FILES:
        filepath = os.path.join(base_dir, filename)

        if not os.path.exists(filepath):
            skipped_files.append(filename)
            print(f"[SKIP] {filename} - file not found")
            continue

        success, replacements = translate_file(filepath)

        if success:
            total_files += 1
            total_replacements += replacements
            processed_files.append(filename)
            print(f"[OK] {filename} - {replacements} replacements")
        else:
            skipped_files.append(filename)
            print(f"[SKIP] {filename} - no changes")

    # Підсумковий звіт
    print()
    print("=" * 70)
    print("PIDSUMKOVYI ZVIT")
    print("=" * 70)
    print(f"Processed files: {total_files}/{len(FILES)}")
    print(f"Total replacements: {total_replacements}")
    print()

    if processed_files:
        print("Successfully processed files:")
        for f in processed_files:
            print(f"   * {f}")
        print()

    if skipped_files:
        print("Skipped files:")
        for f in skipped_files:
            print(f"   * {f}")

    print()
    print("=" * 70)
    print("TRANSLATION COMPLETE!")
    print("=" * 70)

if __name__ == "__main__":
    main()
