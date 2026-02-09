# Bug Report

### Describe the bug

I'm experiencing an issue where `new` expressions with arguments are being incorrectly removed from the bundle even though they have side effects. The code is being tree-shaken when it shouldn't be.

### Reproduction

```js
class Logger {
  constructor(message) {
    console.log(message);
  }
}

// This should NOT be removed since the constructor has side effects
new Logger('Important log message');
```

After bundling, the `new Logger(...)` call gets completely removed from the output, even though the constructor clearly has side effects (logging to console).

### Expected behavior

The `new` expression should be preserved in the bundle when:
1. The constructor has side effects
2. Arguments are passed to the constructor

Even if the instance isn't used, constructors with side effects should not be removed during tree-shaking.

### Additional context

This seems to affect any constructor call with arguments that has side effects. Constructors without arguments seem to work correctly. The issue appears to be related to how side effects are being detected for `new` expressions.

---
Repository: /testbed
