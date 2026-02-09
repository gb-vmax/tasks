# Bug Report

### Describe the bug

When exporting a default class or function declaration with a name, the `hasId` flag is not being set correctly. This causes issues with variable tracking and reference handling for named default exports.

### Reproduction

```js
// Export a named function as default
export default function myFunction() {
  return 'test';
}

// Or export a named class as default
export default class MyClass {
  constructor() {
    this.value = 'test';
  }
}
```

In both cases, the variable tracking doesn't recognize that these declarations have an identifier, which affects how references to the default export are resolved.

### Expected behavior

Named function and class declarations that are exported as default should have their `hasId` flag set to `true` and properly track the original identifier. Anonymous default exports should behave differently from named ones.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
