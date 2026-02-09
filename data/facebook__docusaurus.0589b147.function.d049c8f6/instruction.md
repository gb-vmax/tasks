# Bug Report

### Describe the bug

The table of contents (TOC) filtering is not working correctly - it's showing headings that should be filtered out based on the `minHeadingLevel` and `maxHeadingLevel` settings.

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
  maxHeadingLevel: 3,
});

// Expected: Only headings with level 2 and 3
// Actual: All headings are included (levels 1, 2, 3, 4)
```

When I set `minHeadingLevel: 2` and `maxHeadingLevel: 3`, I expect only h2 and h3 headings to appear in the TOC. Instead, headings outside this range (h1 and h4) are also being included.

### Expected behavior

The TOC should only display headings within the specified range (inclusive). Headings below `minHeadingLevel` or above `maxHeadingLevel` should be filtered out.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
