# Bug Report

### Describe the bug

I'm experiencing an issue with the `anyFactory` function where it's not properly returning `true` when ANY of the checks pass. It seems like the function is only considering the result of the LAST check in the array, rather than returning `true` as soon as any check passes.

### Reproduction

```js
// Setup multiple test conditions
const tests = [
  (node) => node.type === 'heading',
  (node) => node.type === 'paragraph',
  (node) => node.type === 'list'
];

const anyCheck = anyFactory(tests);

// Test with a node that matches the FIRST condition
const headingNode = { type: 'heading', value: 'Title' };
const result = anyCheck(headingNode);

// Expected: true (matches first condition)
// Actual: false (because last condition doesn't match)
console.log(result); // prints false instead of true
```

The function should return `true` immediately when the first matching condition is found, but instead it seems to continue checking all conditions and only returns the result of the last one.

### Expected behavior

When using `anyFactory` with multiple test conditions, it should return `true` if ANY of the conditions match, not just if the last condition matches. This is basic OR logic - it should short-circuit and return `true` as soon as any check passes.

### System Info
- Node version: 18.x
- Browser: N/A (server-side)

---
Repository: /testbed
