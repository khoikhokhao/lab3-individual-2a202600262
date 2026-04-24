# ==========================================
# ROLE 3: OBSERVABILITY & QA ENGINEER
# ==========================================

# ==========================================
# ROLE 3: OBSERVABILITY & QA ENGINEER
# ==========================================

def run_semantic_checks(doc_dict: dict) -> bool:
    """
    Cổng kiểm soát chất lượng: Chặn dữ liệu rác hoặc dữ liệu lỗi.
    """
    # Lấy nội dung cần kiểm tra
    content = doc_dict.get("content", "")
    
    # 1. Kiểm tra độ dài: Nếu content trống hoặc ngắn hơn 10 ký tự -> Trả về False
    if not content or len(content) < 10:
        return False
    
    # 2. Kiểm tra từ khóa lỗi (Toxic keywords)
    # Nếu nội dung chứa các cụm từ báo lỗi hệ thống, chúng ta loại bỏ bản ghi đó
    toxic_keywords = ["Null pointer exception", "OCR Error", "Traceback"]
    
    for keyword in toxic_keywords:
        if keyword in content:
            return False
            
    # Nếu vượt qua tất cả các kiểm tra trên, dữ liệu được coi là hợp lệ
    return True
