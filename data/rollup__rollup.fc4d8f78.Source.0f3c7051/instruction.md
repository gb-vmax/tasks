# Bug Report

### Describe the bug

I'm experiencing an issue with sourcemap generation where the line and column numbers appear to be swapped in the traced segments. When I try to trace back to the original source location, the coordinates are incorrect - what should be the line number is showing up as the column and vice versa.

### Reproduction

```js
const source = new Source(content, 'example.js');
const segment = source.traceSegment(10, 5, 'myFunction');

// segment.line is 5 (should be 10)
// segment.column is 10 (should be 5)
```

When tracing a segment at line 10, column 5, the resulting segment object has these values reversed. This causes sourcemap lookups to point to the wrong location in the original source file.

### Expected behavior

The `traceSegment` method should return a segment object with the correct line and column values matching the input parameters. Line should map to line, and column should map to column.

### Additional context

This is breaking sourcemap-based debugging as the browser dev tools jump to incorrect locations when trying to view the original source. The coordinates seem to be consistently swapped for all traced segments.

---
Repository: /testbed
