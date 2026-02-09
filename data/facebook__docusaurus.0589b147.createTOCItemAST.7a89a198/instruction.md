# Bug Report

### Describe the bug

I'm experiencing an issue with the table of contents (TOC) generation where heading items in the TOC are not being rendered correctly. It seems like all TOC items are being treated as slices instead of respecting their actual type.

### Reproduction

When generating a TOC with mixed heading and slice items:

```markdown
## Heading 1
Some content here

## Heading 2
More content

## Heading 3
Final section
```

The TOC should show individual heading entries, but instead they appear to be processed incorrectly. The structure looks wrong and headings don't link properly to their corresponding sections.

### Expected behavior

Each heading type item in the TOC should be processed as a heading and rendered with the appropriate structure. Slice items should be processed separately as slices. The TOC should correctly distinguish between these two types and handle them differently.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
