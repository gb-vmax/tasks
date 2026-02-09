# Bug Report

### Describe the bug

I'm experiencing an issue with dynamic imports where accessing properties on the imported module results in incorrect tree-shaking behavior. It seems like the logic for tracking which properties are accessed is inverted - properties that should be marked as "unknown" are being tracked specifically, and vice versa.

### Reproduction

```js
// module.js
export const foo = 'foo';
export const bar = 'bar';

// main.js
import('./module.js').then(mod => {
  console.log(mod.foo);
});
```

When bundling this code, the behavior is backwards from what I'd expect. Properties that are explicitly accessed seem to trigger the "unknown key" flag, while accessing with an actual unknown key doesn't.

### Expected behavior

When accessing a specific property like `mod.foo`, only that property should be tracked in `accessedPropKey`. The `hasUnknownAccessedKey` flag should only be set when we truly don't know which property is being accessed (e.g., dynamic property access with a variable).

Currently it seems like the condition is reversed - `UnknownKey` is causing `hasUnknownAccessedKey` to be set to true, when it should be the opposite.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
