import fitz
import os

pdf_path = "assets/pdf/fire_evac_system.pdf"
output_dir = "assets/pdf/fire_evac"

os.makedirs(output_dir, exist_ok=True)

doc = fitz.open(pdf_path)
for i in range(len(doc)):
    page = doc.load_page(i)
    pix = page.get_pixmap(dpi=150)
    output_file = os.path.join(output_dir, f"slide_{i+1}.png")
    pix.save(output_file)
    print(f"Saved {output_file}")
