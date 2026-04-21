sessions = {}

def get_session(session_id):
    if session_id not in sessions:
        sessions[session_id] = {
            "doctor": None,
            "date": None,
            "time": None
        }
    return sessions[session_id]

def update_session(session_id, data):
    sessions[session_id] = data