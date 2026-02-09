# Bug Report

### Describe the bug

I'm encountering an issue with the zwitch handler selection logic. When trying to use custom handlers, the wrong handler is being invoked - it seems like the handler lookup is reversed. Instead of calling my registered handler for a specific key, it's falling back to the `unknown` handler, and vice versa.

### Reproduction

```js
const dispatch = zwitch('type', {
  handlers: {
    foo: (node) => 'handled foo',
    bar: (node) => 'handled bar'
  },
  unknown: (node) => 'unknown handler'
})

// This calls the unknown handler instead of the foo handler
const result = dispatch({type: 'foo'})
console.log(result) // Expected: 'handled foo', Actual: 'unknown handler'

// And this tries to call a non-existent handler instead of unknown
const result2 = dispatch({type: 'baz'})
// This throws an error or behaves unexpectedly
```

### Expected behavior

When a node has a `type` property that matches a registered handler key (like 'foo' or 'bar'), that specific handler should be called. When the type doesn't match any registered handler (like 'baz'), the `unknown` handler should be called as a fallback.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
