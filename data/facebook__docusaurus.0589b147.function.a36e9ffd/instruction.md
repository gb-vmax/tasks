# Bug Report

### Describe the bug

The table of contents (TOC) filtering is not working correctly. When setting `minHeadingLevel` and `maxHeadingLevel`, headings that should be displayed are being filtered out, and headings outside the specified range are being included instead.

### Reproduction

```js
const toc = [
  { level: 2, value: 'Heading 2' },
  { level: 3, value: 'Heading 3' },
  { level: 4, value: 'Heading 4' },
];

const filtered = filterTOC({
  toc,
  minHeadingLevel: 2,
  maxHeadingLevel: 3,
});

// Expected: Heading 2 and Heading 3 to be included
// Actual: Wrong headings are included/excluded
```

### Expected behavior

When `minHeadingLevel` is set to 2 and `maxHeadingLevel` is set to 3, only headings with level 2 and 3 should be included in the filtered TOC. Currently, the filtering logic appears to be inverted or incorrect, causing the wrong headings to be shown.

### System Info

- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
