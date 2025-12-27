# دليل حذف المشروع الخاطئ من Cloudflare

## الطريقة الصحيحة للحذف:

### الخطوة 1: اذهب إلى قائمة المشاريع
رابط مباشر: https://dash.cloudflare.com/ef5878d0bd45841f9bc4277a9f47e409/workers-and-pages

### الخطوة 2: ابحث عن المشروع
- ستجد قائمة بالمشاريع
- ابحث عن: **universe-melodies**

### الخطوة 3: احذف المشروع
**طريقة 1:** من القائمة مباشرة
- بجانب اسم المشروع، ابحث عن أيقونة (⋮) أو (•••) أو "Actions"
- اضغط عليها
- اختر **"Delete"** أو **"Remove"**

**طريقة 2:** من داخل المشروع
- اضغط على اسم المشروع **universe-melodies**
- ابحث عن تبويب اسمه أحد هذه:
  - **Settings**
  - **Manage**
  - **⚙️** (أيقونة الترس)
- انزل للأسفل
- اضغط **"Delete Project"** أو **"Delete Deployment"**

### إذا لم تجد زر الحذف:
جرّب هذه الروابط المباشرة:

**للـ Worker:**
https://dash.cloudflare.com/ef5878d0bd45841f9bc4277a9f47e409/workers/services/view/universe-melodies/production/settings

**أو جرّب:**
https://dash.cloudflare.com/ef5878d0bd45841f9bc4277a9f47e409/workers/services

---

## بديل: لا تحذف - أنشئ مشروع جديد!

إذا لم تستطع الحذف، لا مشكلة:

### أنشئ مشروع Pages جديد باسم مختلف:
```
Project name: universe-melodies-site
```

أو:
```
Project name: universe-melodies-book
```

ثم أكمل باقي الإعدادات كالمعتاد!

---

## الإعدادات الصحيحة للمشروع الجديد:
```
Project name: universe-melodies-site
Production branch: main
Framework preset: None
Build command: (فارغ)
Build output directory: /
```

الرابط سيصبح:
```
https://universe-melodies-site.pages.dev
```

**ونفس النطاق www.universe-melodies.com سنربطه لاحقاً بغض النظر عن اسم المشروع!**
