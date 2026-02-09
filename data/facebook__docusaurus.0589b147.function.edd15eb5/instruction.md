# Bug Report

### Describe the bug

The table of contents (TOC) filtering is not including headings at the minimum heading level. When setting `minHeadingLevel`, headings at exactly that level are being excluded from the TOC instead of being included.

### Reproduction

```js
const toc = [
  { level: 2, value: 'Heading 2', id: 'h2' },
  { level: 3, value: 'Heading 3', id: 'h3' },
  { level: 4, value: 'Heading 4', id: 'h4' }
]

const filtered = filterTOC({
  toc,
  minHeadingLevel: 2,
  maxHeadingLevel: 4
})

// Expected: All three headings should be included
// Actual: Only h3 and h4 are included, h2 is missing
```

### Expected behavior

When `minHeadingLevel` is set to 2, headings at level 2 should be included in the filtered TOC. The filtering should be inclusive of both the minimum and maximum heading levels.

For example:
- `minHeadingLevel: 2` and `maxHeadingLevel: 4` should include h2, h3, and h4
- `minHeadingLevel: 3` and `maxHeadingLevel: 3` should include only h3

Currently it seems like the minimum level is being treated as exclusive rather than inclusive.

---
Repository: /testbed
