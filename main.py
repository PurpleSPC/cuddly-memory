# main.py
import argparse
from app.db.database import init_db, get_session
from app.db.seed import seed_data
from sqlmodel import text

def run_init():
    print("📦 Initializing database...")
    init_db()
    print("✅ Tables created.")

def run_seed():
    print("🌱 Seeding data...")
    seed_data()
    print("✅ Seed complete.")

def run_check():
    print("🔍 Checking DB connectivity...")
    with get_session() as session:
        try:
            session.exec(text("SELECT 1")).first()
            print("✅ Database connection is healthy!")
        except Exception as e:
            print(f"❌ Check failed: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Manage your database.")
    parser.add_argument("command", choices=["init", "seed", "check", "all"], help="Choose an action")

    args = parser.parse_args()

    if args.command == "init":
        run_init()
    elif args.command == "seed":
        run_seed()
    elif args.command == "check":
        run_check()
    elif args.command == "all":
        run_init()
        run_seed()
        run_check()