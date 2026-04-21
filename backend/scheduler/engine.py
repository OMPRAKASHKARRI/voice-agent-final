from backend.db.connection import cursor

SLOTS = ["10:00", "14:00", "16:00"]


def check_availability(doctor, date):
    available = []

    for time in SLOTS:
        cursor.execute(
            "SELECT 1 FROM appointments WHERE doctor=%s AND date=%s AND time=%s",
            (doctor, date, time)
        )

        if cursor.fetchone() is None:
            available.append(time)

    return available


def book(doctor, date, time):
    cursor.execute(
        "SELECT 1 FROM appointments WHERE doctor=%s AND date=%s AND time=%s",
        (doctor, date, time)
    )

    if cursor.fetchone():
        return {"error": "conflict"}

    cursor.execute(
        "INSERT INTO appointments (doctor, date, time) VALUES (%s, %s, %s)",
        (doctor, date, time)
    )

    return {"success": True}


def cancel_booking(doctor, date):
    cursor.execute(
        "DELETE FROM appointments WHERE doctor=%s AND date=%s",
        (doctor, date)
    )