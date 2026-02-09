# Bug Report

### Describe the bug

After a recent update, dynamic imports appear to be broken and causing syntax errors. The code that was working fine before now fails to parse or compile.

### Reproduction

```js
// This used to work but now throws an error
const module = await import('./my-module.js');

// Also fails with .then() syntax
import('./another-module.js').then(mod => {
  console.log(mod);
});

// Even destructuring doesn't work anymore
const { foo, bar } = await import('./utils.js');
```

### Expected behavior

Dynamic imports should work as they did previously. The syntax is valid JavaScript and should be properly handled by the bundler.

### Additional context

This seems to have started happening after the latest update. All forms of dynamic imports are affected - whether using await, .then(), destructuring, or just side-effect imports. The build process fails before even getting to runtime.

---
Repository: /testbed
