# Bug Report

### Describe the bug

I'm experiencing an issue where exports are not being included properly in the bundle. When I have a module that should include all its exports, they're not appearing in the final output.

### Reproduction

```js
// module.js
export const foo = 'foo';
export const bar = 'bar';
export const baz = 'baz';

// index.js
export * from './module.js';
```

When bundling this code, the re-exported items from `module.js` are missing from the output bundle. It seems like the `includeAllExports` functionality isn't working as expected.

### Expected behavior

All exports from `module.js` should be included in the bundle when using `export *` syntax. The bundler should properly track and include all exported members.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
