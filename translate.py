# -*- coding: utf-8 -*-
import re
import sys

# Словник перекладів (загальні елементи для всіх сторінок)
translations = {
    # Navigation
    r'<li class="nav-item submenu"><a class="nav-link" href="./">Home</a>': '<li class="nav-item submenu"><a class="nav-link" href="./">Головна</a>',
    r'<li class="nav-item"><a class="nav-link" href="index.html">Home - Version 1</a></li>': '<li class="nav-item"><a class="nav-link" href="index.html">Головна - Версія 1</a></li>',
    r'<li class="nav-item"><a class="nav-link" href="index-2.html">Home - Version 2</a></li>': '<li class="nav-item"><a class="nav-link" href="index-2.html">Головна - Версія 2</a></li>',
    r'<li class="nav-item"><a class="nav-link" href="index-3.html">Home - Version 3</a></li>': '<li class="nav-item"><a class="nav-link" href="index-3.html">Головна - Версія 3</a></li>',
    r'<li class="nav-item"><a class="nav-link" href="about.html">About Us</a>': '<li class="nav-item"><a class="nav-link" href="about.html">Про нас</a>',
    r'<li class="nav-item"><a class="nav-link" href="services.html">Services</a></li>': '<li class="nav-item"><a class="nav-link" href="services.html">Послуги</a></li>',
    r'<li class="nav-item"><a class="nav-link" href="blog.html">Blog</a></li>': '<li class="nav-item"><a class="nav-link" href="blog.html">Блог</a></li>',
    r'<li class="nav-item submenu"><a class="nav-link" href="#">Pages</a>': '<li class="nav-item submenu"><a class="nav-link" href="#">Сторінки</a>',
    r'<li class="nav-item"><a class="nav-link" href="service-single.html">Service Details</a></li>': '<li class="nav-item"><a class="nav-link" href="service-single.html">Деталі послуги</a></li>',
    r'<li class="nav-item"><a class="nav-link" href="blog-single.html">Blog Details</a></li>': '<li class="nav-item"><a class="nav-link" href="blog-single.html">Деталі блогу</a></li>',
    r'<li class="nav-item"><a class="nav-link" href="case-study.html">Case Study</a></li>': '<li class="nav-item"><a class="nav-link" href="case-study.html">Кейси</a></li>',
    r'<li class="nav-item"><a class="nav-link" href="case-study-single.html">Case Study Details</a></li>': '<li class="nav-item"><a class="nav-link" href="case-study-single.html">Деталі кейсу</a></li>',
    r'<li class="nav-item"><a class="nav-link" href="team.html">Our Team</a></li>': '<li class="nav-item"><a class="nav-link" href="team.html">Наша команда</a></li>',
    r'<li class="nav-item"><a class="nav-link" href="team-single.html">Team Details</a></li>': '<li class="nav-item"><a class="nav-link" href="team-single.html">Деталі команди</a></li>',
    r'<li class="nav-item"><a class="nav-link" href="pricing.html">Pricing Plan</a></li>': '<li class="nav-item"><a class="nav-link" href="pricing.html">Ціни</a></li>',
    r'<li class="nav-item"><a class="nav-link" href="testimonials.html">Testimonials</a></li>': '<li class="nav-item"><a class="nav-link" href="testimonials.html">Відгуки</a></li>',
    r'<li class="nav-item"><a class="nav-link" href="image-gallery.html">Image Gallery</a></li>': '<li class="nav-item"><a class="nav-link" href="image-gallery.html">Галерея фото</a></li>',
    r'<li class="nav-item"><a class="nav-link" href="video-gallery.html">Video Gallery</a></li>': '<li class="nav-item"><a class="nav-link" href="video-gallery.html">Галерея відео</a></li>',
    r'<li class="nav-item"><a class="nav-link" href="faqs.html">FAQs</a></li>': '<li class="nav-item"><a class="nav-link" href="faqs.html">Питання</a></li>',
    r'<li class="nav-item"><a class="nav-link" href="contact.html">Contact Us</a></li>': '<li class="nav-item"><a class="nav-link" href="contact.html">Контакти</a></li>',
    r'<li class="nav-item highlighted-menu"><a href="book-appointment.html">Book An Appointment</a></li>': '<li class="nav-item highlighted-menu"><a href="book-appointment.html">Записатися на прийом</a></li>',

    # Common buttons and links
    r'Book An Appointment': 'Записатися на прийом',
    r'Read More': 'Читати далі',
    r'View All': 'Дивитися всі',
    r'Get Started': 'Почати',
    r'Contact Us': 'Зв\'яжіться з нами',
    r'Get Consultation': 'Отримати консультацію',

    # Footer
    r'Copyright © 2026 All Rights Reserved.': '© 2026 Всі права захищені.',
    r'Quick Links': 'Швидкі посилання',
    r'Our Services': 'Наші послуги',
    r'Subscribe Newsletters': 'Підписатися на розсилку',

    # Lang
    r'<html lang="zxx">': '<html lang="uk">',
}

def translate_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        for eng, ukr in translations.items():
            content = content.replace(eng, ukr)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✅ {filepath}")
        return True
    except Exception as e:
        print(f"❌ Error in {filepath}: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1:
        translate_file(sys.argv[1])
    else:
        print("Usage: python translate.py <filepath>")
