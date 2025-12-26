#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
تحويل chapter5.html من التصميم القديم إلى التصميم الجديد
مع إضافة المستطيلات الملونة وقسم التعليقات
"""

# قراءة الملف الأصلي
with open('/home/user/uploaded_files/CHAPTER5.HTML.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Header الجديد
new_header = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>الفصل الخامس: مشاعر الكون وانفعالاته | ترانيم الكون</title>
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700;900&family=Amiri:wght@400;700&display=swap" rel="stylesheet">
    
    <!-- تحسينات التصميم المخصصة -->
    <style>
        /* تحسين العناوين الرئيسية */
        .chapter-content h2 {
            font-size: 2.2em !important;
            font-weight: bold !important;
            margin-top: 4rem !important;
            margin-bottom: 2rem !important;
            padding-bottom: 15px !important;
            border-bottom: 4px solid currentColor !important;
            color: #E74C3C;
        }
        
        /* تحسين العناوين الفرعية */
        .chapter-content h3 {
            font-size: 1.7em !important;
            font-weight: bold !important;
            margin-top: 2.5rem !important;
            margin-bottom: 1.5rem !important;
            border-right: 5px solid currentColor !important;
            padding-right: 15px !important;
            color: #2980B9 !important;
        }
        
        .chapter-content h4 {
            font-size: 1.4em !important;
            font-weight: bold !important;
            margin-top: 2rem !important;
            margin-bottom: 1rem !important;
            color: #34495E !important;
        }
        
        /* صناديق النصوص العامة */
        .text-box {
            background: linear-gradient(135deg, #EBF5FB 0%, #D6EAF8 100%);
            border: 2px solid #3498DB;
            border-radius: 12px;
            padding: 2rem;
            margin: 2.5rem 0;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            font-size: 1.15em;
            line-height: 2;
        }
        
        /* صناديق الآيات القرآنية */
        .quran-box {
            background: linear-gradient(135deg, #FFF9C4 0%, #FFF3B0 100%);
            border-right: 6px solid #F39C12;
            border-radius: 12px;
            padding: 2rem;
            margin: 2.5rem 0;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            font-family: 'Amiri', serif;
            font-size: 1.3em;
            line-height: 2.2;
        }
        
        /* صناديق الاقتباسات */
        .quote-box {
            background: #F8F9FA;
            border-left: 5px solid #9B59B6;
            border-radius: 10px;
            padding: 1.8rem;
            margin: 2.5rem 0;
            box-shadow: 0 3px 12px rgba(0,0,0,0.08);
            font-style: italic;
            font-size: 1.1em;
            line-height: 1.9;
        }
        
        /* صناديق الملاحظات والتنبيهات */
        .note-box {
            background: linear-gradient(135deg, #FEF9E7 0%, #FCF3CF 100%);
            border-right: 5px solid #F39C12;
            border-radius: 10px;
            padding: 1.8rem;
            margin: 2rem 0;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            font-size: 1.15em;
            line-height: 2;
        }
        
        /* صناديق الخلاصة */
        .summary-box {
            background: linear-gradient(135deg, #E8F8F5 0%, #D5F4E6 100%);
            border: 2px solid #2ECC71;
            border-radius: 12px;
            padding: 1.8rem;
            margin: 2rem 0;
            box-shadow: 0 4px 15px rgba(0,0,0,0.08);
            font-size: 1.15em;
            line-height: 2;
        }
        
        /* تحسين الفقرات */
        .chapter-content p {
            font-size: 1.1em;
            line-height: 2;
            margin-bottom: 1.5rem;
            color: #2C3E50;
        }
        
        /* تحسين القوائم */
        .chapter-content ul, .chapter-content ol {
            font-size: 1.1em;
            line-height: 2;
            margin: 1.5rem 0;
        }
        
        .chapter-content blockquote {
            background: #F8F9FA;
            border-left: 5px solid #9B59B6;
            border-radius: 10px;
            padding: 1.8rem;
            margin: 2.5rem 0;
            box-shadow: 0 3px 12px rgba(0,0,0,0.08);
            font-style: italic;
            font-size: 1.1em;
            line-height: 1.9;
        }
        
        /* تحسين الروابط */
        .chapter-content a {
            color: #3498DB;
            text-decoration: none;
            border-bottom: 2px solid transparent;
            transition: all 0.3s ease;
        }
        
        .chapter-content a:hover {
            color: #2C3E50;
            border-bottom-color: #3498DB;
        }
        
        /* استجابة للأجهزة المحمولة */
        @media (max-width: 768px) {
            .chapter-content h2 {
                font-size: 1.8em !important;
            }
            
            .chapter-content h3 {
                font-size: 1.4em !important;
            }
            
            .text-box, .quran-box, .quote-box, .note-box, .summary-box {
                padding: 1.5rem;
                margin: 1.5rem 0;
            }
        }
        
        /* قسم التعليقات */
        .comments-section {
            margin-top: 4rem;
            padding-top: 3rem;
            border-top: 3px solid #E74C3C;
        }
        
        .comments-section h3 {
            color: #E74C3C;
            font-size: 2em;
            margin-bottom: 2rem;
        }
        
        .comment-form {
            background: #F8F9FA;
            padding: 2rem;
            border-radius: 10px;
            margin-bottom: 2rem;
        }
        
        .comment-form input, .comment-form textarea {
            width: 100%;
            padding: 1rem;
            margin-bottom: 1rem;
            border: 1px solid #DDD;
            border-radius: 5px;
            font-family: 'Tajawal', sans-serif;
            font-size: 1em;
        }
        
        .comment-form textarea {
            min-height: 120px;
            resize: vertical;
        }
        
        .comment-form button {
            background: linear-gradient(135deg, #3498DB 0%, #2980B9 100%);
            color: white;
            padding: 1rem 2rem;
            border: none;
            border-radius: 5px;
            font-size: 1.1em;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .comment-form button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(52, 152, 219, 0.4);
        }
    </style>
</head>
<body>
    <!-- Website URL Banner -->
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; text-align: center; padding: 0.8rem; font-weight: bold; font-size: 1.1rem; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
        🌐 <a href="http://www.universe-melodies.com" style="color: white; text-decoration: none;">www.universe-melodies.com</a>
    </div>

    <nav class="navbar">
        <div class="container">
            <div class="nav-brand"><h2>🌌 ترانيم الكون</h2></div>
            <ul class="nav-menu">
                <li><a href="index.html">الرئيسية</a></li>
                <li><a href="introduction.html">المقدمة</a></li>
                <li><a href="about.html">عن المؤلف</a></li>
                <li><a href="contents.html">فهرس الكتاب</a></li>
            </ul>
            <div class="mobile-menu-toggle">☰</div>
        </div>
    </nav>

    <section class="chapter-header">
        <div class="container">
            <p class="chapter-number">الفصل الخامس</p>
            <h1 class="chapter-title">مشاعر الكون وانفعالاته</h1>
            <p class="chapter-subtitle">رحلة في عالم المشاعر الكونية الخفية</p>
        </div>
    </section>

    <section class="chapter-content">
        <div class="container">
'''

# Footer الجديد مع قسم التعليقات
comments_section = '''

            <!-- قسم التعليقات -->
            <div class="comments-section">
                <h3>
                    <i class="fas fa-comments"></i> شاركنا تأملاتك
                </h3>
                
                <!-- نموذج إضافة تعليق -->
                <form class="comment-form" onsubmit="event.preventDefault(); addComment();">
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
                        <input type="text" id="nameInput" placeholder="الاسم" required>
                        <input type="email" placeholder="البريد الإلكتروني (اختياري)">
                    </div>
                    <textarea id="commentInput" rows="4" placeholder="اكتب تعليقك أو تأملك حول مشاعر الكون..." required></textarea>
                    <button type="submit">
                        <i class="fas fa-paper-plane"></i> إرسال التعليق
                    </button>
                </form>

                <!-- قائمة التعليقات -->
                <div id="commentsList">
                    <!-- تعليق تجريبي -->
                    <div style="background: white; padding: 1.5rem; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); margin-bottom: 1.5rem;">
                        <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                            <div style="width: 50px; height: 50px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 1.5em; margin-left: 1rem;">ع</div>
                            <div>
                                <h4 style="margin: 0; color: #2C3E50;">عبد الله</h4>
                                <span style="color: #95A5A6; font-size: 0.9em;">منذ ساعة</span>
                            </div>
                        </div>
                        <p style="color: #34495E; line-height: 1.8; margin: 0;">فصل رائع جداً، الربط بين المفاهيم القرآنية والعلم الحديث يفتح آفاقاً جديدة للتفكير. شكراً لكم.</p>
                    </div>
                </div>
            </div>

            <footer style="margin-top: 4rem; padding-top: 2rem; border-top: 2px solid #E74C3C; text-align: center;">
                <p>&copy; 2024 ترانيم الكون - د. جميل السقيا | جميع الحقوق محفوظة</p>
                <p style="margin-top: 0.5rem; font-size: 0.9em; opacity: 0.8;">🌐 <a href="http://www.universe-melodies.com" style="color: var(--accent-color); text-decoration: none;">www.universe-melodies.com</a></p>
            </footer>

        </div>
    </section>

    <footer class="footer">
        <div class="container">
            <p>&copy; 2024 ترانيم الكون - جميع الحقوق محفوظة</p>
            <p style="margin-top: 0.5rem; font-size: 0.9em; opacity: 0.8;">🌐 <a href="http://www.universe-melodies.com" style="color: var(--accent-color); text-decoration: none;">www.universe-melodies.com</a></p>
        </div>
    </footer>

    <script src="script.js"></script>
    <script>
        function addComment() {
            const name = document.getElementById('nameInput').value;
            const comment = document.getElementById('commentInput').value;
            
            if (name && comment) {
                alert('شكراً لك! تم إرسال تعليقك بنجاح.');
                // يمكن إضافة كود لحفظ التعليق في قاعدة بيانات
                document.getElementById('nameInput').value = '';
                document.getElementById('commentInput').value = '';
            }
        }
    </script>
</body>
</html>'''

# استخراج المحتوى الرئيسي من الملف الأصلي (بين <body> و </body>)
import re
body_match = re.search(r'<body>(.*?)</body>', content, re.DOTALL)
if body_match:
    body_content = body_match.group(1)
    
    # إزالة <div class="container"> الأول و </div> الأخير
    body_content = re.sub(r'^\s*<div class="container">', '', body_content)
    body_content = re.sub(r'</div>\s*$', '', body_content[::-1], count=1)[::-1]
    
    # تطبيق التعديلات على الصناديق
    # تحويل .box.box-desc إلى .text-box
    body_content = re.sub(r'<div class="box box-desc">', '<div class="text-box">', body_content)
    body_content = re.sub(r'<span class="box-title">(.*?)</span>', r'<h4 style="color: #2980B9; margin-bottom: 1rem;">\1</h4>', body_content)
    
    # تحويل .box.box-scene إلى .note-box
    body_content = re.sub(r'<div class="box box-scene">', '<div class="note-box">', body_content)
    
    # تحويل .box.box-science إلى .note-box
    body_content = re.sub(r'<div class="box box-science">', '<div class="note-box">', body_content)
    
    # تحويل .verse-container إلى .quran-box
    body_content = re.sub(r'<div class="verse-container"(.*?)>', r'<div class="quran-box"\1>', body_content)
    body_content = re.sub(r'<div class="verse-text">(.*?)</div>', r'<p style="text-align: center; font-size: 1.5em; font-weight: bold; color: #148f77; margin: 0;">\1</p>', body_content)
    body_content = re.sub(r'<span class="verse-ref">(.*?)</span>', r'<p style="text-align: center; margin-top: 1rem; font-weight: bold; font-size: 1.1em; color: #E67E22;">\1</p>', body_content)
    
    # تحويل .hadith إلى .quote-box
    body_content = re.sub(r'<div class="hadith">', '<div class="quote-box">', body_content)
    body_content = re.sub(r'<span class="source">(.*?)</span>', r'<p style="text-align: left; margin-top: 1rem; font-size: 0.95em; color: #7F8C8D;">\1</p>', body_content)
    
    # تحويل .poetry إلى .quote-box
    body_content = re.sub(r'<div class="poetry">', '<div class="quote-box" style="text-align: center; font-style: normal;">', body_content)
    
    # دمج الملف النهائي
    final_content = new_header + body_content + comments_section
    
    # حفظ الملف النهائي
    with open('/home/user/webapp/chapter5.html', 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    print("✅ تم تحويل الملف بنجاح!")
    print(f"📝 حجم الملف الجديد: {len(final_content)} حرف")
else:
    print("❌ خطأ: لم يتم العثور على محتوى body")
