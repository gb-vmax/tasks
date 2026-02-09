# Bug Report

### Describe the bug

I'm experiencing an issue where method calls on objects are being incorrectly flagged as having side effects, causing rollup to fail to tree-shake code that should be safe to remove.

### Reproduction

```js
const obj = {
  getValue() {
    return 42;
  }
};

// This should be tree-shakeable since getValue() has no side effects
const result = obj.getValue();

// But rollup is keeping this code even though result is never used
```

When I build with rollup, the code above is not being eliminated even though it's clearly dead code. The method call appears to be treated as if it has side effects when it doesn't.

### Expected behavior

Pure method calls that don't mutate state or have side effects should be tree-shakeable when their results are unused. The bundler should be able to remove these calls during the optimization phase.

### Additional context

This seems to have started happening recently. My bundle sizes have increased because a lot of what should be dead code is being kept in the output. I've verified that the methods themselves are pure and don't have any side effects.

---
Repository: /testbed
