# Bug Report

### Describe the bug

I'm encountering an issue with conditional (ternary) expressions where the consequent and alternate branches appear to be swapped in the generated output. When using the ternary operator `condition ? valueIfTrue : valueIfFalse`, the output seems to have the true and false values reversed.

### Reproduction

```js
// Input expression
const result = isActive ? 'active' : 'inactive';

// Expected output: 'active' when isActive is true
// Actual output: 'inactive' when isActive is true
```

Another example:
```js
const value = x > 10 ? 'greater' : 'less or equal';

// When x = 15:
// Expected: 'greater'
// Actual: 'less or equal'
```

### Expected behavior

The ternary operator should evaluate correctly with the consequent (true branch) returned when the test condition is true, and the alternate (false branch) returned when the condition is false.

Currently it seems like the branches are reversed - the alternate is being used when the condition is true and vice versa.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
