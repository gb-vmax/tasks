# Bug Report

### Describe the bug

I'm experiencing an issue with nested object property access in the rehype-stringify handler logic. When working with objects that have handler functions, the code appears to be accessing the wrong property which causes unexpected behavior or errors.

### Reproduction

```js
const obj = {
  type: 'element',
  tagName: 'div',
  element: function() { /* handler function */ }
}

// When processing this object, instead of calling the registered handler
// for 'element' type, it tries to call obj['element'] directly
// This leads to incorrect function being invoked
```

The issue seems to be related to how the handler lookup works - it's using the wrong object property to retrieve the handler function.

### Expected behavior

The system should look up handlers from the registered handlers object, not from the value object itself. When a handler is registered for a specific type, it should be retrieved from the handlers registry, not from the input value's properties.

### System Info
- rehype-stringify version: 10.0.0
- Node version: Latest

---
Repository: /testbed
