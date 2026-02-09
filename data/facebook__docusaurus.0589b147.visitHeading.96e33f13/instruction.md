# Bug Report

### Describe the bug

The table of contents (TOC) generation is not working correctly for level 2 headings (##). After a recent change, h2 headings are no longer being included in the generated TOC, even though they should be.

### Reproduction

Create a markdown file with the following content:

```md
# Main Title

## Section 1

Some content here.

### Subsection 1.1

More content.

## Section 2

Additional content.
```

The generated TOC is missing the "Section 1" and "Section 2" entries. Only "Subsection 1.1" appears in the TOC.

### Expected behavior

The TOC should include all headings from level 2 and below (h2, h3, h4, etc.). Level 1 headings (h1) are correctly excluded as page titles, but h2 headings should be the top-level items in the TOC.

Expected TOC structure:
- Section 1
  - Subsection 1.1
- Section 2

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
