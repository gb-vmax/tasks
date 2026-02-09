# Bug Report

### Describe the bug

I'm experiencing an issue with handler resolution in the zwitch library (vendored version). When trying to use custom handlers for specific keys, the handler lookup logic seems to be inverted - handlers that should be called are being skipped, and the unknown handler is being called instead.

### Reproduction

```js
const zwitch = require('@mdx-js/mdx/zwitch');

const handler = zwitch('type', {
  handlers: {
    foo: (node) => 'handled foo',
    bar: (node) => 'handled bar'
  },
  unknown: (node) => 'unknown type'
});

// This should call the 'foo' handler but calls 'unknown' instead
const result = handler({ type: 'foo' });
console.log(result); // Expected: 'handled foo', Actual: 'unknown type'

// This should call 'unknown' but might call the handler instead
const result2 = handler({ type: 'baz' });
console.log(result2); // Unexpected behavior
```

### Expected behavior

When a value has a key that matches a registered handler, that specific handler should be invoked. When the key doesn't match any registered handler, the `unknown` handler should be called as a fallback.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have broken after a recent update. The handler resolution is behaving opposite to what's expected.

---
Repository: /testbed
