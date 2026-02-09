# Bug Report

### Describe the bug

I'm encountering an issue where property definitions with side effects are not being properly detected during tree-shaking. It seems like certain class property initializers that should be preserved (because they have side effects) are being incorrectly removed from the bundle.

### Reproduction

```js
class MyClass {
  // This property has side effects in its key
  [console.log('key evaluation')]() {}
  
  // Static property with side effects in value
  static prop = console.log('static init');
  
  // Instance property with side effects
  instanceProp = someFunction();
}
```

When bundling code like this, properties that should be retained because they have observable side effects are being dropped. This is causing runtime errors in my application where I expect certain initialization code to run.

### Expected behavior

All property definitions with side effects (either in the key computation, value initialization, or decorators) should be preserved in the output bundle, regardless of whether they appear to be used elsewhere in the code.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems like it might be related to how the bundler analyzes side effects in class property definitions. The tree-shaking is being too aggressive and removing code that actually needs to execute.

---
Repository: /testbed
