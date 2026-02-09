# Bug Report

### Describe the bug

I'm experiencing an issue with method calls on objects where the tree-shaking/side-effect detection seems to be broken. When calling methods on objects (not using `new`), the behavior is incorrect and the calls are being treated as constructor invocations.

### Reproduction

```js
const obj = {
  method() {
    console.log('called');
  }
};

obj.method(); // This should be treated as a regular method call
```

The issue appears to be related to how member expression method calls are being analyzed. The call expression is incorrectly identifying regular method calls, which is affecting dead code elimination and side effect tracking.

### Expected behavior

Regular method calls (like `obj.method()`) should be distinguished from constructor calls (like `new Constructor()`). The interaction type should correctly reflect that these are normal function calls, not constructor invocations.

### Additional context

This seems to affect how the bundler determines whether code can be safely removed during tree-shaking. Method calls that should be preserved are potentially being treated incorrectly.

---
Repository: /testbed
