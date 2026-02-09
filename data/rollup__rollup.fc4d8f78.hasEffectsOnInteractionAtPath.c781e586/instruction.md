# Bug Report

### Describe the bug

I'm experiencing an issue where `new` expressions are being incorrectly tree-shaken from my bundle. Code that instantiates objects with side effects is being removed during the build process, causing runtime errors in production.

### Reproduction

```js
class Logger {
  constructor() {
    console.log('Logger initialized');
    window.loggerInstance = this;
  }
}

// This gets removed from the bundle even though it has side effects
new Logger();

// Later in the code, this fails because loggerInstance is undefined
window.loggerInstance.log('test');
```

The `new Logger()` statement is being completely eliminated from the output bundle, even though the constructor has observable side effects (logging and setting a global variable).

### Expected behavior

The `new` expression should be preserved in the bundle when:
1. The constructor has side effects
2. The instantiated object is used elsewhere (even if not directly assigned)

The tree-shaking logic should recognize that instantiating objects can have side effects and should not remove these statements.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

This is blocking our production deployment as critical initialization code is being stripped out.

---
Repository: /testbed
