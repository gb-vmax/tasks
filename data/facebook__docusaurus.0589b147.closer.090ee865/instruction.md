# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown parser where callback functions passed to the `closer` function are not being invoked properly. It seems like the callback is being referenced but never actually called, which breaks the expected behavior of custom exit handlers.

### Reproduction

```js
const processor = remark();

// Register a custom handler with a callback
processor.use(function() {
  this.Parser.prototype.blockTokenizers.custom = function(eat, value) {
    // ... tokenization logic
  };
  
  // The callback passed here should be invoked on exit
  const exitHandler = function(token) {
    console.log('Exit handler called');
    // Custom cleanup logic
  };
  
  // This should call both the exitHandler AND the default exit logic
  const closeFunc = closer(exitHandler);
  closeFunc(token);
});
```

When the close function is called, the custom exit handler is never executed. The token is processed but any custom logic in the callback is skipped.

### Expected behavior

The callback function passed to `closer()` should be invoked with the token as an argument before calling the default `exit2` function. This allows for custom cleanup or processing logic during the exit phase.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
