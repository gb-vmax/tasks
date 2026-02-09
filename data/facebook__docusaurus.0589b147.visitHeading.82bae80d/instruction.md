# Bug Report

### Describe the bug

The table of contents (TOC) is not being generated correctly for markdown headings. Level 2 headings (`##`) are no longer appearing in the TOC, only level 3 and deeper headings are being included.

### Reproduction

Create a markdown file with various heading levels:

```markdown
# Page Title

## Section 1
Some content here

### Subsection 1.1
More content

## Section 2
Additional content

### Subsection 2.1
Even more content
```

Expected TOC structure:
- Section 1
  - Subsection 1.1
- Section 2
  - Subsection 2.1

Actual TOC structure:
- Subsection 1.1
- Subsection 2.1

The level 2 headings (Section 1, Section 2) are missing from the generated table of contents.

### Expected behavior

Level 2 headings should be included in the TOC. Only the level 1 heading (page title) should be excluded, as it represents the document title.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
