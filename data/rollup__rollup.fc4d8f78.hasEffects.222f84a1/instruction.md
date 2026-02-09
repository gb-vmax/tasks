# Bug Report

### Describe the bug

I'm experiencing an issue with assignment expressions where certain side effects are not being properly detected during bundling. It seems like the order of evaluation for checking side effects has changed, which is causing some assignments to be incorrectly optimized away.

### Reproduction

When using compound assignment operators (like `+=`, `-=`, etc.) on object properties, the bundler is not correctly preserving the side effects. This appears to affect member expressions that have getters/setters or proxy traps.

```js
const obj = {
  _value: 0,
  get value() {
    console.log('getter called');
    return this._value;
  },
  set value(v) {
    console.log('setter called');
    this._value = v;
  }
};

// With compound assignment operators
obj.value += 5;
```

The expected behavior is that both the getter and setter should be called (since `+=` needs to read the current value before adding to it), but it seems like the side effects are being evaluated in the wrong order, potentially causing the getter call to be missed or the assignment to be optimized incorrectly.

### Expected behavior

For compound assignment operators (`+=`, `-=`, `*=`, etc.), the left-hand side should be accessed/read before the assignment occurs, triggering any getters or property access side effects. Simple assignment with `=` should not trigger these read side effects.

The bundler should correctly preserve all side effects in the proper order for both simple and compound assignments.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
