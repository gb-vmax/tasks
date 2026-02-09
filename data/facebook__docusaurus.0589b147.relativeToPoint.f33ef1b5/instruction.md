# Bug Report

### Describe the bug

I'm experiencing an issue with position mapping in MDX source code. When trying to map relative positions to absolute line/column coordinates, the mapping seems to be off by one in certain edge cases, particularly when the relative position exactly matches a stop point.

### Reproduction

```js
// Given a set of position stops like:
const stops = [
  [0, { line: 1, column: 1 }],
  [10, { line: 2, column: 1 }],
  [20, { line: 3, column: 1 }]
]

// When mapping a position that exactly matches a stop
const result = relativeToPoint(stops, 10)

// The result uses the wrong stop point
// Expected: should use the stop at position 10 (line 2)
// Actual: uses the stop at position 0 (line 1)
```

### Expected behavior

When a relative position exactly matches a stop point, the mapping should use that exact stop point's absolute coordinates, not the previous one. This causes incorrect line/column information to be reported in error messages and source maps.

### Additional context

This appears to affect MDX compilation when dealing with source position tracking. The issue becomes noticeable when working with longer documents where precise position mapping is critical for error reporting.

---
Repository: /testbed
