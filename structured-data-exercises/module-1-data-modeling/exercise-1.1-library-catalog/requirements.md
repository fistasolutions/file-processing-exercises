# Greenfield Public Library -- Digital Catalog System Requirements

## Overview

The Greenfield Public Library currently tracks its collection in a spreadsheet. We need a proper database to manage our books, authors, and genres. This document describes what we need to store and the rules our data must follow.

---

## Entities

### Authors

Each author in our system has the following information:

| Field | Description | Rules |
|-------|-------------|-------|
| Name | Full name of the author | Required. Maximum 200 characters. No two authors should have the exact same name. |
| Biography | A short biography of the author | Optional. Can be several paragraphs long (no length limit). |
| Birth Year | The year the author was born | Optional. Must be a whole number (e.g., 1965, not "nineteen sixty-five"). |

### Genres

Each genre has:

| Field | Description | Rules |
|-------|-------------|-------|
| Name | The genre name | Required. Maximum 100 characters. Must be unique (no duplicate genre names). |
| Description | What this genre includes | Optional. A sentence or two explaining the genre. Maximum 500 characters. |

### Books

Each book has:

| Field | Description | Rules |
|-------|-------------|-------|
| Title | The book's title | Required. Maximum 300 characters. |
| ISBN | International Standard Book Number | Required. Must be unique across all books. Exactly 13 characters (ISBN-13 format). |
| Publication Year | Year the book was published | Required. Must be a whole number. |
| Page Count | Number of pages | Optional. Must be a positive whole number if provided. |
| Author | Who wrote the book | Required. Each book has exactly one author. The author must already exist in the system. |
| Genre | The book's genre | Required. Each book has exactly one genre. The genre must already exist in the system. |

---

## Relationships

- Each **book** belongs to exactly one **author** and exactly one **genre**.
- Each **author** can have written many books (or none, if they were just added to the system).
- Each **genre** can contain many books (or none).

---

## Sample Data

Here are some records from our current spreadsheet to help you understand the data:

### Authors

| Name | Biography | Birth Year |
|------|-----------|------------|
| Harper Lee | American novelist known for To Kill a Mockingbird | 1926 |
| George Orwell | English novelist and essayist, born Eric Arthur Blair | 1903 |
| Jane Austen | English novelist known for romantic fiction set among the landed gentry | 1775 |
| Gabriel Garcia Marquez | Colombian novelist and Nobel Prize laureate | 1927 |
| Toni Morrison | American novelist and Nobel Prize winner in Literature | 1931 |
| Frank Herbert | American science fiction author | 1920 |
| Ursula K. Le Guin | American author known for science fiction and fantasy | 1929 |
| Chimamanda Ngozi Adichie | Nigerian author and public speaker | 1977 |
| Kazuo Ishiguro | British novelist born in Japan, Nobel Prize in Literature 2017 | 1954 |
| Margaret Atwood | Canadian poet, novelist, and environmental activist | 1939 |

### Genres

| Name | Description |
|------|-------------|
| Literary Fiction | Character-driven narratives exploring the human condition |
| Science Fiction | Speculative fiction dealing with imaginative concepts such as advanced technology and space exploration |
| Dystopian | Fiction set in a dark, oppressive future society |
| Romance | Stories focused on romantic relationships between characters |
| Magical Realism | Realistic narrative with magical or fantastical elements treated as ordinary |
| Fantasy | Fiction featuring supernatural or magical elements not found in the real world |

### Books

| Title | ISBN | Year | Pages | Author | Genre |
|-------|------|------|-------|--------|-------|
| To Kill a Mockingbird | 9780061120084 | 1960 | 281 | Harper Lee | Literary Fiction |
| 1984 | 9780451524935 | 1949 | 328 | George Orwell | Dystopian |
| Animal Farm | 9780451526342 | 1945 | 112 | George Orwell | Dystopian |
| Pride and Prejudice | 9780141439518 | 1813 | 432 | Jane Austen | Romance |
| Sense and Sensibility | 9780141439662 | 1811 | 409 | Jane Austen | Romance |
| One Hundred Years of Solitude | 9780060883287 | 1967 | 417 | Gabriel Garcia Marquez | Magical Realism |
| Love in the Time of Cholera | 9780307389732 | 1985 | 368 | Gabriel Garcia Marquez | Magical Realism |
| Beloved | 9781400033416 | 1987 | 324 | Toni Morrison | Literary Fiction |
| Song of Solomon | 9781400033423 | 1977 | 337 | Toni Morrison | Literary Fiction |
| Dune | 9780441013593 | 1965 | 688 | Frank Herbert | Science Fiction |
| The Left Hand of Darkness | 9780441478125 | 1969 | 304 | Ursula K. Le Guin | Science Fiction |
| A Wizard of Earthsea | 9780547722023 | 1968 | 183 | Ursula K. Le Guin | Fantasy |
| Americanah | 9780307455925 | 2013 | 477 | Chimamanda Ngozi Adichie | Literary Fiction |
| Half of a Yellow Sun | 9781400095209 | 2006 | 541 | Chimamanda Ngozi Adichie | Literary Fiction |
| The Remains of the Day | 9780679731726 | 1989 | 245 | Kazuo Ishiguro | Literary Fiction |
| Never Let Me Go | 9781400078776 | 2005 | 288 | Kazuo Ishiguro | Science Fiction |
| The Handmaid's Tale | 9780385490818 | 1985 | 311 | Margaret Atwood | Dystopian |
| Oryx and Crake | 9780385721677 | 2003 | 374 | Margaret Atwood | Science Fiction |

---

## Edge Cases to Consider

1. Some authors have no biography -- the library has not gotten around to writing one yet.
2. Some books have no page count listed (older editions where that data was lost).
3. ISBN must be unique -- we once had two copies of the same book entered with the same ISBN and it caused confusion in our checkout system.
4. Author names should be unique in our system. If two authors share a name, we add a middle initial or birth year to distinguish them.
5. Genre names must be unique. We do not want "Science Fiction" and "Science fiction" as separate genres.

---

## Success Criteria

The database should:
- Store all 18 sample books with their authors and genres
- Reject any book submitted without a title or ISBN
- Reject any book with a duplicate ISBN
- Allow querying all books by a specific author
- Allow querying all books in a specific genre
