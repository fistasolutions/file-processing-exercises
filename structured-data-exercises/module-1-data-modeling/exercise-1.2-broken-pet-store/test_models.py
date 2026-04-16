"""
Test suite for Pet Store models.
Run: python test_models.py

When all 6 bugs in broken_models.py are fixed, all tests pass.
"""

import sys


def run_tests():
    errors = []
    passed = 0

    # ── Test 1: Import the models ────────────────────────────────────
    print("Test 1: Importing models...")
    try:
        from broken_models import Base, Owner, Pet, Vet
        print("  PASSED: Models imported successfully")
        passed += 1
    except ImportError as e:
        print(f"  FAILED: Import error -- {e}")
        errors.append(f"Test 1: {e}")
        print(f"\n{len(errors)} test(s) failed. Fix the import error first.")
        return False
    except Exception as e:
        print(f"  FAILED: Unexpected error -- {e}")
        errors.append(f"Test 1: {e}")
        print(f"\n{len(errors)} test(s) failed. Fix this error first.")
        return False

    # ── Test 2: Create tables ────────────────────────────────────────
    print("Test 2: Creating tables...")
    try:
        from sqlalchemy import create_engine
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        print("  PASSED: Tables created successfully")
        passed += 1
    except Exception as e:
        print(f"  FAILED: Could not create tables -- {e}")
        errors.append(f"Test 2: {e}")
        print(f"\n{len(errors)} test(s) failed. Fix table creation errors.")
        return False

    # ── Test 3: Insert an owner ──────────────────────────────────────
    print("Test 3: Inserting an owner...")
    try:
        from sqlalchemy.orm import sessionmaker
        Session = sessionmaker(bind=engine)
        session = Session()

        owner1 = Owner(name="Alice Johnson", email="alice@example.com", phone="555-0101")
        session.add(owner1)
        session.commit()

        fetched = session.query(Owner).filter_by(name="Alice Johnson").first()
        assert fetched is not None, "Owner not found after insert"
        assert fetched.email == "alice@example.com", f"Expected alice@example.com, got {fetched.email}"
        print("  PASSED: Owner inserted and retrieved")
        passed += 1
    except Exception as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 3: {e}")

    # ── Test 4: Insert a pet with owner relationship ─────────────────
    print("Test 4: Inserting a pet linked to an owner...")
    try:
        pet1 = Pet(name="Buddy", species="Dog", breed="Golden Retriever", age=3, weight=30, owner_id=owner1.id)
        session.add(pet1)
        session.commit()

        fetched_pet = session.query(Pet).filter_by(name="Buddy").first()
        assert fetched_pet is not None, "Pet not found after insert"
        assert fetched_pet.species == "Dog", f"Expected Dog, got {fetched_pet.species}"
        assert fetched_pet.owner_id == owner1.id, "Pet owner_id does not match"
        print("  PASSED: Pet inserted and linked to owner")
        passed += 1
    except Exception as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 4: {e}")

    # ── Test 5: Navigate owner -> pets relationship ──────────────────
    print("Test 5: Navigating owner.pets relationship...")
    try:
        session.refresh(owner1)
        assert len(owner1.pets) == 1, f"Expected 1 pet, got {len(owner1.pets)}"
        assert owner1.pets[0].name == "Buddy", f"Expected Buddy, got {owner1.pets[0].name}"
        print("  PASSED: owner.pets navigation works")
        passed += 1
    except Exception as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 5: {e}")

    # ── Test 6: Pet name is stored as string ─────────────────────────
    print("Test 6: Verifying pet name is a string type...")
    try:
        pet2 = Pet(name="Whiskers", species="Cat", breed="Siamese", age=5, weight=4, owner_id=owner1.id)
        session.add(pet2)
        session.commit()

        fetched = session.query(Pet).filter_by(name="Whiskers").first()
        assert fetched is not None, "Pet with string name not found"
        assert isinstance(fetched.name, str), f"Expected str, got {type(fetched.name)}"
        print("  PASSED: Pet name stored and retrieved as string")
        passed += 1
    except Exception as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 6: {e}")

    # ── Test 7: Owner email uniqueness ───────────────────────────────
    print("Test 7: Testing owner email uniqueness constraint...")
    try:
        duplicate_owner = Owner(name="Bob Smith", email="alice@example.com", phone="555-0202")
        session.add(duplicate_owner)
        try:
            session.commit()
            # If we reach here, the unique constraint is missing
            print("  FAILED: Duplicate email was accepted -- unique constraint missing")
            errors.append("Test 7: Duplicate email accepted (unique=True missing on Owner.email)")
            session.rollback()
        except Exception:
            session.rollback()
            print("  PASSED: Duplicate email correctly rejected")
            passed += 1
    except Exception as e:
        print(f"  FAILED: Unexpected error -- {e}")
        errors.append(f"Test 7: {e}")

    # ── Test 8: Vet license_number is required ───────────────────────
    print("Test 8: Testing vet license_number is required...")
    try:
        vet_no_license = Vet(name="Dr. Smith", specialty="Surgery", license_number=None)
        session.add(vet_no_license)
        try:
            session.commit()
            # If we reach here, nullable=False is missing
            print("  FAILED: Vet without license was accepted -- nullable=False missing")
            errors.append("Test 8: Null license accepted (nullable=False missing on Vet.license_number)")
            session.rollback()
        except Exception:
            session.rollback()
            print("  PASSED: Vet without license correctly rejected")
            passed += 1
    except Exception as e:
        print(f"  FAILED: Unexpected error -- {e}")
        errors.append(f"Test 8: {e}")

    # ── Test 9: Insert a valid vet ───────────────────────────────────
    print("Test 9: Inserting a valid vet...")
    try:
        vet = Vet(name="Dr. Sarah Chen", specialty="Dermatology", license_number="VET-2024-001", clinic_name="Happy Paws Clinic")
        session.add(vet)
        session.commit()

        fetched_vet = session.query(Vet).filter_by(license_number="VET-2024-001").first()
        assert fetched_vet is not None, "Vet not found after insert"
        assert fetched_vet.name == "Dr. Sarah Chen", f"Expected Dr. Sarah Chen, got {fetched_vet.name}"
        print("  PASSED: Vet inserted successfully")
        passed += 1
    except Exception as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 9: {e}")

    session.close()

    # ── Summary ──────────────────────────────────────────────────────
    print(f"\n{'='*50}")
    print(f"Results: {passed}/9 tests passed")
    if errors:
        print(f"\nFailed tests:")
        for err in errors:
            print(f"  - {err}")
        return False
    else:
        print("\nAll tests passed! All 6 bugs are fixed.")
        return True


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
