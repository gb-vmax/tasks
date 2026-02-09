# Bug Report

### Describe the bug

I'm experiencing an issue where duplicate export validation isn't working properly. When I try to export the same identifier multiple times from a module, I expect to get an error about duplicate exports, but instead the code seems to allow it through without any warnings.

### Reproduction

```js
// module.js
export const foo = 1;
export const foo = 2; // Should error but doesn't
```

Or with re-exports:

```js
// module.js
export { bar } from './other.js';
export const bar = 3; // Should error but doesn't
```

### Expected behavior

The bundler should throw an error when the same name is exported multiple times from the same module, either through direct exports or re-exports. This is invalid JavaScript and should be caught during the build process.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
