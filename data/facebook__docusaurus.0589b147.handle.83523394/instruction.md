# Bug Report

### Describe the bug

After a recent update, the `handle` function in the MDX state handler is returning an unexpected object structure instead of the direct value. This is breaking MDX compilation for components that rely on the handler's return value.

### Reproduction

```js
// When processing MDX nodes, the handle function now returns:
// { value: <result>, context: <context> }
// instead of just <result>

const state = createState2(options);
const result = state.handle(node);

// Before: result would be the processed node value
// Now: result is an object with 'value' and 'context' properties
console.log(result); // Outputs: { value: ..., context: ... }
```

### Expected behavior

The `handle` function should return the processed node value directly, not wrapped in an object. The return value should be whatever `one2(node2, context)` produces.

### Additional context

This appears to have changed the API contract of the handle function. Code expecting a direct return value now receives an object wrapper instead, which breaks downstream processing.

---
Repository: /testbed
