# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the position information for collected tokens appears to be incorrect. When processing events and collecting token values, the end positions seem to be pointing to the wrong location in the source text.

### Reproduction

```js
// When collecting events with specific token types
const events = [
  ['enter', { type: 'someToken', start: { line: 1, column: 1 }, end: { line: 1, column: 10 } }],
  ['exit', { type: 'someToken', start: { line: 1, column: 1 }, end: { line: 1, column: 10 } }]
];

const result = collect(events, ['someToken']);

// The stops array contains position markers
// Expected: stops should have [start_pos, end_pos] pairs
// Actual: both positions in the pair point to the same location
```

### Expected behavior

The `stops` array should contain proper start and end position pairs for each collected token segment. The second element in each stop pair should reference the end position of the token, not the start position.

### Additional context

This affects any code that relies on accurate position tracking in the MDX parser, particularly when trying to map parsed content back to source locations for error reporting or source maps.

---
Repository: /testbed
