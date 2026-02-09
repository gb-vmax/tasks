# Bug Report

### Describe the bug

I'm experiencing an issue with static blocks in classes where the tree-shaking behavior seems incorrect. When I have a static block with side effects in a class, the bundler is not properly including or excluding the code as expected.

### Reproduction

```js
class MyClass {
  static {
    console.log('This should be included');
    someFunction();
  }
  
  static {
    console.log('Another static block');
  }
}
```

When bundling this code, the static blocks are either being incorrectly removed when they should be kept (because they have side effects), or they're being included when they should be tree-shaken away. The behavior is inconsistent with what I'd expect based on whether the code has side effects or not.

### Expected behavior

Static blocks with side effects should be properly detected and included in the bundle. The bundler should correctly analyze each statement in the static block to determine if it has side effects and make inclusion decisions accordingly.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
