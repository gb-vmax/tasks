# Bug Report

### Describe the bug

I'm experiencing an issue with assignment operations where member expression assignments with operators like `+=`, `-=`, etc. are not being treated correctly in terms of side effects. It seems like the property access that should happen before the assignment is not being accounted for.

### Reproduction

```js
const obj = {
  get value() {
    console.log('getter called');
    return 1;
  },
  set value(v) {
    console.log('setter called');
  }
};

obj.value += 5;
```

### Expected behavior

For compound assignment operators (like `+=`, `-=`, `*=`), the getter should be called first to read the current value before performing the operation and calling the setter. The side effects from accessing the property should be detected.

For simple assignment (`=`), only the setter should be called without accessing the getter first.

### Additional context

This appears to affect how side effects are tracked during tree-shaking or optimization passes. The behavior changed recently and now compound assignments might not be preserving necessary code that has side effects during property access.

---
Repository: /testbed
