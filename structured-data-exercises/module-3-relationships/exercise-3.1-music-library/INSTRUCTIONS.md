# Exercise 3.1 -- Music Library

**Build**: Relationships -- Add bidirectional relationships and cascade behavior to a music database

## Goal

Add `relationship()` definitions to a music database that already has foreign keys in place. After adding relationships, you will load sample data, write queries that navigate through relationships (artist.albums, album.tracks), and test cascade delete behavior.

## What You Have

- `models_no_relationships.py` -- Artist, Album, and Track models with correct columns and ForeignKey references, but NO `relationship()` definitions. You cannot currently navigate from an artist to their albums or from an album to its tracks.
- `sample_data.csv` -- 10 artists, 30 albums, and 100+ tracks with realistic music data. The CSV has columns: type (artist/album/track), plus type-specific fields.

## Your Tasks

### Step 1: Read the Current Models

Read `models_no_relationships.py` and note the foreign key columns: `Album.artist_id` references `artists.id`, and `Track.album_id` references `albums.id`. These are the "wires" -- but they are not "plugged in" to Python-level navigation yet.

### Step 2: Add Relationships

Modify the models to add `relationship()` with `back_populates` on all three models:

- `Artist.albums` -- one-to-many relationship to Album, with `cascade="all, delete-orphan"`
- `Album.artist` -- many-to-one relationship back to Artist
- `Album.tracks` -- one-to-many relationship to Track, with `cascade="all, delete-orphan"`
- `Track.album` -- many-to-one relationship back to Album

### Step 3: Load Sample Data

Write a script that reads `sample_data.csv` and populates the database. Process artists first, then albums (linking to artists), then tracks (linking to albums).

### Step 4: Write Navigation Queries

Write and execute these queries using relationship navigation (not manual JOINs):

1. Print all albums by a specific artist using `artist.albums`
2. Print all tracks on a specific album using `album.tracks`
3. For each artist, calculate total track duration (sum of all track durations across all their albums)

### Step 5: Test Cascade Delete

Delete one artist and verify that all their albums and tracks are also removed from the database. Print the count of remaining artists, albums, and tracks before and after the delete.

## Expected Results

- Models have bidirectional relationships: `artist.albums`, `album.artist`, `album.tracks`, `track.album` all work
- Sample data is loaded: 10 artists, 30 albums, 100+ tracks
- Navigation queries return correct results without manual JOIN/filter
- Deleting an artist cascades to remove their albums and tracks
- No orphaned records remain after cascade delete

## Reflection

1. What would happen if you set `cascade="all, delete-orphan"` on Track.album (the child side) instead of Album.tracks (the parent side)?
2. If an album could have multiple artists (a collaboration), how would you change the relationship model? What new table would you need?
3. Why does SQLAlchemy require `back_populates` on both sides? What happens if you only put it on one side?
