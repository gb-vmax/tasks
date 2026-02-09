# Bug Report

### Duplicate export detection not working properly

I think I found a bug with how duplicate exports are being detected. It seems like the bundler is allowing duplicate exports in some cases when it shouldn't.

### Reproduction

```js
// module.js
export const foo = 1;
export const foo = 2; // This should throw an error but doesn't
```

Or with re-exports:

```js
// module.js
export { bar } from './other.js';
export const bar = 'test'; // Should also throw an error
```

### Expected behavior

The bundler should throw a duplicate export error when:
1. The same name is exported multiple times in a module
2. A name is both exported locally and re-exported from another module

Currently it seems like it's only catching duplicates when both conditions are true at the same time, instead of either condition being true.

### Additional context

This is causing issues in our build process where we have accidental duplicate exports that should be caught during bundling but are slipping through. The errors only show up at runtime which makes debugging harder.

---
Repository: /testbed
