# Bug Report

### Describe the bug

I'm experiencing an issue with the table of contents (TOC) generation where heading items and slice items appear to be swapped in the output. When I have a document with both regular headings and TOC slices, they're being rendered in the wrong order or with incorrect structure.

### Reproduction

Create an MDX file with mixed heading types:

```mdx
# Main Title

Some content here

## Section 1

More content

### Subsection 1.1

Content in subsection
```

The generated TOC shows the wrong hierarchy - it looks like heading items are being treated as slices and vice versa. The nesting levels don't match what's actually in the document.

### Expected behavior

The TOC should correctly identify and render:
- Regular headings as heading items
- TOC slices as slice items

Each item type should maintain its proper structure and nesting in the generated table of contents.

### System Info
- Docusaurus version: latest
- Node version: 18.x

Has anyone else run into this? The TOC was working fine before, but now the structure seems completely inverted.

---
Repository: /testbed
