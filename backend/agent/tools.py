from backend.scheduler.engine import check_availability, book, cancel_booking
from backend.utils.date_parser import normalize_date


def handle_tools(data, session):
    intent = data.get("intent") or "book"

    doctor = data.get("doctor") or session.get("doctor")
    raw_date = data.get("date") or session.get("date")
    time = data.get("time") or session.get("time")

    date = normalize_date(raw_date)

    # store memory
    if doctor:
        session["doctor"] = doctor.lower()
    if raw_date:
        session["date"] = raw_date
    if time:
        session["time"] = time

    # ================= BOOK =================
    if intent == "book":

        if not doctor:
            return "Which doctor would you like?"

        if not date:
            return "Which date?"

        if not time:
            slots = check_availability(doctor, date)
            return f"Available slots: {slots}"

        result = book(doctor, date, time)

        if "error" in result:
            slots = check_availability(doctor, date)
            return f"That slot is busy. Try: {slots}"

        return f"✅ Booked with {doctor} at {time}"

    # ================= CANCEL =================
    if intent == "cancel":
        if not doctor or not date:
            return "Which appointment do you want to cancel?"

        cancel_booking(doctor, date)
        return "❌ Appointment cancelled"

    # ================= RESCHEDULE =================
    if intent == "reschedule":
        if not doctor or not date:
            return "Tell me which appointment to reschedule."

        if not time:
            slots = check_availability(doctor, date)
            return f"Available new slots: {slots}"

        cancel_booking(doctor, date)
        book(doctor, date, time)

        return f"🔁 Rescheduled to {time}"

    return "Please provide details like doctor, date or time."