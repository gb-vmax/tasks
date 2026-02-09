# Bug Report

### Describe the bug

Table of contents (TOC) generation is not working correctly for heading levels. After a recent change, headings with depth 2 (## headings) are no longer appearing in the generated TOC, but they should be included.

### Reproduction

Create a markdown file with various heading levels:

```md
# Page Title

## Section 1
Some content here

### Subsection 1.1
More content

## Section 2
Another section
```

Expected: The TOC should include "Section 1", "Subsection 1.1", and "Section 2"
Actual: Only "Subsection 1.1" appears in the TOC. The `##` level headings are missing.

### Expected behavior

Headings at depth 2 and below should be included in the table of contents. Only depth 1 headings (page titles) should be excluded from the TOC.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
