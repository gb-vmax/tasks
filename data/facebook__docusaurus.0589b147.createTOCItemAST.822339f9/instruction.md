# Bug Report

### Describe the bug

The table of contents (TOC) generation is producing incorrect output. When I have a mix of headings and slice items in my markdown, they appear to be swapped in the generated TOC structure.

### Reproduction

Create a markdown file with headings and TOC slices:

```md
# Main Title

Some content here

## Section 1

More content

<!-- truncate -->

## Section 2

Final content
```

When the TOC is generated, the heading items are being rendered as slices and slice items are being rendered as headings. The entire TOC structure appears inverted from what it should be.

### Expected behavior

The TOC should correctly identify and render:
- Heading items as headings with proper hierarchy
- Slice items (like `<!-- truncate -->`) as slice markers

Instead, these seem to be reversed in the output.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
