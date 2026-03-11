Hey, I need help automating a small part of our infrastructure provisioning pipeline. We have a Terraform module repository at `/home/user/infra-modules` and I need you to do a patch version bump and record it in our changelog.

Here's exactly what I need done:

**1. Read the current version**

The current version is stored in `/home/user/infra-modules/VERSION`. It contains a single line with a semantic version like `MAJOR.MINOR.PATCH`. You need to read it, increment the PATCH number by 1, and write the new version back to `/home/user/infra-modules/VERSION`. The file should contain only the new version string followed by a newline — no extra whitespace or blank lines.

**2. Append a changelog entry**

The changelog lives at `/home/user/infra-modules/CHANGELOG.md`. It already has some content. You need to **prepend** a new entry at the top of the file (right after the `# Changelog` header line) with this exact format:

```
## [<new_version>] - 2024-11-15
### Changed
- Bumped patch version for provisioning pipeline release
```

So the new entry block should appear between the `# Changelog` header and whatever existing entries are already there. There should be exactly one blank line between the `# Changelog` header and the new `## [...]` entry, and exactly one blank line between the end of the new entry and the start of the next existing entry.

**3. Write a release notes file**

Create a new file at `/home/user/infra-modules/RELEASE_NOTES.txt` containing exactly:

```
Release: <new_version>
Date: 2024-11-15
Type: patch
Description: Bumped patch version for provisioning pipeline release
```

Where `<new_version>` is the bumped version you computed in step 1. No trailing blank lines — the file should end right after the last line.

To be concrete about what "exactly" means for all files: I'll be running automated checks on the byte-level content, so please make sure there are no extra spaces, no extra blank lines, and no missing newlines at the end of files.
