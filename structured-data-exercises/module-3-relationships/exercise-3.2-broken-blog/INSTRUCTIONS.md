# Exercise 3.2 -- Broken Blog

**Debug**: Relationships -- Find and fix 5 relationship configuration bugs in a blog system

## Goal

Fix 5 relationship configuration bugs in a blog platform with Author, Post, and Comment models. Each bug is a different category of relationship misconfiguration: back_populates mismatch, missing cascade option, wrong model reference, wrong table name in ForeignKey, and missing tablename.

## What You Have

- `broken_blog.py` -- Author, Post, and Comment models with 5 relationship bugs. The intent is clear (authors write posts, posts have comments), but the configuration is wrong in five different ways.
- `test_relationships.py` -- A test suite that creates authors with posts and comments, tests navigation, and verifies cascade behavior. Currently fails.

## Your Tasks

### Step 1: Run the Tests

Run `python test_relationships.py` and observe the errors. Each error points to a different relationship misconfiguration.

### Step 2: Examine the Relationships

Open `broken_blog.py` and carefully examine every `relationship()` call and every `ForeignKey` reference. For each one, check:
- Does `back_populates` on model A match the attribute name on model B?
- Does the `ForeignKey` reference the correct table name (not class name)?
- Does every model have `__tablename__`?
- Is `cascade` configured correctly for parent-child relationships?

### Step 3: Fix All Five Bugs

The five bugs are:
1. `back_populates` mismatch between Author and Post
2. Missing `delete-orphan` in Post.comments cascade
3. Wrong model name in Comment.post relationship
4. Wrong table name in Post.author_id ForeignKey
5. Missing `__tablename__` on Comment model

Fix each one and re-run the tests after each fix.

### Step 4: Verify Cascade Behavior

After all tests pass, manually test cascade delete:
1. Create an author with 2 posts, each with 3 comments
2. Delete the author
3. Verify that all posts and comments are removed (zero orphaned records)

## Expected Results

- All tests in `test_relationships.py` pass
- `author.posts` returns the author's posts
- `post.comments` returns the post's comments
- `post.author` returns the post's author
- Deleting an author cascades through posts to comments
- No orphaned records after cascade delete

## Reflection

1. Bug #1 (back_populates mismatch) is the most common relationship error. What naming convention would prevent it?
2. Why does SQLAlchemy reference table names (lowercase, plural) in ForeignKey but class names (capitalized, singular) in relationship()?
3. What is the difference between `cascade="all"` and `cascade="all, delete-orphan"`? When would you want one but not the other?
