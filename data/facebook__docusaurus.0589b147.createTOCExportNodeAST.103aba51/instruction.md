# Bug Report

### Describe the bug

I'm experiencing an issue with the table of contents (TOC) generation in MDX files. When using heading-type TOC items, the generated AST appears to be incorrect, causing the TOC to render incorrectly or not at all.

### Reproduction

Create an MDX file with headings that should appear in the TOC:

```md
# Main Heading

Some content here.

## Subheading 1

More content.

## Subheading 2

Even more content.
```

When the MDX loader processes this file, the TOC export doesn't generate the correct structure for heading items. The rendered TOC is malformed or missing expected heading entries.

### Expected behavior

The TOC should correctly identify and render all heading-type items with their proper structure. Heading items should be processed differently from slice items in the AST generation.

### System Info

- Docusaurus version: latest
- Node version: 18.x

This seems to have started recently. Not sure if this is related to recent changes in the MDX loader or TOC processing logic.

---
Repository: /testbed
