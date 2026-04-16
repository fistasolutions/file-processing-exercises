"""
Contact Book Application
Currently uses in-memory SQLite. Your task: deploy to Neon PostgreSQL.
"""

from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True)
    phone = Column(String(20))
    notes = Column(Text)

    def __repr__(self):
        return f"<Contact: {self.name} ({self.email})>"


# ── Database Connection ──────────────────────────────────────────────
# TODO: Replace this with DATABASE_URL from environment variable
# TODO: Add connection pooling configuration
engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


# ── CRUD Operations ──────────────────────────────────────────────────

def add_contact(name, email=None, phone=None, notes=None):
    """Create a new contact."""
    session = Session()
    contact = Contact(name=name, email=email, phone=phone, notes=notes)
    session.add(contact)
    session.commit()
    contact_id = contact.id
    session.close()
    return contact_id


def get_contact(contact_id):
    """Get a contact by ID."""
    session = Session()
    contact = session.get(Contact, contact_id)
    if contact:
        result = {
            "id": contact.id,
            "name": contact.name,
            "email": contact.email,
            "phone": contact.phone,
            "notes": contact.notes,
        }
    else:
        result = None
    session.close()
    return result


def search_contacts(name_fragment):
    """Search contacts by name."""
    session = Session()
    contacts = session.query(Contact).filter(
        Contact.name.contains(name_fragment)
    ).all()
    results = [
        {"id": c.id, "name": c.name, "email": c.email, "phone": c.phone}
        for c in contacts
    ]
    session.close()
    return results


def update_contact(contact_id, **kwargs):
    """Update a contact's fields."""
    session = Session()
    contact = session.get(Contact, contact_id)
    if not contact:
        session.close()
        return False
    for key, value in kwargs.items():
        if hasattr(contact, key):
            setattr(contact, key, value)
    session.commit()
    session.close()
    return True


def delete_contact(contact_id):
    """Delete a contact by ID."""
    session = Session()
    contact = session.get(Contact, contact_id)
    if not contact:
        session.close()
        return False
    session.delete(contact)
    session.commit()
    session.close()
    return True


def list_all_contacts():
    """List all contacts."""
    session = Session()
    contacts = session.query(Contact).order_by(Contact.name).all()
    results = [
        {"id": c.id, "name": c.name, "email": c.email, "phone": c.phone}
        for c in contacts
    ]
    session.close()
    return results


# ── Main ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Contact Book -- SQLite Demo")
    print("=" * 40)

    # Add sample contacts
    id1 = add_contact("Alice Johnson", "alice@example.com", "555-0101", "Met at conference")
    id2 = add_contact("Bob Smith", "bob@example.com", "555-0202", "College friend")
    id3 = add_contact("Carol Williams", "carol@example.com", "555-0303")

    # List all
    print("\nAll contacts:")
    for c in list_all_contacts():
        print(f"  {c['name']} -- {c['email']} -- {c['phone']}")

    # Search
    print("\nSearch for 'li':")
    for c in search_contacts("li"):
        print(f"  {c['name']}")

    # Update
    update_contact(id1, phone="555-9999")
    print(f"\nUpdated Alice's phone: {get_contact(id1)['phone']}")

    # Delete
    delete_contact(id3)
    print(f"\nAfter deleting Carol: {len(list_all_contacts())} contacts remain")

    print("\nDone! All operations work on SQLite.")
    print("Next step: deploy to Neon PostgreSQL.")
