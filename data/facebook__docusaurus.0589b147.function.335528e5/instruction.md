# Bug Report

### Describe the bug

The table of contents filtering is not working as expected. When setting `minHeadingLevel` and `maxHeadingLevel` options, headings that should be filtered out are still appearing in the TOC.

### Reproduction

```js
const toc = [
  { level: 1, value: 'Heading 1' },
  { level: 2, value: 'Heading 2' },
  { level: 3, value: 'Heading 3' },
  { level: 4, value: 'Heading 4' },
];

// Configure to only show h2 and h3
const filtered = filterTOC({
  toc,
  minHeadingLevel: 2,
  maxHeadingLevel: 3
});

// Expected: Only level 2 and 3 headings
// Actual: All headings are included
```

### Expected behavior

Only headings between the specified min and max levels (inclusive) should appear in the filtered TOC. In the example above, only h2 and h3 headings should be included, but h1 and h4 are also showing up.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
