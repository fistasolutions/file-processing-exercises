"""
Test suite for Blog Platform relationships.
Run: python test_relationships.py

When all 5 bugs in broken_blog.py are fixed, all tests pass.
"""

import sys


def run_tests():
    errors = []
    passed = 0

    # ── Test 1: Import and create tables ─────────────────────────────
    print("Test 1: Importing models and creating tables...")
    try:
        from broken_blog import Base, Author, Post, Comment
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker

        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        print("  PASSED: Models imported and tables created")
        passed += 1
    except Exception as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 1: {e}")
        print(f"\nFix this error first -- cannot proceed without working models.")
        print(f"\nResults: {passed} passed, {len(errors)} failed")
        return False

    # ── Test 2: Create author with posts ─────────────────────────────
    print("Test 2: Creating author with posts...")
    try:
        author = Author(name="Jane Doe", email="jane@example.com", bio="Tech writer")
        post1 = Post(title="First Post", body="Hello World", author=author)
        post2 = Post(title="Second Post", body="More content", author=author)
        session.add(author)
        session.commit()

        assert author.id is not None, "Author not saved"
        assert len(author.posts) == 2, f"Expected 2 posts, got {len(author.posts)}"
        print("  PASSED: Author with posts created")
        passed += 1
    except Exception as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 2: {e}")

    # ── Test 3: Navigate post -> author ──────────────────────────────
    print("Test 3: Navigating post.author...")
    try:
        fetched_post = session.query(Post).filter_by(title="First Post").first()
        assert fetched_post is not None, "Post not found"
        assert fetched_post.author is not None, "post.author is None"
        assert fetched_post.author.name == "Jane Doe", f"Expected Jane Doe, got {fetched_post.author.name}"
        print("  PASSED: post.author navigation works")
        passed += 1
    except Exception as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 3: {e}")

    # ── Test 4: Create comments on a post ─────────────────────────────
    print("Test 4: Adding comments to a post...")
    try:
        comment1 = Comment(body="Great post!", commenter_name="Alice", post=post1)
        comment2 = Comment(body="Thanks for sharing", commenter_name="Bob", post=post1)
        comment3 = Comment(body="Interesting read", commenter_name="Charlie", post=post2)
        session.add_all([comment1, comment2, comment3])
        session.commit()

        assert len(post1.comments) == 2, f"Expected 2 comments on post1, got {len(post1.comments)}"
        assert len(post2.comments) == 1, f"Expected 1 comment on post2, got {len(post2.comments)}"
        print("  PASSED: Comments added to posts")
        passed += 1
    except Exception as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 4: {e}")

    # ── Test 5: Navigate comment -> post ──────────────────────────────
    print("Test 5: Navigating comment.post...")
    try:
        fetched_comment = session.query(Comment).filter_by(commenter_name="Alice").first()
        assert fetched_comment is not None, "Comment not found"
        assert fetched_comment.post is not None, "comment.post is None"
        assert fetched_comment.post.title == "First Post", f"Expected 'First Post', got '{fetched_comment.post.title}'"
        print("  PASSED: comment.post navigation works")
        passed += 1
    except Exception as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 5: {e}")

    # ── Test 6: Cascade delete - author -> posts -> comments ──────────
    print("Test 6: Testing cascade delete (author -> posts -> comments)...")
    try:
        # Count before delete
        author_count_before = session.query(Author).count()
        post_count_before = session.query(Post).count()
        comment_count_before = session.query(Comment).count()

        # Delete the author
        session.delete(author)
        session.commit()

        # Count after delete
        author_count_after = session.query(Author).count()
        post_count_after = session.query(Post).count()
        comment_count_after = session.query(Comment).count()

        assert author_count_after == author_count_before - 1, "Author not deleted"
        assert post_count_after == 0, f"Expected 0 posts after cascade delete, got {post_count_after}"
        assert comment_count_after == 0, f"Expected 0 comments after cascade delete, got {comment_count_after}"
        print("  PASSED: Cascade delete removed author, posts, and comments")
        passed += 1
    except Exception as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 6: {e}")

    # ── Test 7: Verify no orphaned records ────────────────────────────
    print("Test 7: Verifying no orphaned records remain...")
    try:
        orphaned_posts = session.query(Post).all()
        orphaned_comments = session.query(Comment).all()
        assert len(orphaned_posts) == 0, f"Found {len(orphaned_posts)} orphaned posts"
        assert len(orphaned_comments) == 0, f"Found {len(orphaned_comments)} orphaned comments"
        print("  PASSED: No orphaned records")
        passed += 1
    except Exception as e:
        print(f"  FAILED: {e}")
        errors.append(f"Test 7: {e}")

    session.close()

    # ── Summary ──────────────────────────────────────────────────────
    print(f"\n{'='*50}")
    print(f"Results: {passed}/7 tests passed")
    if errors:
        print(f"\nFailed tests:")
        for err in errors:
            print(f"  - {err}")
        return False
    else:
        print("\nAll tests passed! All 5 bugs are fixed.")
        return True


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
