from datetime import datetime, timedelta

def normalize_date(date_str):
    if not date_str:
        return None

    text = str(date_str).lower()

    if text in ["tomorrow", "நாளை", "kal"]:
        return (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

    try:
        return datetime.strptime(text, "%Y-%m-%d").strftime("%Y-%m-%d")
    except:
        return None