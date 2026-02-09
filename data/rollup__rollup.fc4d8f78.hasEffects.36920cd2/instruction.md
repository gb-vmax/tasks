# Bug Report

### Describe the bug

I'm experiencing an issue with the `typeof` operator in unary expressions. It seems like the behavior has changed and now `typeof` checks are being treated incorrectly, causing side effects to be reported when they shouldn't be.

### Reproduction

```js
// This should not report side effects but it does
function test() {
  return typeof someComplexExpression;
}

// The typeof operator should be side-effect free for any expression,
// not just identifiers
const result = typeof (obj.prop.method());
```

### Expected behavior

The `typeof` operator should be considered side-effect free regardless of what expression it's applied to. According to JavaScript semantics, `typeof` never throws an error even if the operand would normally cause an error (like accessing a property of undefined).

For example:
- `typeof undeclaredVariable` - no error
- `typeof obj.nonexistent.property` - no error (even if obj.nonexistent is undefined)
- `typeof someFunction()` - no error (evaluates the function but typeof itself doesn't throw)

The current behavior seems to only treat `typeof identifier` as side-effect free, but it should apply to all expressions.

### Additional context

This affects tree-shaking and dead code elimination, as code that should be removed is being kept because side effects are incorrectly detected.

---
Repository: /testbed
