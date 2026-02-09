# Bug Report

### Describe the bug

I'm experiencing an issue with variable declarations in MDX files. When declaring multiple variables in a single statement (using comma separation), only the first variable is being parsed correctly. The remaining variables in the declaration list are being ignored.

### Reproduction

```js
// This should declare three variables
let a = 1, b = 2, c = 3;

// Only 'a' is recognized, 'b' and 'c' are undefined
console.log(a); // works
console.log(b); // undefined
console.log(c); // undefined
```

Also seeing issues with destructuring patterns that should require initialization:

```js
// This should throw an error but doesn't
let { x, y };

// Meanwhile, simple identifier declarations incorrectly throw errors
let z; // throws "Complex binding patterns require an initialization value"
```

### Expected behavior

- Multiple variable declarations separated by commas should all be parsed and available
- Destructuring patterns without initialization should raise an error
- Simple identifier declarations without initialization should be allowed (unless it's a const)

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have broken basic JavaScript parsing behavior. Any help would be appreciated!

---
Repository: /testbed
