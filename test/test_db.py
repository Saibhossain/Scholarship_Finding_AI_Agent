from agent.db.database import SessionLocal
from agent.db.crud import update_profile, get_or_create_profile

db = SessionLocal()

session_id = "test_user"

# Create/update
profile = update_profile(db, session_id, {
    "name": "Rokib",
    "gpa": 3.8,
    "field": "Computer Science"
})

print("Updated:", profile.name, profile.gpa)

# Fetch
profile = get_or_create_profile(db, session_id)
print("Fetched:", profile.name, profile.field)

db.close()
