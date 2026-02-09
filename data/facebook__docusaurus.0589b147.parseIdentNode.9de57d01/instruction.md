# Bug Report

### Describe the bug

I'm encountering an issue with parsing JavaScript identifiers in MDX files. When using keywords like `class` or `function` as property names (e.g., `obj.class` or `obj.function`), the parser seems to be handling them incorrectly. The context stack isn't being managed properly in these cases.

### Reproduction

```js
// This should work but causes parsing issues
const obj = {
  class: 'my-class',
  function: 'my-function'
}

// Accessing properties with keyword names
console.log(obj.class)
console.log(obj.function)
```

When parsing MDX content that includes property access using reserved keywords as property names (with dot notation), the parser appears to be popping the context incorrectly.

### Expected behavior

The parser should correctly handle reserved keywords when they're used as property names in member expressions (e.g., `object.class` or `object.function`). These are valid JavaScript and should parse without issues.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest LTS

---
Repository: /testbed
