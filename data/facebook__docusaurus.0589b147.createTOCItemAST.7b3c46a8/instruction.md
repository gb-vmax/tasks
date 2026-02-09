# Bug Report

### Describe the bug

The table of contents (TOC) generation is producing incorrect output - headings and slices appear to be swapped in the generated TOC structure. When I have a document with both regular headings and heading slices, they're being rendered in the wrong format.

### Reproduction

Create an MDX file with mixed heading types:

```md
# Main Heading

## Section 1

### Subsection 1.1

## Section 2
```

The generated TOC shows sections where subsections should be and vice versa. The hierarchy looks completely inverted from what it should be.

### Expected behavior

The TOC should correctly represent headings as headings and slices as slices, maintaining the proper document structure and hierarchy.

### System Info
- Docusaurus version: latest
- Package: @docusaurus/mdx-loader

---
Repository: /testbed
