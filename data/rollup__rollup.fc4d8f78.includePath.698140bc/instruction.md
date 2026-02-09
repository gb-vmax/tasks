# Bug Report

### Describe the bug

I'm experiencing an issue with logical expressions where the wrong branch is being included in the output bundle. When using logical operators like `&&` or `||`, it seems like both branches are being included even when tree-shaking should eliminate the unused branch.

### Reproduction

```js
const condition = true;
const result = condition && expensiveOperation();

// or

const fallback = false;
const value = fallback || defaultValue();
```

In cases where the condition can be statically determined, I would expect only the relevant branch to be included in the bundle. However, both branches appear to be getting included when they shouldn't be.

### Expected behavior

When a logical expression has a branch that can be determined to be unused at build time, that branch should be tree-shaken out of the final bundle. Only the branch that will actually be executed should be included.

### Additional context

This seems to affect both `&&` and `||` operators. The bundler should be able to optimize these cases when the condition is known at compile time, but it's including unnecessary code in the output.

---
Repository: /testbed
