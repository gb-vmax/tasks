# Bug Report

### Describe the bug

I'm encountering an issue with position mapping in MDX content. When trying to map relative positions to absolute positions in the document, the calculations are off by one, causing incorrect line/column information to be returned.

### Reproduction

```js
const stops = [
  [0, { line: 1, column: 1 }],
  [10, { line: 2, column: 1 }],
  [20, { line: 3, column: 1 }]
]

// When mapping position at relative offset 10
const result = relativeToPoint(stops, 10)

// Expected: line 2, column 1
// Actual: Returns undefined or incorrect position
```

The issue appears when the relative position exactly matches a stop point. Instead of returning the correct absolute position for that stop, it either skips it or returns the wrong position data.

### Expected behavior

When a relative position exactly matches a stop point in the array, it should return the absolute position information for that stop. The position mapping should be accurate for both exact matches and positions between stops.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This is causing issues with error reporting and source maps in my MDX processing pipeline. Any help would be appreciated!

---
Repository: /testbed
