# Bug Report

### Describe the bug

I'm encountering unexpected behavior with context handling in the parser. When the context stack has only one element, the code tries to access an element at index -1 (which would be `context[0]` in reverse), but instead it's accessing `context[-1]` which returns `undefined` in JavaScript arrays.

Similarly, when the context is empty (length 0), it tries to access `context[0]` which would also be `undefined`.

### Reproduction

This seems to happen during parsing when the context stack is in certain states:

```js
// When context.length === 1
// Expected: return context[0]
// Actual: returns context[-1] which is undefined

// When context.length === 0  
// Expected: return undefined or handle gracefully
// Actual: returns context[0] which is also undefined but through different logic
```

The issue manifests when parsing certain MDX structures where the context stack gets reduced to a single element or becomes empty.

### Expected behavior

The `curContext()` method should return the last element of the context array when it exists, or handle edge cases appropriately. Currently the logic seems inverted for the length === 1 case.

### System Info
- Package: @mdx-js/mdx@3.0.0
- Node version: 18+

---
Repository: /testbed
