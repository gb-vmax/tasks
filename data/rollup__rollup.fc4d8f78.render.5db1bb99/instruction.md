# Bug Report

### Object expression rendering broken when used as expression statement

I'm encountering an issue where object expressions are being wrapped in parentheses when they shouldn't be, and vice versa. This is causing syntax errors in the generated output.

### Reproduction

When I have code like this:

```js
// Case 1: Object as expression statement
({ foo: 'bar' });

// Case 2: Arrow function returning object
const fn = () => ({ value: 42 });
```

The bundler is producing invalid output. In case 1, the parentheses are being removed when they should be kept (since object literals need parens as expression statements). In case 2, extra parentheses are being added when they're already present.

Additionally, when tree-shaking is involved, properties that should be included in the output are being removed, while properties that should be removed are being kept.

### Expected behavior

- Object expressions used as expression statements should keep their wrapping parentheses
- Arrow functions returning objects should maintain correct parentheses
- Tree-shaking should correctly preserve included properties and remove excluded ones

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. The generated code either throws syntax errors or includes dead code that should have been tree-shaken.

---
Repository: /testbed
