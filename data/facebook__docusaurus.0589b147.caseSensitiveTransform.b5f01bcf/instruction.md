# Bug Report

### Describe the bug

I'm encountering an issue with HTML attribute handling where certain attributes are not being properly recognized or transformed. It seems like the attribute lookup mechanism is broken - attributes that should be found in the attributes mapping are being ignored.

### Reproduction

```js
const attributes = {
  'className': 'class',
  'htmlFor': 'for'
}

// Trying to transform 'className' attribute
// Expected: should return 'class' (the mapped value)
// Actual: returns 'className' (the original attribute)
```

When processing HTML elements with attributes that have special mappings (like `className` -> `class`), the transformation doesn't work correctly. The function appears to always return the original attribute name instead of checking if a mapping exists and returning the mapped value.

### Expected behavior

When an attribute exists in the attributes mapping object, it should return the transformed/mapped attribute name. For example, `className` should be transformed to `class`, and `htmlFor` should be transformed to `for`.

### System Info
- rehype-stringify version: 10.0.0
- Node version: Latest

---
Repository: /testbed
