# Bug Report

### Describe the bug

I'm encountering an issue with plugin hooks where the `this` context is not being preserved correctly when hooks are executed. After some debugging, I noticed that plugin methods that rely on accessing their own instance properties via `this` are failing because the context is being bound to the wrong object.

### Reproduction

```js
const myPlugin = {
  name: 'my-plugin',
  internalState: { count: 0 },
  
  buildStart() {
    // This should access the plugin's own internalState
    this.internalState.count++;
    console.log(this.internalState.count);
  }
}

// When the plugin hook is called, `this` doesn't point to myPlugin anymore
// Expected: this.internalState is accessible
// Actual: this.internalState is undefined or points to wrong object
```

### Expected behavior

Plugin hooks should maintain the correct `this` context and be able to access their own instance properties and methods. The `this` keyword inside a hook should refer to the plugin object itself.

### Additional context

This seems to have started happening recently. I have several plugins that store internal state and rely on `this` to access that state within their hooks. They all stopped working at the same time.

---
Repository: /testbed
