# Bug Report

### Describe the bug

I'm experiencing an issue with MDX files that have multiple named exports. When I have more than one export statement in my MDX file, the table of contents (TOC) generation seems to break or not work as expected.

### Reproduction

Create an MDX file with multiple named exports:

```mdx
---
title: My Page
---

export const foo = 'bar';
export const baz = 'qux';

## Heading 1

Some content here.

## Heading 2

More content.
```

When processing this file, the TOC doesn't generate correctly even though the headings are valid.

### Expected behavior

The TOC should be generated properly regardless of how many named exports are in the MDX file. Multiple exports shouldn't interfere with the TOC generation.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
