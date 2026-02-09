# Bug Report

### Describe the bug

I'm experiencing an issue where side effects in class property definitions are not being properly detected. It seems like properties with side effects in their keys are being incorrectly tree-shaken or optimized away, causing unexpected behavior at runtime.

### Reproduction

```js
class MyClass {
  [console.log('key side effect')]() {}
  
  static value = console.log('static value side effect');
}
```

When bundling code like this, the side effects from computed property keys appear to be getting removed even though they should be preserved. The `console.log` statements in the property key are not executing in the bundled output.

### Expected behavior

All side effects in class property definitions should be detected and preserved during bundling:
- Side effects in computed property keys should always be preserved
- Side effects in static property values should be preserved
- Side effects from decorators should be preserved

The bundler should treat these as having effects and not remove them during tree-shaking.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
