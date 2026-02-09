# Bug Report

### Describe the bug
I'm experiencing issues with object destructuring patterns when using shorthand properties with default values. The parser seems to be handling the assignment incorrectly, causing unexpected behavior in certain edge cases.

### Reproduction
```js
// This pattern doesn't work as expected
const { prop = defaultValue } = obj;

// Also having issues with nested destructuring
const { 
  user: { 
    name = 'default' 
  } = {} 
} = data;
```

When using shorthand property assignments in destructuring patterns, the parser appears to be mixing up when to parse default values vs regular assignments. This affects both simple and nested destructuring scenarios.

### Expected behavior
Object destructuring with shorthand properties and default values should parse correctly and handle all edge cases properly. The parser should distinguish between pattern contexts and regular assignment contexts.

### System Info
- Version: 3.0.0
- Node: v18.x

This seems related to how the parser handles the `isPattern` flag when processing property values. Any guidance would be appreciated!

---
Repository: /testbed
