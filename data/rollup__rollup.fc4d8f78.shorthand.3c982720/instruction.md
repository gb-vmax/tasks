# Bug Report

### Describe the bug

I'm experiencing an issue with object destructuring and shorthand property detection. When using shorthand properties in object literals, the code seems to be treating them incorrectly - properties that should be recognized as shorthand are not being detected as such, and vice versa.

### Reproduction

```js
const name = 'John';
const age = 30;

// Using shorthand property syntax
const person = { name, age };

// The shorthand properties are not being recognized correctly
// Expected: both properties should be identified as shorthand
// Actual: behavior is inverted
```

Another case:

```js
// Regular property (not shorthand)
const obj = { name: 'John' };

// This is incorrectly being treated as shorthand when it's not
```

### Expected behavior

Shorthand properties (like `{ name }` where the key and value variable have the same name) should be correctly identified as shorthand. Regular properties with explicit values (like `{ name: 'John' }`) should not be identified as shorthand.

The detection logic seems to be inverted - shorthand properties are being flagged as non-shorthand and regular properties are being flagged as shorthand.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
