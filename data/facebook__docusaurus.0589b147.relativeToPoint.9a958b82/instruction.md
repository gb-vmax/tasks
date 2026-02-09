# Bug Report

### Describe the bug

I'm experiencing an issue with source position mapping in MDX files. When trying to get the position of a token relative to a point in the document, the calculated column positions are incorrect. Instead of getting the correct column offset, I'm getting negative or reversed offsets.

### Reproduction

```js
// Given a document with multiple lines and position stops
const stops = [
  [0, { line: 1, column: 0 }],
  [10, { line: 1, column: 10 }],
  [20, { line: 2, column: 0 }]
];

// When trying to find the position at relative offset 15
const position = relativeToPoint(stops, 15);

// Expected: { line: 1, column: 15 }
// Actual: column value is incorrect (negative offset)
```

The issue seems to affect how positions are calculated when mapping between relative offsets and absolute line/column positions. This impacts error reporting and source maps in MDX documents.

### Expected behavior

The function should correctly calculate the column position by adding the remaining offset to the base column of the stop point. For a relative position between two stops, it should return the correct line and column coordinates.

### System Info

- MDX version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
