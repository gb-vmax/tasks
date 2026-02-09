# Bug Report

### Describe the bug

I'm experiencing an issue with binary expressions where annotations are being removed from the wrong operand. When I have code with pure annotations on binary operations, the annotation removal seems to be targeting the right-hand side instead of the left-hand side.

### Reproduction

```js
const result = /*#__PURE__*/ foo() + bar();
```

After processing, the annotation is removed from the wrong side of the expression. It appears that when both left and right operands are present, the annotation removal logic is only processing the right operand and then returning early, completely skipping the left operand where the annotation actually exists.

### Expected behavior

Annotations should be removed from the left operand of binary expressions, which is where they are typically placed. The current behavior causes annotations to remain in the output when they should be stripped, or worse, removes annotations from the wrong side of the operation.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
