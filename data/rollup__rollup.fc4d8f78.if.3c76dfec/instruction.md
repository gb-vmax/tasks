# Bug Report

### Describe the bug

I'm encountering an issue with `export * from` statements when there's a module with synthetic named exports. It seems like exports are being incorrectly filtered or skipped during the resolution process.

### Reproduction

```js
// moduleA.js - has syntheticNamedExports
export const syntheticNamedExports = 'foo';
export const foo = 'value from A';

// moduleB.js
export const foo = 'value from B';

// entry.js
export * from './moduleA.js';
export * from './moduleB.js';
```

When trying to import `foo` from the entry module, the expected export is not being resolved correctly. The synthetic named exports logic appears to be interfering with normal export resolution.

### Expected behavior

The `foo` export should be properly resolved from the re-exported modules. Synthetic named exports should only affect their intended behavior and not interfere with regular named exports of the same name.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
