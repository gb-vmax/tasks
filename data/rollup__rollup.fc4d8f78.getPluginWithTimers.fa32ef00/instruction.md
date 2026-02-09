# Bug Report

### Describe the bug

I'm encountering an issue with plugin hooks that have a `handler` property. When a plugin defines a hook with an object containing a `handler` function (instead of just a plain function), the hook doesn't execute correctly. It seems like the wrong function reference is being used.

### Reproduction

```js
const myPlugin = {
  name: 'test-plugin',
  buildStart: {
    handler: function() {
      console.log('This should run');
    },
    order: 'pre'
  }
};

// Use the plugin in rollup config
// The handler function doesn't get called properly
```

### Expected behavior

When a plugin hook is defined as an object with a `handler` property, the actual handler function should be invoked correctly. Both formats should work:
- `hookName: function() {}` (plain function)
- `hookName: { handler: function() {}, order: 'pre' }` (object with handler)

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
