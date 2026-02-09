# Bug Report

### Describe the bug

I'm encountering an issue where the `#__PURE__` annotation is not being respected correctly during side effect analysis. When a `new` expression is marked with `#__PURE__`, the code is still being treated as having side effects in certain cases.

### Reproduction

```js
// This should be tree-shaken if unused
const unused = /*#__PURE__*/ new SomeClass(sideEffectFunction());
```

In the above code, even though the `new` expression is annotated as pure, it seems like the side effects from the constructor arguments are being evaluated before the purity annotation is checked. This prevents proper tree-shaking of unused pure constructor calls.

### Expected behavior

When a `new` expression is marked with `#__PURE__`, it should be treated as having no side effects and tree-shaken away if the result is unused, regardless of whether the arguments themselves have side effects. The purity annotation should take precedence.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
