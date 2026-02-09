# Bug Report

### Describe the bug

I'm experiencing an issue with the zwitch handler function where it's not calling the appropriate handlers when a matching key is found. The function seems to be inverting the logic - it only executes handlers when they're NOT found, which is the opposite of what should happen.

### Reproduction

```js
const handler = zwitch('type', {
  handlers: {
    foo: (value) => console.log('Handling foo:', value),
    bar: (value) => console.log('Handling bar:', value)
  },
  invalid: () => console.log('Invalid value'),
  unknown: () => console.log('Unknown type')
})

// This should call the 'foo' handler but nothing happens
handler({ type: 'foo', data: 'test' })

// This should call the 'bar' handler but nothing happens either
handler({ type: 'bar', data: 'test' })
```

### Expected behavior

When calling the handler with an object that has a matching type in the handlers object, the corresponding handler function should be executed. Instead, it appears that valid handlers are being skipped entirely.

The handlers should be invoked when their keys match, not when they don't match.

### System Info
- Version: Using @mdx-js/mdx@3.0.0
- Node: v18.x

---
Repository: /testbed
