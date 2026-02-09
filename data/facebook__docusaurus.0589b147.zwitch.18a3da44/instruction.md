# Bug Report

### Issue with handler function lookup in zwitch

I'm experiencing an issue where the zwitch dispatcher is incorrectly checking for handler existence. When trying to process values with specific types, the function lookup logic seems to be broken.

### Reproduction

```js
const dispatcher = zwitch('type', {
  handlers: {
    foo: function foo(value) {
      return 'handled foo'
    },
    bar: function bar(value) {
      return 'handled bar'
    }
  },
  unknown: function(value) {
    return 'unknown type'
  }
})

// This doesn't work as expected
const result = dispatcher({ type: 'foo', data: 'test' })
// Expected: 'handled foo'
// Actual: Error or unexpected behavior
```

### Expected behavior

The dispatcher should look up the handler based on the value's type property and execute the corresponding handler function. When a handler exists for the given type, it should be called properly.

### Additional context

This seems to be related to how the function checks whether a handler exists. The current implementation appears to be checking the wrong object when verifying if a handler is available, which causes valid handlers to not be found or executed.

---
Repository: /testbed
