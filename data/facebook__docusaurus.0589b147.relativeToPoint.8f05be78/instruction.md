# Bug Report

### Describe the bug

I'm experiencing an issue with position/offset calculations in MDX parsing. When working with source positions, the calculated offsets appear to be incorrect for certain cases, particularly when dealing with positions that fall exactly on a stop boundary.

### Reproduction

```js
// When converting relative positions to points
const stops = [
  [0, { line: 1, column: 1, offset: 0 }],
  [10, { line: 2, column: 1, offset: 10 }],
  [20, { line: 3, column: 1, offset: 20 }]
];

// Converting a position that's exactly at a stop boundary
const result = relativeToPoint(stops, 10);

// The offset calculation seems off - getting unexpected values
console.log(result.offset); // Expected: 10, but getting wrong value
```

### Expected behavior

When converting relative positions to absolute points, the offset should be calculated correctly based on the stop position plus the remaining distance. Positions that fall exactly on stop boundaries should use that stop as the reference point.

### Additional context

This seems to affect source map accuracy and error reporting in MDX files. The line and column numbers might also be impacted when positions align with newlines or other structural boundaries.

---
Repository: /testbed
