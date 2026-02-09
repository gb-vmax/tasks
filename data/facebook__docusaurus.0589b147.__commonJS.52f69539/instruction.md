# Bug Report

### Describe the bug

I'm experiencing an issue with module loading where CommonJS modules are being re-initialized on every require call instead of returning the cached exports. This causes modules to execute their initialization code multiple times, which breaks singleton patterns and causes unexpected behavior.

### Reproduction

```js
// myModule.js
console.log('Module initialized');
let counter = 0;

module.exports = {
  increment() {
    return ++counter;
  },
  getCount() {
    return counter;
  }
};

// main.js
const mod1 = require('./myModule');
const mod2 = require('./myModule');

console.log(mod1.increment()); // Expected: 1
console.log(mod2.getCount());  // Expected: 1, but getting 0
```

The module initialization log appears twice, and the counter state is not shared between the two require calls.

### Expected behavior

CommonJS modules should be cached after the first require, so subsequent require calls return the same module.exports object without re-executing the module code. The counter should be shared across all require calls to the same module.

### System Info
- Node version: 18.x
- Build system: Custom bundler with CommonJS support

---
Repository: /testbed
