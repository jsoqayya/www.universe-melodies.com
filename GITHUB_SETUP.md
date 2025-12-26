# 🔗 دليل الرفع على GitHub Repository موجود

## 📋 المتطلبات الأساسية

- حساب GitHub نشط
- Git مثبت على جهازك
- Repository موجود على GitHub (فارغ أو يحتوي على ملفات)

---

## 🚀 السيناريو الأول: Repository فارغ جديد

### الخطوة 1: فك ضغط الملفات

```bash
# فك ضغط الأرشيف
tar -xzf taranim-book-website.tar.gz

# الدخول إلى المجلد
cd taranim-book-website
```

### الخطوة 2: تهيئة Git

```bash
# تهيئة مستودع Git محلي
git init

# إضافة جميع الملفات
git add .

# أول commit
git commit -m "Initial commit: ترانيم الكون - موقع الكتاب الإلكتروني"
```

### الخطوة 3: الربط بـ GitHub

```bash
# استبدل YOUR_USERNAME باسم المستخدم الخاص بك
# استبدل REPO_NAME باسم الـ Repository
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git

# تحقق من الربط
git remote -v
```

### الخطوة 4: رفع الملفات

```bash
# رفع الملفات (Branch: main)
git push -u origin main

# أو إذا كان الـ branch اسمه master:
git push -u origin master
```

---

## 🔄 السيناريو الثاني: Repository موجود بالفعل (Existing Project)

### الخطوة 1: استنساخ Repository الموجود

```bash
# استنساخ الـ Repository الموجود
git clone https://github.com/YOUR_USERNAME/REPO_NAME.git

# الدخول إلى المجلد المستنسخ
cd REPO_NAME
```

### الخطوة 2: نسخ ملفات المشروع

```bash
# فك ضغط الأرشيف في مكان آخر
cd ..
tar -xzf taranim-book-website.tar.gz

# نسخ جميع الملفات إلى Repository
cp -r taranim-book-website/* REPO_NAME/

# العودة إلى مجلد Repository
cd REPO_NAME
```

### الخطوة 3: التحقق من التغييرات

```bash
# عرض الملفات المضافة/المعدلة
git status

# معاينة التغييرات
git diff
```

### الخطوة 4: رفع التغييرات

```bash
# إضافة جميع التغييرات
git add .

# عمل Commit
git commit -m "إضافة موقع ترانيم الكون الإلكتروني"

# رفع التغييرات
git push origin main
```

---

## 🔐 السيناريو الثالث: استخدام Personal Access Token

إذا كان GitHub يطلب منك Token بدلاً من كلمة المرور:

### الخطوة 1: إنشاء Personal Access Token

1. اذهب إلى: https://github.com/settings/tokens
2. انقر "Generate new token" → "Generate new token (classic)"
3. أعطِ Token اسماً: مثل "Taranim Website"
4. اختر Scopes: `repo` (كامل)
5. انقر "Generate token"
6. **احفظ Token في مكان آمن** (لن تستطيع رؤيته مرة أخرى!)

### الخطوة 2: استخدام Token

```bash
# طريقة 1: استخدام Token في URL
git remote set-url origin https://YOUR_TOKEN@github.com/YOUR_USERNAME/REPO_NAME.git

# طريقة 2: استخدام Git Credential Manager
git config --global credential.helper store
git push origin main
# سيطلب منك username و password (استخدم Token كـ password)
```

---

## 🌍 تفعيل GitHub Pages

### الخطوة 1: الذهاب إلى Settings

1. افتح Repository على GitHub
2. انقر على "Settings" (الإعدادات)

### الخطوة 2: تفعيل Pages

1. في القائمة الجانبية، انقر "Pages"
2. في "Source": اختر "Deploy from a branch"
3. في "Branch": اختر `main` (أو `master`)
4. في "Folder": اختر `/ (root)`
5. انقر "Save"

### الخطوة 3: الانتظار

- GitHub Pages يستغرق **2-5 دقائق** لنشر الموقع
- بعدها سيكون الموقع متاحاً على:
  ```
  https://YOUR_USERNAME.github.io/REPO_NAME/
  ```

### الخطوة 4: التحقق

```bash
# الموقع سيكون متاحاً على هذا الرابط:
https://YOUR_USERNAME.github.io/REPO_NAME/
```

---

## 🎨 Domain مخصص (اختياري)

إذا كنت تريد استخدام نطاق خاص بك (مثل www.taranim-book.com):

### الخطوة 1: شراء Domain

اشترِ نطاقاً من أي مزود (GoDaddy, Namecheap, Google Domains, إلخ)

### الخطوة 2: إضافة CNAME في GitHub

1. في مجلد المشروع، أنشئ ملف `CNAME` (بدون امتداد):
   ```bash
   echo "www.your-domain.com" > CNAME
   git add CNAME
   git commit -m "Add custom domain"
   git push origin main
   ```

### الخطوة 3: إعداد DNS Records

في لوحة تحكم مزود النطاق، أضف:

```
Type: CNAME
Name: www
Value: YOUR_USERNAME.github.io
```

انتظر **24-48 ساعة** حتى ينتشر DNS

---

## ⚠️ حل المشاكل الشائعة

### مشكلة: `fatal: remote origin already exists`

```bash
# حذف remote القديم
git remote remove origin

# إضافة remote جديد
git remote add origin https://github.com/YOUR_USERNAME/REPO_NAME.git
```

### مشكلة: `! [rejected] main -> main (non-fast-forward)`

```bash
# خيار 1: Pull ثم Push
git pull origin main --allow-unrelated-histories
git push origin main

# خيار 2: Force Push (احذر: سيحذف التاريخ القديم)
git push -f origin main
```

### مشكلة: صفحة 404 على GitHub Pages

- تأكد من أن ملف `index.html` موجود في المجلد الرئيسي
- انتظر 5 دقائق بعد Push
- تحقق من إعدادات Pages في Settings

### مشكلة: CSS/JS لا تعمل على GitHub Pages

تأكد من أن الروابط نسبية وليست مطلقة:

```html
<!-- ✅ صحيح -->
<link rel="stylesheet" href="style.css">
<script src="script.js"></script>

<!-- ❌ خطأ -->
<link rel="stylesheet" href="/style.css">
<script src="/script.js"></script>
```

---

## 📞 الدعم

إذا واجهت أي مشكلة:

1. راجع [GitHub Documentation](https://docs.github.com/en/pages)
2. ابحث عن الخطأ في [Stack Overflow](https://stackoverflow.com/)
3. اطلب المساعدة في [GitHub Community](https://github.community/)

---

**نتمنى لك تجربة سلسة! 🚀**
