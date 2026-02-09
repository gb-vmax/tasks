# Bug Report

### Describe the bug

I'm experiencing an issue with the table of contents (TOC) generation where heading items are not being rendered correctly in the TOC. The TOC appears to be missing heading entries or displaying incorrect items.

### Reproduction

When I create a document with headings like this:

```md
# Main Title

## Section 1
Some content here

## Section 2
More content

### Subsection 2.1
Nested content
```

The generated TOC doesn't show the headings properly. It seems like heading items are being treated as slice items or something similar.

### Expected behavior

The TOC should correctly display all heading items with their proper types. Each heading should appear in the TOC structure as a heading item, not as a slice or other type.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems to have started happening recently. Not sure if it's related to a recent change in the MDX loader.

---
Repository: /testbed
