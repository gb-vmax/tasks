# Bug Report

### Describe the bug

I'm encountering an issue where the `zwitch` function is not correctly detecting handlers for values. It seems like the handler lookup is checking the wrong object for the presence of the key property.

### Reproduction

```js
const handler = zwitch('type', {
  handlers: {
    foo: () => 'handled foo',
    bar: () => 'handled bar'
  }
})

const value = { type: 'foo', data: 'test' }

// This should call the 'foo' handler but doesn't work correctly
handler(value)
```

### Expected behavior

The function should check if the value has the specified key property before attempting to look up the handler. Currently it appears to be checking the handlers object instead of the value object, which causes incorrect behavior when processing values.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
