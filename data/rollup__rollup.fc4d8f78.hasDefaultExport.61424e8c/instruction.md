# Bug Report

### Describe the bug

I'm encountering an issue with module default export detection. When a module re-exports a default export from another module, it's not being recognized as having a default export.

### Reproduction

```js
// a.js
export default 'hello';

// b.js
export { default } from './a.js';

// main.js
import b from './b.js';
```

In this scenario, module `b.js` should be detected as having a default export since it re-exports the default from `a.js`, but it appears the bundler is not recognizing this correctly.

### Expected behavior

Modules that re-export a default export should be treated as having a default export themselves. The `hasDefaultExport` check should return `true` for modules that either:
- Define their own default export, OR
- Re-export a default export from another module

### Additional context

This seems to affect tree-shaking and import resolution. The issue appears after the module has been parsed and the AST is available.

---
Repository: /testbed
