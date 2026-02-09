# Bug Report

### Describe the bug

I'm encountering unexpected behavior with logical expressions (`&&` and `||`) in my code. It seems like the tree-shaking/optimization is incorrectly determining which branch of a logical expression should be used or retained.

### Reproduction

When I have code like this:

```js
const result = someCondition || fallbackValue;
```

or

```js
const result = someCondition && computedValue;
```

The bundler appears to be making incorrect decisions about which branch can be eliminated. In some cases, it's keeping the wrong branch or eliminating code that should be retained.

For example:
```js
// Case 1: OR operator
const value = false || 'default';
// Expected: 'default'
// Getting unexpected behavior

// Case 2: AND operator  
const value = true && 'result';
// Expected: 'result'
// Getting unexpected behavior
```

### Expected behavior

The logical expression should correctly evaluate which branch will be used at runtime and optimize accordingly. When the left operand of `||` is falsy, the right branch should be used. When the left operand of `&&` is truthy, the right branch should be used.

### System Info
- Using latest version from main branch
- Node.js v18

This seems like it might be related to the branch resolution analysis logic. The wrong branches are being selected during the optimization phase.

---
Repository: /testbed
