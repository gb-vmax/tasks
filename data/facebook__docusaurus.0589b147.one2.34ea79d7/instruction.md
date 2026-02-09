# Bug Report

### Describe the bug

I'm experiencing an issue with the zwitch function where it seems to be calling handlers even when they don't exist. The function appears to have inverted logic that causes it to skip execution when a handler is found, but attempts to call it when no handler exists.

### Reproduction

```js
const dispatch = zwitch('type', {
  handlers: {
    'foo': (node) => console.log('Handling foo:', node)
  },
  unknown: (node) => console.log('Unknown type:', node)
})

// This should call the 'foo' handler but doesn't do anything
dispatch({ type: 'foo', value: 'test' })

// This should call the unknown handler but throws an error
dispatch({ type: 'bar', value: 'test' })
```

### Expected behavior

When a matching handler exists in `handlers`, it should be called with the provided value and parameters. When no matching handler exists, the `unknown` handler should be called if defined. The function shouldn't attempt to call undefined handlers.

### Additional context

This appears to be affecting MDX processing where different node types need to be dispatched to their respective handlers. The current behavior causes handlers to not execute when they should, and attempts to execute when handlers are undefined, leading to runtime errors.

---
Repository: /testbed
