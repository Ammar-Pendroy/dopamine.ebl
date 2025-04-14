# LOYALTY SYSTEM

def get_loyalty_points(user_id="guest"):
    try:
        doc = db.collection("loyalty_points").document(user_id).get()
        if doc.exists:
            return doc.to_dict().get("points", 0)
    except:
        pass
    return 0

def increment_loyalty_points(user_id="guest"):
    ref = db.collection("loyalty_points").document(user_id)
    current = get_loyalty_points(user_id)
    ref.set({"points": current + 1})

def reset_loyalty_points(user_id="guest"):
    db.collection("loyalty_points").document(user_id).set({"points": 0})
