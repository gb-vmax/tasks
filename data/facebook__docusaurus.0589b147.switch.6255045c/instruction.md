# Bug Report

### Describe the bug

I'm experiencing an issue with template literal validation in the ESLint plugin. When using template literals without expressions (e.g., `` `hello world` ``), they are being incorrectly rejected as invalid translation labels, even though they should be treated the same as regular string literals.

### Reproduction

```js
// This works fine
const label1 = 'Hello World';

// This should also work but doesn't
const label2 = `Hello World`;

// Template literals without any ${} expressions should be valid
const label3 = `Simple string`;
```

The validator seems to be treating template literals differently than plain strings, even when they don't contain any expressions. A template literal with no interpolations should behave identically to a regular string literal.

### Expected behavior

Template literals without expressions (no `${}` placeholders) should be recognized as valid string labels, just like regular string literals. Both `` `text` `` and `'text'` should pass validation when they contain valid translation content.

### System Info
- ESLint plugin version: latest
- Node version: 18.x

---
Repository: /testbed
