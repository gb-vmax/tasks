# Bug Report

### Describe the bug

I'm experiencing an issue with the table of contents (TOC) generation in MDX files. After a recent update, the TOC export seems to be malformed and causing runtime errors when trying to render the TOC on the page.

### Reproduction

Create an MDX file with headings that should appear in the TOC:

```mdx
# Main Heading

Some content here.

## Subheading 1

More content.

## Subheading 2

Even more content.
```

When the page loads, the TOC doesn't render correctly and throws errors in the browser console related to invalid AST structure.

### Expected behavior

The TOC should be properly generated and exported, allowing it to render correctly on the page with all the headings listed in a hierarchical structure.

### System Info

- Docusaurus version: latest
- Node version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
