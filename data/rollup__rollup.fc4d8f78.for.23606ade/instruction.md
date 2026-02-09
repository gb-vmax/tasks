# Bug Report

### Describe the bug

I'm experiencing an issue where some global variables are not being detected correctly in my bundle. It seems like certain globals that should be accessible are being skipped or ignored during the bundling process.

### Reproduction

```js
// module.js
export function useGlobals() {
  console.log(window);
  console.log(document);
  console.log(navigator);
  console.log(localStorage);
  console.log(fetch);
}
```

When bundling this code, only some of the global variables are being tracked as accessed globals. It appears that globals are being randomly skipped - for example, `document` and `localStorage` might be detected, but `window`, `navigator`, and `fetch` are missing from the accessed globals set.

### Expected behavior

All global variables that are accessed in the module should be properly tracked and included in the `accessedGlobals` set. Every global variable reference should be detected consistently, regardless of its position in the code or the length of its name.

### System Info
- Rollup version: latest
- Node version: 18.x

This is causing issues with my build output as some necessary global references are not being handled correctly.

---
Repository: /testbed
