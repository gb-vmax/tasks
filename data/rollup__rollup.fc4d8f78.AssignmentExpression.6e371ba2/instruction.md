# Bug Report

### Describe the bug

I'm experiencing an issue with assignment expressions where side effects are not being properly detected. When using compound assignment operators like `+=`, `-=`, `*=`, etc., the bundler is incorrectly treating them the same as simple `=` assignments, which causes problems with tree-shaking and side effect detection.

### Reproduction

```js
let obj = {
  get value() {
    console.log('getter called');
    return 1;
  },
  set value(v) {
    console.log('setter called');
  }
};

// With compound assignment operators, the getter should be called
// before the setter because the current value needs to be read first
obj.value += 5;

// Expected: both "getter called" and "setter called" logged
// Actual: only "setter called" is logged (getter access is not detected)
```

### Expected behavior

For compound assignment operators (`+=`, `-=`, `*=`, etc.), the left-hand side should be accessed/read before the assignment happens, since these operators need the current value to perform the operation. The bundler should detect this as a potential side effect.

Simple assignment with `=` doesn't need to read the current value, so it shouldn't trigger property access.

### Additional context

This affects code with getters that have side effects. When using compound assignments, those side effects are being incorrectly eliminated during tree-shaking because the property access isn't being detected.

---
Repository: /testbed
