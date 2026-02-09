# Bug Report

### Describe the bug

I'm experiencing an issue where class property definitions with side effects are not being properly detected during tree-shaking. Some properties that should be retained are being incorrectly removed from the bundle, while others that should be removed are being kept.

### Reproduction

```js
class MyClass {
  // Property with side effect in key - should be retained
  [console.log('key effect')]() {}
  
  // Static property with side effect in value - should be retained
  static prop = console.log('static value effect');
  
  // Property with decorator - should be retained
  @decorator
  decoratedProp = 'value';
}
```

After bundling, the side effects are not being handled correctly. Some properties with clear side effects are being removed while others without side effects are being kept.

### Expected behavior

Properties with side effects (in keys, values, or decorators) should be properly detected and retained during tree-shaking. Properties without side effects should be eligible for removal if unused.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
