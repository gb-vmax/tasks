# Bug Report

### Describe the bug

I'm encountering an issue where `new` expressions are being incorrectly tree-shaken from the output bundle. When creating instances of classes that have side effects (like modifying global state or performing I/O operations), the bundler is removing these statements even though they should be preserved.

### Reproduction

```js
class Logger {
  constructor() {
    console.log('Logger initialized');
    globalState.loggerCount++;
  }
}

// This constructor call has side effects but gets removed
new Logger();

export function doSomething() {
  return 'result';
}
```

After bundling, the `new Logger()` statement is completely removed from the output, even though the constructor has clear side effects that should be executed.

### Expected behavior

Constructor calls should be preserved in the bundle when they access or modify properties on the created instance, or when they have other observable side effects. The `new Logger()` statement should remain in the bundled output.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
