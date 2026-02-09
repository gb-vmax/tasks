# Bug Report

### Describe the bug

The table of contents (TOC) generation is producing incorrect output where the heading text and IDs are swapped. When generating a TOC, the `value` field contains the heading ID instead of the actual heading text, and the `id` field contains the heading text instead of the ID.

### Reproduction

Create an MDX file with headings:

```md
## Introduction
Some content here

## Getting Started
More content
```

The generated TOC items will have:
```js
{
  value: 'introduction',  // This should be "Introduction"
  id: 'Introduction',      // This should be 'introduction'
  level: 2
}
```

### Expected behavior

The TOC should correctly map heading text to the `value` field and the generated ID to the `id` field:

```js
{
  value: 'Introduction',
  id: 'introduction',
  level: 2
}
```

This appears to have broken recently - the values are being assigned to the wrong properties during TOC generation.

---
Repository: /testbed
