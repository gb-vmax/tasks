# Bug Report

### Describe the bug

When bundling with the `system` format, exported class declarations are being incorrectly transformed. Classes that should maintain their original names are being wrapped in variable assignments, and the system export statement is being added unconditionally regardless of whether the class is actually exported.

### Reproduction

```js
// input.js
export class MyClass {
  constructor() {
    this.value = 42;
  }
}

// Bundle with format: 'system'
```

Expected output should preserve the class declaration when the variable name matches, but instead it's being transformed into:

```js
let MyClass = class MyClass { ... };
System.register('exports', ['MyClass']);
```

This happens even when the class name doesn't need to be renamed. The export statement is also added to all classes in system format, not just the ones that are actually exported.

### Expected behavior

- Classes should only be wrapped in variable assignments when the rendered variable name differs from the original class name
- System export statements should only be added when the class is actually exported (when it exists in `exportNamesByVariable`)
- Classes with matching names should use the standard rendering path

### System Info
- Rollup version: latest
- Output format: system
- Node version: 18.x

---
Repository: /testbed
