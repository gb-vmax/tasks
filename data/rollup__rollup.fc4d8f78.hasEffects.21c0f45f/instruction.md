# Bug Report

### Describe the bug

When using `new` expressions with the `#__PURE__` annotation, the callee's side effects are not being properly checked. The annotation should only suppress side effects from the constructor call itself and its arguments, but it appears to be suppressing side effects from the callee expression as well.

### Reproduction

```js
// Example code that demonstrates the issue
const sideEffect = /* #__PURE__ */ new (getSomeConstructor())();

function getSomeConstructor() {
  console.log('This side effect should be detected');
  return MyClass;
}
```

In this case, even though the `new` expression is marked as pure, the `getSomeConstructor()` call has side effects that should still be detected and prevent tree-shaking or other optimizations.

### Expected behavior

When a `new` expression is annotated with `#__PURE__`:
- Side effects from arguments should be checked
- Side effects from the constructor call itself should be suppressed
- **Side effects from the callee expression should still be detected**

The pure annotation should not cause the callee's own side effects to be ignored.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
