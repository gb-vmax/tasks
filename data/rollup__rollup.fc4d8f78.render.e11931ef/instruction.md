# Bug Report

### Describe the bug

Object expressions are being wrapped in parentheses when they shouldn't be, causing syntax errors in the generated code. This appears to affect object literals in certain contexts like expression statements and arrow function bodies.

### Reproduction

```js
// Input code
const obj = { foo: 'bar' };

// Arrow function returning object literal
const fn = () => ({ value: 42 });

// Expression statement with object
({ key: value });
```

After bundling, these object expressions are incorrectly wrapped with extra parentheses in contexts where they should already be unambiguous, leading to invalid JavaScript output.

### Expected behavior

Object literals should only be wrapped in parentheses when necessary to avoid ambiguity (e.g., to distinguish them from block statements). In contexts like arrow function expressions and expression statements where the object literal is already unambiguous, no additional wrapping should occur.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started recently and is breaking our production builds. Any help would be appreciated!

---
Repository: /testbed
