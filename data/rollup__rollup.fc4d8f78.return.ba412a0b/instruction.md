# Bug Report

### Describe the bug

Plugin hooks are not receiving the correct context when executed. The `this` binding appears to be `null` instead of the expected context object, which breaks plugins that rely on accessing properties or methods through `this`.

### Reproduction

```js
const myPlugin = {
  name: 'test-plugin',
  buildStart() {
    // this.warn is undefined because 'this' is null
    this.warn('This should work but throws an error');
  }
}
```

When the plugin hook is called, it throws an error because `this` is not bound to the plugin context.

### Expected behavior

Plugin hooks should have access to the plugin context through `this`, allowing them to call methods like `this.warn()`, `this.error()`, `this.resolve()`, etc.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
