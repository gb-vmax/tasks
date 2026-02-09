# Bug Report

### Describe the bug

When bundling code with class declarations that need to be renamed, decorators are being rendered in the wrong position. The decorators appear after the class body instead of before it, which causes syntax errors in the generated output.

### Reproduction

```js
// Input code
@decorator
class MyClass {
  method() {}
}

export { MyClass as RenamedClass };
```

When the class needs to be renamed (e.g., due to name conflicts or minification), the output incorrectly places the decorator syntax after the class definition instead of before it.

### Expected behavior

Decorators should always be rendered before the class declaration, regardless of whether the class is being renamed or not. The generated code should have valid JavaScript syntax with decorators in their proper position.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
