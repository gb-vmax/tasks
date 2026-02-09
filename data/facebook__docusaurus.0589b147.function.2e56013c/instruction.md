# Bug Report

### Describe the bug

The table of contents (TOC) filtering is not working correctly. When setting `minHeadingLevel` and `maxHeadingLevel`, headings that should be filtered out are still appearing in the TOC.

### Reproduction

```js
const toc = [
  { level: 1, value: 'Heading 1' },
  { level: 2, value: 'Heading 2' },
  { level: 3, value: 'Heading 3' },
  { level: 4, value: 'Heading 4' },
];

const filtered = filterTOC({
  toc,
  minHeadingLevel: 2,
  maxHeadingLevel: 3
});

// Expected: Only headings with level 2 and 3
// Actual: Headings with level 1, 2, and 3 are included
```

### Expected behavior

When I set `minHeadingLevel: 2` and `maxHeadingLevel: 3`, only headings with levels 2 and 3 should appear in the filtered TOC. Headings with level 1 should be excluded, and headings with level 4 should also be excluded.

Currently, it seems like headings below the minimum level are being included when they shouldn't be.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
