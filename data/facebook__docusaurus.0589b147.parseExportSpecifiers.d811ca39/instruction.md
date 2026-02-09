# Bug Report

### Describe the bug

I'm experiencing a critical issue where export specifiers are no longer being parsed correctly. When trying to use named exports with the `export { ... }` syntax, the parser fails completely.

### Reproduction

```js
// This export statement causes parsing to fail
export { foo, bar } from './module';

// Also fails with local exports
const baz = 123;
export { baz };
```

The parser appears to be unable to handle the curly brace syntax for export specifiers. This affects any code that uses named exports.

### Expected behavior

Named export statements should parse correctly and the exported identifiers should be recognized. The parser should handle:
- Export specifiers with `from` clause
- Local export specifiers
- Renamed exports like `export { foo as bar }`

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This is blocking our entire build process since we rely heavily on named exports. Any help would be greatly appreciated!

---
Repository: /testbed
