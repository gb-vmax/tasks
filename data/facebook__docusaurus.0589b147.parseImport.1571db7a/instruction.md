# Bug Report

### Describe the bug

Import statements are not being parsed correctly. When trying to use standard ES6 import syntax, the parser throws unexpected token errors instead of properly handling the import declaration.

### Reproduction

```js
// This throws an error
import something from 'module-name';

// Also fails
import { named } from 'another-module';
```

The parser seems to be rejecting valid import statements that should work according to the ES6 spec. This breaks any code that uses imports.

### Expected behavior

Standard import declarations should be parsed without errors. Both default imports and named imports should work as expected:

```js
import foo from 'bar';  // Should parse successfully
import { x, y } from 'baz';  // Should also work
```

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
