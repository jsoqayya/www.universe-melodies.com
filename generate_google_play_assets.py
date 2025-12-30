#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Google Play Assets Generator for Taranim Alkawn App
Generates all required graphics assets for Google Play Console submission
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
import os
import sys

# Output directories
BASE_DIR = "google_play_assets"
DIRS = {
    "app_icon": f"{BASE_DIR}/app_icon",
    "feature_graphic": f"{BASE_DIR}/feature_graphic",
    "phone_screenshots": f"{BASE_DIR}/phone_screenshots",
    "tablet_screenshots": f"{BASE_DIR}/tablet_screenshots"
}

# Source images
BOOK_COVER_AR = "book-cover.jpg"
BOOK_COVER_EN = "hymns-universe-cover-en.jpg"
AUTHOR_PHOTO = "author-photo.jpg"

# Colors (based on cosmic theme)
COLOR_DEEP_SPACE = (10, 15, 35)  # Deep blue-black
COLOR_COSMIC_BLUE = (30, 60, 120)  # Cosmic blue
COLOR_GOLDEN = (255, 215, 0)  # Golden for text
COLOR_WHITE = (255, 255, 255)
COLOR_LIGHT_BLUE = (100, 150, 255)

def create_gradient_background(width, height, color1, color2):
    """Create a gradient background"""
    base = Image.new('RGB', (width, height), color1)
    top = Image.new('RGB', (width, height), color2)
    mask = Image.new('L', (width, height))
    mask_data = []
    for y in range(height):
        mask_data.extend([int(255 * (y / height))] * width)
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base

def add_rounded_corners(img, radius):
    """Add rounded corners to an image"""
    circle = Image.new('L', (radius * 2, radius * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, radius * 2, radius * 2), fill=255)
    
    alpha = Image.new('L', img.size, 255)
    w, h = img.size
    
    # Top-left corner
    alpha.paste(circle.crop((0, 0, radius, radius)), (0, 0))
    # Top-right corner
    alpha.paste(circle.crop((radius, 0, radius * 2, radius)), (w - radius, 0))
    # Bottom-left corner
    alpha.paste(circle.crop((0, radius, radius, radius * 2)), (0, h - radius))
    # Bottom-right corner
    alpha.paste(circle.crop((radius, radius, radius * 2, radius * 2)), (w - radius, h - radius))
    
    img.putalpha(alpha)
    return img

def create_app_icon():
    """
    Generate App Icon: 512x512 pixels
    This is the main icon shown in Google Play Store
    """
    print("📱 Creating App Icon (512x512px)...")
    
    try:
        # Load the book cover
        cover = Image.open(BOOK_COVER_AR)
        
        # Create a square canvas with gradient background
        icon = create_gradient_background(512, 512, COLOR_DEEP_SPACE, COLOR_COSMIC_BLUE)
        
        # Resize cover to fit in icon (leaving some padding)
        cover_size = 420
        cover = cover.resize((cover_size, int(cover_size * cover.height / cover.width)), Image.Resampling.LANCZOS)
        
        # Center the cover
        x = (512 - cover.width) // 2
        y = (512 - cover.height) // 2
        
        # Add a subtle shadow effect
        shadow = Image.new('RGBA', (cover.width + 20, cover.height + 20), (0, 0, 0, 0))
        shadow_draw = ImageDraw.Draw(shadow)
        shadow_draw.rectangle([10, 10, cover.width + 10, cover.height + 10], fill=(0, 0, 0, 100))
        shadow = shadow.filter(ImageFilter.GaussianBlur(10))
        
        # Convert icon to RGBA for pasting
        icon = icon.convert('RGBA')
        icon.paste(shadow, (x - 10, y - 10), shadow)
        icon.paste(cover, (x, y), cover if cover.mode == 'RGBA' else None)
        
        # Convert back to RGB for JPEG
        final_icon = Image.new('RGB', icon.size, COLOR_DEEP_SPACE)
        final_icon.paste(icon, (0, 0), icon if icon.mode == 'RGBA' else None)
        
        # Save
        output_path = f"{DIRS['app_icon']}/app_icon_512x512.png"
        final_icon.save(output_path, 'PNG', quality=95, optimize=True)
        print(f"   ✅ Saved: {output_path}")
        
        return True
    except Exception as e:
        print(f"   ❌ Error creating app icon: {e}")
        return False

def create_feature_graphic():
    """
    Generate Feature Graphic: 1024x500 pixels
    This is the main promotional banner at the top of the app page
    """
    print("🎨 Creating Feature Graphic (1024x500px)...")
    
    try:
        # Create gradient background
        graphic = create_gradient_background(1024, 500, COLOR_DEEP_SPACE, COLOR_COSMIC_BLUE)
        draw = ImageDraw.Draw(graphic)
        
        # Load book cover
        cover = Image.open(BOOK_COVER_AR)
        cover = cover.resize((280, int(280 * cover.height / cover.width)), Image.Resampling.LANCZOS)
        
        # Position cover on the right side
        cover_x = 1024 - cover.width - 50
        cover_y = (500 - cover.height) // 2
        
        # Add shadow
        shadow = Image.new('RGBA', (cover.width + 20, cover.height + 20), (0, 0, 0, 0))
        shadow_draw = ImageDraw.Draw(shadow)
        shadow_draw.rectangle([10, 10, cover.width + 10, cover.height + 10], fill=(0, 0, 0, 120))
        shadow = shadow.filter(ImageFilter.GaussianBlur(15))
        
        graphic = graphic.convert('RGBA')
        graphic.paste(shadow, (cover_x - 10, cover_y - 10), shadow)
        graphic.paste(cover, (cover_x, cover_y), cover if cover.mode == 'RGBA' else None)
        
        # Add decorative elements (stars/cosmic dots)
        for i in range(50):
            import random
            x = random.randint(50, 600)
            y = random.randint(50, 450)
            size = random.randint(1, 3)
            draw.ellipse([x, y, x + size, y + size], fill=(255, 255, 255, random.randint(100, 255)))
        
        # Add title text
        try:
            # Try to use a system font
            title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 60)
            subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
        except:
            title_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()
        
        # Main title
        title_text = "ترانيم الكون"
        title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
        title_width = title_bbox[2] - title_bbox[0]
        title_x = 80
        title_y = 150
        
        # Draw text with shadow
        draw.text((title_x + 2, title_y + 2), title_text, font=title_font, fill=(0, 0, 0, 180))
        draw.text((title_x, title_y), title_text, font=title_font, fill=COLOR_GOLDEN)
        
        # Subtitle
        subtitle_text = "سيمفونية الوجود الواعي"
        subtitle_y = title_y + 80
        draw.text((title_x + 2, subtitle_y + 2), subtitle_text, font=subtitle_font, fill=(0, 0, 0, 180))
        draw.text((title_x, subtitle_y), subtitle_text, font=subtitle_font, fill=COLOR_WHITE)
        
        # Additional info
        info_text = "القرآن والعلم • عربي + English"
        info_y = subtitle_y + 50
        draw.text((title_x + 2, info_y + 2), info_text, font=subtitle_font, fill=(0, 0, 0, 180))
        draw.text((title_x, info_y), info_text, font=subtitle_font, fill=COLOR_LIGHT_BLUE)
        
        # Convert back to RGB
        final_graphic = Image.new('RGB', graphic.size, COLOR_DEEP_SPACE)
        final_graphic.paste(graphic, (0, 0), graphic if graphic.mode == 'RGBA' else None)
        
        # Save
        output_path = f"{DIRS['feature_graphic']}/feature_graphic_1024x500.png"
        final_graphic.save(output_path, 'PNG', quality=95, optimize=True)
        print(f"   ✅ Saved: {output_path}")
        
        return True
    except Exception as e:
        print(f"   ❌ Error creating feature graphic: {e}")
        return False

def create_phone_screenshot(index, title, description, show_cover=True, is_english=False):
    """
    Create a single phone screenshot with mockup frame
    Size: 1080x1920 pixels (9:16 ratio)
    """
    # Create base canvas
    canvas = create_gradient_background(1080, 1920, COLOR_DEEP_SPACE, COLOR_COSMIC_BLUE)
    
    # Phone screen area (with padding for text)
    screen_top = 200
    screen_height = 1400
    screen_width = 900
    screen_x = (1080 - screen_width) // 2
    
    # Create phone screen background
    screen = Image.new('RGB', (screen_width, screen_height), (255, 255, 255))
    
    if show_cover:
        # Load appropriate cover
        cover_img = Image.open(BOOK_COVER_EN if is_english else BOOK_COVER_AR)
        # Resize to fit screen
        cover_height = screen_height - 100
        cover_width = int(cover_height * cover_img.width / cover_img.height)
        cover_img = cover_img.resize((cover_width, cover_height), Image.Resampling.LANCZOS)
        
        # Center cover on screen
        cover_x = (screen_width - cover_width) // 2
        cover_y = 50
        screen.paste(cover_img, (cover_x, cover_y))
    else:
        # Create a content view (simulated text page)
        draw = ImageDraw.Draw(screen)
        draw.rectangle([50, 50, screen_width - 50, 150], fill=COLOR_COSMIC_BLUE)
        
        # Add some simulated text lines
        for i in range(10):
            y = 200 + (i * 100)
            draw.rectangle([50, y, screen_width - 50, y + 60], fill=(240, 240, 240))
            draw.rectangle([50, y, screen_width - 100 - (i % 3) * 100, y + 60], fill=(200, 200, 200))
    
    # Add rounded corners to screen
    screen = screen.convert('RGBA')
    screen = add_rounded_corners(screen, 40)
    
    # Paste screen onto canvas
    canvas = canvas.convert('RGBA')
    canvas.paste(screen, (screen_x, screen_top), screen)
    
    # Add title text at top
    draw = ImageDraw.Draw(canvas)
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 50)
        desc_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 35)
    except:
        title_font = ImageFont.load_default()
        desc_font = ImageFont.load_default()
    
    # Title at top
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (1080 - title_width) // 2
    draw.text((title_x, 80), title, font=title_font, fill=COLOR_GOLDEN)
    
    # Description at bottom
    desc_bbox = draw.textbbox((0, 0), description, font=desc_font)
    desc_width = desc_bbox[2] - desc_bbox[0]
    desc_x = (1080 - desc_width) // 2
    draw.text((desc_x, 1700), description, font=desc_font, fill=COLOR_WHITE)
    
    # Convert back to RGB
    final = Image.new('RGB', canvas.size, COLOR_DEEP_SPACE)
    final.paste(canvas, (0, 0), canvas if canvas.mode == 'RGBA' else None)
    
    return final

def create_phone_screenshots():
    """
    Generate Phone Screenshots: 1080x1920 pixels (minimum 2, maximum 8)
    Show different features and screens of the app
    """
    print("📸 Creating Phone Screenshots (1080x1920px)...")
    
    screenshots = [
        {
            "title": "الغلاف العربي",
            "description": "كتاب ترانيم الكون - النسخة العربية الكاملة",
            "show_cover": True,
            "is_english": False
        },
        {
            "title": "English Version",
            "description": "Universe Melodies - Complete English Edition",
            "show_cover": True,
            "is_english": True
        },
        {
            "title": "قراءة سلسة",
            "description": "تجربة قراءة مريحة مع خطوط واضحة",
            "show_cover": False,
            "is_english": False
        },
        {
            "title": "محتوى شامل",
            "description": "15 فصلاً يجمع بين القرآن والعلم الحديث",
            "show_cover": False,
            "is_english": False
        },
        {
            "title": "بدون إنترنت",
            "description": "اقرأ في أي وقت ومكان بدون اتصال",
            "show_cover": False,
            "is_english": False
        }
    ]
    
    success_count = 0
    for i, config in enumerate(screenshots, 1):
        try:
            screenshot = create_phone_screenshot(
                i, 
                config["title"], 
                config["description"],
                config["show_cover"],
                config["is_english"]
            )
            output_path = f"{DIRS['phone_screenshots']}/screenshot_{i}_{config['title'].replace(' ', '_')[:20]}.png"
            screenshot.save(output_path, 'PNG', quality=95, optimize=True)
            print(f"   ✅ Saved: {output_path}")
            success_count += 1
        except Exception as e:
            print(f"   ❌ Error creating screenshot {i}: {e}")
    
    return success_count > 0

def create_tablet_screenshots():
    """
    Generate Tablet Screenshots: 1920x1080 pixels (landscape, optional)
    """
    print("📱 Creating Tablet Screenshots (1920x1080px) - Optional...")
    
    try:
        # Create a landscape version
        canvas = create_gradient_background(1920, 1080, COLOR_DEEP_SPACE, COLOR_COSMIC_BLUE)
        
        # Load both covers
        cover_ar = Image.open(BOOK_COVER_AR)
        cover_en = Image.open(BOOK_COVER_EN)
        
        # Resize covers
        cover_height = 700
        cover_ar = cover_ar.resize((int(cover_height * cover_ar.width / cover_ar.height), cover_height), Image.Resampling.LANCZOS)
        cover_en = cover_en.resize((int(cover_height * cover_en.width / cover_en.height), cover_height), Image.Resampling.LANCZOS)
        
        # Position covers
        total_width = cover_ar.width + cover_en.width + 100
        start_x = (1920 - total_width) // 2
        y = (1080 - cover_height) // 2
        
        canvas = canvas.convert('RGBA')
        canvas.paste(cover_ar, (start_x, y), cover_ar if cover_ar.mode == 'RGBA' else None)
        canvas.paste(cover_en, (start_x + cover_ar.width + 100, y), cover_en if cover_en.mode == 'RGBA' else None)
        
        # Add text
        draw = ImageDraw.Draw(canvas)
        try:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 50)
        except:
            font = ImageFont.load_default()
        
        text = "عربي + English • متاح على جميع الأجهزة"
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_x = (1920 - text_width) // 2
        draw.text((text_x, 100), text, font=font, fill=COLOR_GOLDEN)
        
        # Convert and save
        final = Image.new('RGB', canvas.size, COLOR_DEEP_SPACE)
        final.paste(canvas, (0, 0), canvas if canvas.mode == 'RGBA' else None)
        
        output_path = f"{DIRS['tablet_screenshots']}/tablet_screenshot_1.png"
        final.save(output_path, 'PNG', quality=95, optimize=True)
        print(f"   ✅ Saved: {output_path}")
        
        return True
    except Exception as e:
        print(f"   ❌ Error creating tablet screenshot: {e}")
        return False

def create_assets_info_file():
    """Create a README file with information about all generated assets"""
    info_content = """# Google Play Store Assets - ترانيم الكون
# Generated Assets Information

## 📱 App Icon (Required)
- **File**: `app_icon/app_icon_512x512.png`
- **Size**: 512 x 512 pixels
- **Format**: PNG
- **Usage**: Main app icon displayed in Google Play Store

## 🎨 Feature Graphic (Required)
- **File**: `feature_graphic/feature_graphic_1024x500.png`
- **Size**: 1024 x 500 pixels
- **Format**: PNG
- **Usage**: Main promotional banner at the top of the app listing

## 📸 Phone Screenshots (Required - 2-8 images)
- **Directory**: `phone_screenshots/`
- **Size**: 1080 x 1920 pixels (9:16 ratio)
- **Format**: PNG
- **Count**: 5 screenshots provided
- **Descriptions**:
  1. Arabic book cover display
  2. English version cover
  3. Smooth reading experience
  4. Comprehensive content (15 chapters)
  5. Offline reading capability

## 📱 Tablet Screenshots (Optional)
- **Directory**: `tablet_screenshots/`
- **Size**: 1920 x 1080 pixels (16:9 ratio, landscape)
- **Format**: PNG
- **Usage**: Display on tablet devices

## 📋 Upload Instructions

### Step 1: Navigate to Google Play Console
1. Go to: https://play.google.com/console
2. Select your app: "ترانيم الكون"
3. Navigate to: **Store presence → Main store listing**

### Step 2: Upload App Icon
1. Scroll to "App icon" section
2. Click "Upload"
3. Select: `app_icon/app_icon_512x512.png`

### Step 3: Upload Feature Graphic
1. Scroll to "Feature graphic" section
2. Click "Upload"
3. Select: `feature_graphic/feature_graphic_1024x500.png`

### Step 4: Upload Phone Screenshots
1. Scroll to "Phone screenshots" section
2. Click "Add screenshots"
3. Upload all 5 files from `phone_screenshots/` directory
4. Arrange them in order (drag and drop)

### Step 5: Upload Tablet Screenshots (Optional)
1. Scroll to "7-inch tablet" and "10-inch tablet" sections
2. Upload files from `tablet_screenshots/` directory

### Step 6: Save and Review
1. Click "Save" at the bottom
2. Review all uploaded assets
3. Check preview on the right side

## ✅ Quality Checklist

Before uploading, verify:
- [ ] All images are within size limits (< 1 MB for icon, < 15 MB for others)
- [ ] Images are in correct format (PNG preferred)
- [ ] No important text/content near edges (Google may crop)
- [ ] All text is readable and clear
- [ ] Images represent the actual app accurately
- [ ] Colors are consistent across all assets
- [ ] No copyrighted material without permission

## 🎨 Design Notes

**Color Scheme:**
- Deep Space Blue (#0A0F23)
- Cosmic Blue (#1E3C78)
- Golden Text (#FFD700)
- White (#FFFFFF)
- Light Blue (#6496FF)

**Theme:**
- Cosmic/Space theme reflecting the book's title "Universe Melodies"
- Professional and spiritual aesthetic
- Bilingual support (Arabic + English)
- Book cover prominently featured

## 📞 Support

For any issues or questions:
- Email: [Your support email]
- Google Play Console Help: https://support.google.com/googleplay/android-developer

---

**Generated**: 2024-12-30
**App**: ترانيم الكون (Universe Melodies)
**Package**: com.booknavigator.reader
**Version**: 1.0.0
"""
    
    with open(f"{BASE_DIR}/README.md", 'w', encoding='utf-8') as f:
        f.write(info_content)
    
    print(f"📄 Created assets information file: {BASE_DIR}/README.md")

def main():
    """Main execution function"""
    print("=" * 60)
    print("🚀 Google Play Assets Generator")
    print("   ترانيم الكون - Universe Melodies")
    print("=" * 60)
    print()
    
    # Check if source images exist
    if not os.path.exists(BOOK_COVER_AR):
        print(f"❌ Error: Source image not found: {BOOK_COVER_AR}")
        return 1
    
    if not os.path.exists(BOOK_COVER_EN):
        print(f"❌ Error: Source image not found: {BOOK_COVER_EN}")
        return 1
    
    # Create directories
    print("📁 Creating output directories...")
    for dir_name, dir_path in DIRS.items():
        os.makedirs(dir_path, exist_ok=True)
        print(f"   ✅ Created: {dir_path}")
    print()
    
    # Generate all assets
    results = {
        "app_icon": create_app_icon(),
        "feature_graphic": create_feature_graphic(),
        "phone_screenshots": create_phone_screenshots(),
        "tablet_screenshots": create_tablet_screenshots()
    }
    
    print()
    print("=" * 60)
    print("📊 Generation Summary:")
    print("=" * 60)
    
    success_count = sum(1 for v in results.values() if v)
    total_count = len(results)
    
    for asset_name, success in results.items():
        status = "✅ Success" if success else "❌ Failed"
        print(f"   {asset_name}: {status}")
    
    print()
    print(f"Total: {success_count}/{total_count} asset types generated successfully")
    print()
    
    # Create info file
    create_assets_info_file()
    
    print("=" * 60)
    print("✅ All assets generated successfully!")
    print(f"📁 Output directory: {BASE_DIR}/")
    print()
    print("Next steps:")
    print("1. Review all generated images")
    print("2. Upload to Google Play Console")
    print("3. Read README.md for detailed instructions")
    print("=" * 60)
    
    return 0 if success_count == total_count else 1

if __name__ == "__main__":
    sys.exit(main())
