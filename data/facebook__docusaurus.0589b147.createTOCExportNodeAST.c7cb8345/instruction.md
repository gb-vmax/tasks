# Bug Report

### Describe the bug

The table of contents (TOC) generation is broken after a recent update. When building pages with MDX content, the TOC either doesn't appear or shows incorrect/missing entries.

### Reproduction

Create an MDX file with multiple headings:

```mdx
# Main Title

## Section 1
Some content here

## Section 2
More content

### Subsection 2.1
Nested content
```

After building, the generated TOC is incomplete or empty. Some heading entries that should appear in the navigation are missing.

### Expected behavior

All headings should be properly extracted and included in the table of contents. The TOC should display all heading levels correctly with their corresponding text and IDs.

### System Info
- Docusaurus version: Latest
- Node version: 18.x

This seems to have started happening recently, possibly after an update to the MDX loader. The TOC was working fine before.

---
Repository: /testbed
