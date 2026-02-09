# Bug Report

### Describe the bug

I'm encountering an issue with class declarations where the class name is being incorrectly handled during the rendering/transformation process. When a class is declared and then referenced, the name collision prevention logic seems to be inverted, causing unexpected behavior in the generated output.

### Reproduction

```js
class MyClass {
  constructor() {
    this.value = 42;
  }
}

export { MyClass };
```

When bundling code with class declarations that have the same name as their assigned variable, the output doesn't render correctly. The class body and decorators are being rendered when they shouldn't be (or vice versa), and name collision checks are being applied to the wrong variables.

### Expected behavior

Class declarations should be properly transformed with correct name handling. When the rendered variable name matches the original class name, the transformation should handle it appropriately. Additionally, variables that are the same as the class variable should not have name restrictions applied to them.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems like it might be a regression in the class declaration handling logic. The behavior appears to be inverted from what it should be.

---
Repository: /testbed
