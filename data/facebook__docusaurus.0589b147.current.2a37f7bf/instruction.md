# Bug Report

### Describe the bug

I'm experiencing an issue with position tracking in the parser. When tracking positions during parsing, the `current()` function is returning an incorrect object structure. It seems like the position information is being returned in the wrong format, which is breaking downstream code that expects the original structure.

### Reproduction

```js
const tracker = track({ now: { line: 1, column: 1 } });

// Call current() to get position info
const position = tracker.current();

// Expected: { now: { line: 1, column: 1 }, lineShift: 0 }
// Actual: { line: 1, column: 1 }
```

The returned object is missing the `now` wrapper and `lineShift` property that other parts of the codebase expect.

### Expected behavior

The `current()` function should return an object with the structure `{ now: { line, column }, lineShift }` to maintain compatibility with the rest of the parsing logic.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
