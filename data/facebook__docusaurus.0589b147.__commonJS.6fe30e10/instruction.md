# Bug Report

### Describe the bug

After a recent update, the CommonJS module loading system seems to be broken. When trying to load modules, I'm getting errors about undefined exports or modules not being initialized properly.

### Reproduction

```js
// When requiring a CommonJS module
const module = require('./some-module');

// The module.exports is undefined or not properly initialized
console.log(module); // undefined or incorrect value
```

This appears to affect all CommonJS modules being loaded through the `__commonJS` helper function. The modules aren't being initialized correctly before their exports are returned.

### Expected behavior

The module should be properly initialized on first require, with `mod.exports` being populated by the callback function before being returned to the caller.

### System Info
- Node version: 18.x
- remark version: 15.0.1

---
Repository: /testbed
