# Bug Report

### Describe the bug

I'm experiencing issues with object destructuring patterns when parsing MDX files. It seems like shorthand property assignments with default values are not being handled correctly in destructuring contexts.

### Reproduction

```js
// This pattern fails to parse correctly
const { prop = defaultValue } = obj;

// Also affects nested destructuring
function example({ nested: { value = 'default' } }) {
  // ...
}
```

When using destructuring patterns with default values, the parser appears to be treating them incorrectly. The shorthand assignment detection logic seems inverted - it's triggering when it shouldn't and not triggering when it should.

### Expected behavior

Object destructuring with default values should parse correctly:
- `{ prop = value }` should be recognized as a valid destructuring pattern with a default
- Nested destructuring patterns should work properly
- The parser should correctly distinguish between destructuring patterns and regular object literals

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This is blocking our ability to use default parameters in destructured function arguments within MDX components. Any help would be appreciated!

---
Repository: /testbed
