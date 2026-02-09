# Bug Report

### Describe the bug

I'm experiencing an issue with class property definitions where static properties with side effects are not being properly detected. When a class has a static property with an initializer that has side effects, those effects are not being tracked correctly, which can lead to incorrect tree-shaking or code elimination.

### Reproduction

```js
class MyClass {
  static prop = sideEffect();
}
```

In this case, the `sideEffect()` call should be preserved during bundling, but it appears to be getting removed or not properly tracked. This only happens with static properties - instance properties seem to work fine.

### Expected behavior

Static property initializers with side effects should be detected and preserved during the bundling process, just like instance properties are.

### Additional context

This seems to affect static properties specifically. Non-static properties don't have this issue. The side effects should be evaluated regardless of whether the property is static or not.

---
Repository: /testbed
