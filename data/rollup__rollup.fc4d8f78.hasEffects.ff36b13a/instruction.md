# Bug Report

### Describe the bug

When using class declarations with side effects in the class body, the side effects are being incorrectly evaluated in the wrong order. This causes issues when the class body contains code that should execute before the class identifier is marked as reached.

### Reproduction

```js
class MyClass {
  static {
    // This block should be evaluated for side effects
    // before the class identifier is considered "reached"
    console.log('Static initialization block');
    someGlobalFunction();
  }
}
```

The issue appears when:
1. A class has a static initialization block or other side effects in the body
2. The class identifier needs to be marked as reached during side effect analysis
3. The order of evaluation matters for correct tree-shaking or dead code elimination

### Expected behavior

The class body side effects should be evaluated in the correct order relative to when the class identifier is marked as reached. The identifier should be marked before checking for initialization effects to ensure proper dependency tracking.

### Additional context

This seems to affect classes with:
- Static initialization blocks
- Constructor side effects
- Method definitions that may have side effects

The evaluation order is critical for accurate side effect detection and tree-shaking analysis.

---
Repository: /testbed
