from pdf2image import convert_from_path
import pytesseract


def pdf_to_text(pdf_path, lang='jpn_vert'):
    print("Start")
    images = convert_from_path(pdf_path, poppler_path=r"C:\poppler-24.08.0\Library\bin")
    print(f"Detected {len(images)} pages.")

    text_output = []
    for i, img in enumerate(images):
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        text = pytesseract.image_to_string(img, lang=lang, config="--psm 12")
        text_output.append(text)
        print(f"Page {i + 1} done.")

    return " ".join(text_output)


if __name__ == "__main__":
    pdf_path = "C:/file.pdf"
    extracted_text = pdf_to_text(pdf_path)

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(extracted_text)

    print("Done")
