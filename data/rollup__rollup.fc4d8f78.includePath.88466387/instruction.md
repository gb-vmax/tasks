# Bug Report

### Describe the bug

I'm encountering an issue with dynamic imports where the module isn't being properly included in the bundle when accessing properties on the imported module. It seems like the tree-shaking logic is incorrectly removing code that should be included.

### Reproduction

```js
// moduleA.js
export const foo = 'foo';
export const bar = 'bar';

// main.js
async function loadModule() {
  const module = await import('./moduleA.js');
  console.log(module.foo);
}
```

When I build this, the dynamic import doesn't seem to be getting included properly. The bundle is missing the necessary code even though I'm clearly accessing a property from the imported module.

### Expected behavior

The dynamic import should be included in the bundle and all accessed properties should be available at runtime. The tree-shaking should recognize that we're accessing `module.foo` and include the necessary exports.

### Additional context

This appears to have started happening recently. Previously, dynamic imports were working correctly and the bundle would include the imported modules as expected.

---
Repository: /testbed
