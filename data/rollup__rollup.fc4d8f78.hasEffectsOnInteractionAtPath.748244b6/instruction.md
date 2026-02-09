# Bug Report

### Describe the bug

I'm experiencing an issue where constructor calls with the `new` keyword are not being tracked correctly for side effects. It seems like the tracking logic is inverted - when I instantiate a class with `new`, the side effect detection doesn't work as expected.

### Reproduction

```js
class MyClass {
  constructor() {
    // side effects here
    console.log('instantiated');
  }
}

// Using new keyword
const instance = new MyClass();

// The instantiation tracking appears to be using the wrong context
// Expected: should track as instantiated
// Actual: seems to be tracking as called instead
```

### Expected behavior

When using `new` to instantiate a class, the system should properly track it as an instantiation interaction and detect side effects accordingly. The tracking context should differentiate between regular function calls and constructor calls with `new`.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
