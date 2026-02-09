# Bug Report

### Describe the bug

I'm encountering an issue with the `new` operator where constructor calls are not being properly recognized. When using `new` with a constructor function, the behavior seems incorrect - it's treating the call as if it were a regular function call instead of a constructor invocation.

Additionally, there appears to be a problem with pure annotation comments. Code that should be marked as pure (using `/*#__PURE__*/` comments) is being treated as impure, and vice versa. This is causing unexpected tree-shaking behavior where pure constructor calls are not being removed during dead code elimination.

### Reproduction

```js
class MyClass {
  constructor() {
    this.value = 42;
  }
}

// This should be recognized as a constructor call with 'new'
const instance = new MyClass();

// Pure annotations are also not working correctly
const obj = /*#__PURE__*/ new SomeClass();
```

### Expected behavior

- Constructor calls using `new` should be properly identified as constructor invocations
- Pure annotation comments should correctly mark expressions as pure for tree-shaking purposes
- Dead code elimination should remove unused pure constructor calls

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
