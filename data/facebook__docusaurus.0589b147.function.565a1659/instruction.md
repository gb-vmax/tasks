# Bug Report

### Describe the bug

The table of contents (TOC) filtering is showing the wrong heading levels. When I set `minHeadingLevel` and `maxHeadingLevel`, the TOC displays headings that are outside the specified range instead of within it.

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
  maxHeadingLevel: 3
});

// Expected: Shows only level 2 and 3 headings
// Actual: Shows only level 4 heading (levels outside the range)
```

### Expected behavior

When I configure `minHeadingLevel: 2` and `maxHeadingLevel: 3`, the TOC should display only headings at levels 2 and 3. Currently, it's doing the opposite - showing headings that fall outside the specified range.

### System Info

- Docusaurus version: latest
- Node version: 18.x

This seems like the filtering logic might be inverted somehow. The TOC is filtering out the headings I want to keep and keeping the ones I want to filter out.

---
Repository: /testbed
