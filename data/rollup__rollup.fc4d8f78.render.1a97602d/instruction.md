# Bug Report

### Describe the bug

When bundling code that contains unnamed class expressions assigned to variables in `using` or `await using` declarations, the generated output has incorrect syntax. The class name is being inserted at the wrong position in the class expression, causing the output to be malformed.

### Reproduction

```js
using myResource = class {
  constructor() {
    this.value = 42;
  }
};
```

When this code is bundled, the class name insertion happens at the wrong offset, resulting in invalid JavaScript output.

### Expected behavior

The bundler should correctly insert the variable name into the unnamed class expression at the proper position (right after the `class` keyword), producing valid output like:

```js
using myResource = class myResource {
  constructor() {
    this.value = 42;
  }
};
```

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to only affect `using` and `await using` declarations specifically. Regular variable declarations with class expressions work fine.

---
Repository: /testbed
