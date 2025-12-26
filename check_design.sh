#!/bin/bash
echo "=== فحص التصميم النهائي للفصل السادس ==="
echo ""
echo "1. حجم الملفات:"
ls -lh chapter6.html chapter6_final_enhanced.css | awk '{print "   ", $5, $9}'
echo ""
echo "2. التحقق من استخدام CSS الجديد:"
grep -q "chapter6_final_enhanced.css" chapter6.html && echo "   ✅ يستخدم CSS المحسّن" || echo "   ❌ لا يستخدم CSS المحسّن"
echo ""
echo "3. التحقق من زر العودة للأعلى:"
grep -q "backToTop" chapter6.html && echo "   ✅ زر العودة للأعلى موجود" || echo "   ❌ زر العودة للأعلى غير موجود"
echo ""
echo "4. عدد الألوان الحيوية الجديدة في CSS:"
grep -c "#FF6B95\|#FFA07A\|#4CAF50\|#FF9800\|#2196F3\|#9C27B0" chapter6_final_enhanced.css | awk '{print "   ", $0, "لون حيوي"}'
echo ""
echo "5. عدد التأثيرات التفاعلية (hover):"
grep -c ":hover" chapter6_final_enhanced.css | awk '{print "   ", $0, "تأثير hover"}'
echo ""
echo "6. حالة الخادم:"
curl -s -I http://localhost:8080/chapter6.html 2>&1 | grep "HTTP" | awk '{print "   ", $0}'
echo ""
echo "=== انتهى الفحص ==="
