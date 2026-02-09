# Bug Report

### Describe the bug

I'm encountering an issue with attribute transformation in the MDX parser. When processing attributes, the case-sensitive transform function appears to be returning incorrect values. Instead of looking up the proper attribute name from the attributes mapping, it seems to be returning the wrong value.

### Reproduction

```js
const attributes = {
  'className': 'class',
  'htmlFor': 'for'
}

// Expected: should return 'class' (the mapped value)
// Actual: returns 'className' (the key itself)
const result = caseSensitiveTransform(attributes, 'className')
console.log(result) // outputs 'className' instead of 'class'
```

This affects how JSX attributes are transformed when parsing MDX content. The function should look up the attribute in the mapping and return the corresponding value, but it's doing the opposite.

### Expected behavior

When an attribute exists in the mapping, the function should return the mapped value (e.g., `'className'` should map to `'class'`). When it doesn't exist in the mapping, it should return the original attribute name.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
