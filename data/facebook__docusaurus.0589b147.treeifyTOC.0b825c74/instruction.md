# Bug Report

### Describe the bug

The table of contents (TOC) tree structure is being built incorrectly when dealing with nested headings. When I have headings at different levels (like H2, H3, H4), the parent-child relationships aren't being established properly, causing some headings to appear at the wrong nesting level in the TOC.

### Reproduction

Given a markdown document with the following heading structure:

```markdown
## H2 - Section 1
### H3 - Subsection 1.1
#### H4 - Subsubsection 1.1.1
## H2 - Section 2
```

The TOC tree should show:
- H2 - Section 1
  - H3 - Subsection 1.1
    - H4 - Subsubsection 1.1.1
- H2 - Section 2

But instead, the H4 heading is being incorrectly associated with the wrong parent, resulting in a malformed tree structure.

### Expected behavior

Each heading should be correctly nested under its immediate parent heading based on the heading levels. An H4 should be a child of the preceding H3, an H3 should be a child of the preceding H2, etc.

### System Info

- Docusaurus version: latest
- Node version: 18.x

This seems to affect the sidebar navigation when using the TOC feature. The hierarchy doesn't match what's in the actual document.

---
Repository: /testbed
