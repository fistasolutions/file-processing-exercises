# Team File Management Scenario

## The Team

You have been brought in to fix the file management chaos for a small product team of 3 people who share a project folder on a network drive (or shared cloud folder like Google Drive or Dropbox).

### Team Members

**Sarah -- Project Manager**

- Creates: project plans, meeting notes, status reports, client presentations, timelines
- File types: .docx, .pptx, .xlsx, .pdf, .md
- Workflow: Creates a new document for every meeting. Updates status reports weekly. Stores client-facing presentations separately from internal ones. Needs to find past meeting notes quickly.
- Pain point: "I can never find the meeting notes from two weeks ago. They're somewhere in the folder but I don't know where anyone put them."

**Alex -- Designer**

- Creates: mockups, wireframes, logos, brand assets, icon sets, design specifications
- File types: .png, .svg, .psd, .fig (Figma exports), .pdf (design specs), .zip (asset exports)
- Workflow: Creates multiple versions of each design (v1, v2, v3, final). Exports assets in multiple formats. Needs to keep source files (.psd, .fig) separate from exported files (.png, .svg). Shares final approved versions with the PM.
- Pain point: "There are 15 versions of the logo and I don't know which one the client approved. Also, my PSD files are huge and I don't want them backed up every day."

**Jordan -- Developer**

- Creates: source code, scripts, documentation, database schemas, API specs, deployment configs
- File types: .py, .js, .ts, .md, .yaml, .json, .sql, .sh, .dockerfile
- Workflow: Uses git for code version control but stores non-code documentation in the shared folder. Creates technical documentation that the PM needs to reference. Generates database schemas and API specs that the designer needs for mockups.
- Pain point: "I keep my code in git, but the shared folder has random config files and old scripts that nobody knows if they're still needed."

## Current Problems

1. **Everything in root**: All three team members dump files in the top-level folder. There are currently 200+ files with no organization.

2. **No naming convention**: Files are named inconsistently:
   - Sarah: "meeting notes 3-15.docx", "Meeting Notes March.docx", "notes-march-15.md"
   - Alex: "logo.png", "logo-v2.png", "logo-FINAL.png", "logo-FINAL-2.png", "logo-approved.png"
   - Jordan: "schema.sql", "schema-updated.sql", "schema-v3-DONT-USE.sql"

3. **Version chaos**: Nobody knows which version of a file is current. Old versions are not archived -- they just accumulate alongside current versions.

4. **Can't find anything**: All three team members spend 5-10 minutes per day searching for files that should be easy to find.

5. **Backup confusion**: The entire folder is backed up daily, but Alex's PSD files are 50-200 MB each, consuming most of the backup storage. Meanwhile, Jordan's critical deployment configs are not in the shared folder at all.

6. **No cleanup process**: Files from 6 months ago sit next to files from today. Nobody archives completed projects. Nobody deletes temp files.

## Requirements

Your file management system must address:

1. **Folder structure**: Where does each type of file go? How deep should nesting be? Should there be per-project folders, per-person folders, or per-type folders?

2. **Naming conventions**: How should files be named? Include conventions for:
   - Meeting notes (date, attendees, topic)
   - Design files (project, component, version)
   - Reports and presentations (type, date, audience)
   - Technical docs (component, type)
   - Versioning (how to indicate v1, v2, final)

3. **Version management**: How to handle multiple versions? Archive old versions? Indicate the current/approved version?

4. **Backup strategy**: What gets backed up, how often? How to handle large design files? Where do critical configs go?

5. **Search guidance**: How does each team member find common files quickly? What search strategies work for different file types?

6. **Cleanup process**: How often should old files be archived? Who is responsible? What qualifies as "old"?

7. **Onboarding**: If a 4th team member joins, what do they need to know on day one?

## Constraints

- The system must be simple enough that all three team members will actually follow it (complexity kills adoption)
- No specialized software -- use only folder structure, naming, and documentation
- Must work on any shared filesystem (Google Drive, Dropbox, network drive, or local folder)
- The system must handle files that do not exist yet -- it is forward-looking, not just a one-time cleanup
