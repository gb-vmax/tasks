# Bug Report

### Duplicate export declarations not being caught

I'm encountering an issue where the bundler is not properly detecting duplicate export declarations in my modules. When I accidentally export the same name twice, the build succeeds without any errors, but this leads to confusing runtime behavior.

### Reproduction

```js
// module.js
export const foo = 'first';
export const foo = 'second'; // Should throw an error but doesn't
```

or

```js
// module.js
export { bar } from './other.js';
export const bar = 'local'; // Should throw an error but doesn't
```

### Expected behavior

The bundler should throw a duplicate export error during the build process when the same name is exported multiple times from a module. This validation is important to catch these issues early rather than having them surface at runtime.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems like a regression as I'm pretty sure this used to work correctly in earlier versions. The duplicate export validation appears to be broken.

---
Repository: /testbed
