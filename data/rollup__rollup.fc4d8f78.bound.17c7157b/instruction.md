# Bug Report

### Describe the bug

I'm experiencing an issue where member expression properties are not being tracked correctly in certain scenarios. It seems like changes to the `bound` flag are not being properly propagated, causing the AST to have inconsistent state.

### Reproduction

```js
// When accessing a member expression with computed properties
const obj = {
  a: {
    b: function() {
      return this.value;
    }
  }
};

// The bound state doesn't update correctly
obj.a.b.call({ value: 123 });
```

After some investigation, it appears that modifications to internal flags on `MemberExpression` nodes aren't being reflected properly. This causes downstream issues where the compiler incorrectly assumes certain expressions are unbound when they should be bound (or vice versa).

### Expected behavior

The `bound` property should be correctly updated and reflected in the AST node state. Any changes to this flag should be properly tracked so that subsequent operations on the member expression work as expected.

### Additional context

This seems to affect tree-shaking and dead code elimination in some cases, as the compiler may make incorrect assumptions about whether certain member expressions need to be preserved or can be optimized away.

---
Repository: /testbed
