import re

# ==========================================
# ROLE 2: ETL/ELT BUILDER
# ==========================================

def process_pdf_data(raw_json: dict) -> dict:
    """
    Xử lý dữ liệu từ nguồn PDF.
    """
    # Bước 1: Lấy nội dung thô và làm sạch nhiễu (Header/Footer)
    raw_text = raw_json.get("extractedText", "")
    
    # Sử dụng Regex để tìm và xóa 'HEADER_PAGE_X' hoặc 'FOOTER_PAGE_X' (X là số)
    # r'HEADER_PAGE_\d+|FOOTER_PAGE_\d+' có nghĩa là: 
    # Tìm chuỗi bắt đầu bằng HEADER_PAGE_ kèm theo chữ số (\d+) HOẶC FOOTER_PAGE_ kèm chữ số.
    cleaned_content = re.sub(r'HEADER_PAGE_\d+|FOOTER_PAGE_\d+', '', raw_text).strip()
    
    # Bước 2: Map dữ liệu thô sang định dạng chuẩn của UnifiedDocument
    # Dựa trên file doc1_messy.json, chúng ta ánh xạ các key tương ứng
    processed_doc = {
        "document_id": raw_json.get("docId", ""),
        "source_type": "PDF",
        "author": raw_json.get("authorName", "Unknown").strip(),
        "category": raw_json.get("docCategory", "General"),
        "content": cleaned_content,
        "timestamp": raw_json.get("createdAt", "")
    }
    
    return processed_doc

def process_video_data(raw_json: dict) -> dict:
    """
    Xử lý dữ liệu từ nguồn Video.
    """
    # Map dữ liệu thô từ Video sang định dạng chuẩn UnifiedDocument
    # Dựa trên file vid1_metadata.json, chúng ta ánh xạ các key tương ứng
    processed_doc = {
        "document_id": raw_json.get("video_id", ""),
        "source_type": "Video",
        "author": raw_json.get("creator_name", "Unknown"),
        "category": raw_json.get("category", "General"),
        "content": raw_json.get("transcript", ""),
        "timestamp": raw_json.get("published_timestamp", "")
    }
    
    return processed_doc
