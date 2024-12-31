import os
from pathlib import Path
import fitz  # PyMuPDF
from PIL import Image
import re

class PDFProcessor:
    def process_pdf(self, pdf_path, output_dir, course_name):
        """Process all slides in the PDF"""
        print("\nBearbetar PDF-slides...")
        processed_slides = []

        try:
            pdf_document = fitz.open(pdf_path)

            for page_num, page in enumerate(pdf_document):
                # Get slide number
                slide_number = str(page_num + 1)

                # Create high-quality image from page
                zoom = 4  # higher zoom for better quality
                mat = fitz.Matrix(zoom, zoom)
                pix = page.get_pixmap(matrix=mat, alpha=False)
                
                # Convert to PIL Image
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

                # Save image
                image_filename = f"{course_name}_slide_{slide_number}.png"
                image_path = os.path.join(output_dir, image_filename)
                img.save(image_path, "PNG", quality=100, optimize=False)

                processed_slides.append((image_path, slide_number))
                print(f"Bearbetade slide {slide_number}")

            pdf_document.close()
            return processed_slides

        except Exception as e:
            raise Exception(f"Fel vid bearbetning av PDF: {str(e)}")

class FileManager:
    def setup_directories(self, images_path, notes_path):
        """Create directories for images and notes"""
        Path(images_path).mkdir(parents=True, exist_ok=True)
        Path(notes_path).parent.mkdir(parents=True, exist_ok=True)

def main():
    print("PDF till Obsidian Anteckningar")
    print("-" * 30)

    # Get user inputs
    pdf_path = input("Sökväg till PDF: ").strip().strip("\"'")
    course_name = input("Vad heter kursen: ").strip()
    note_name = input("Vad ska anteckningen heta: ").strip()
    notes_path = input("Sökväg dit du vill ha anteckningen i Obsidian: ").strip().strip("\"'")
    images_base_path = input("Sökväg dit du vill ha mappen med bilder: ").strip().strip("\"'")

    # Setup paths
    image_folder_name = f"{course_name} - {note_name} - photos"
    images_dir = os.path.join(images_base_path, image_folder_name)
    note_path = os.path.join(notes_path, f"{note_name}.md")

    # Initialize classes
    file_manager = FileManager()
    pdf_processor = PDFProcessor()

    try:
        # Validate PDF exists
        if not os.path.exists(pdf_path):
            raise ValueError(f"PDF-filen hittades inte: {pdf_path}")

        # Setup directories
        print("\nSkapar mappar...")
        file_manager.setup_directories(images_dir, note_path)
        print(f"Skapade bildmapp: {images_dir}")

        # Process all slides from PDF
        slides = pdf_processor.process_pdf(pdf_path, images_dir, course_name)

        if not slides:
            raise ValueError("Inga slides kunde bearbetas från PDF:en.")

        print(f"\nBearbetade {len(slides)} slides från PDF:en")

        # Create note file with image references
        print("\nSkapar anteckningsfil...")
        with open(note_path, "w", encoding="utf-8") as note_file:
            for image_path, slide_number in slides:
                image_filename = os.path.basename(image_path)
                note_file.write(f"## Slide {slide_number}\n\n")
                note_file.write(f"![[{image_filename}]]\n\n")
                note_file.write("**Anteckning**:\n\n")

        print("\nProcess färdig!")
        print(f"Bilder sparade i: {images_dir}")
        print(f"Anteckningsfil skapad: {note_path}")

    except Exception as e:
        print(f"\nEtt fel uppstod: {str(e)}")

    input("\nTryck Enter för att avsluta...")

if __name__ == "__main__":
    main()