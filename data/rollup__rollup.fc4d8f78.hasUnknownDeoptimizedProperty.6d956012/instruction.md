# Bug Report

### Describe the bug

I'm experiencing an issue with object property deoptimization that's causing incorrect behavior in my build. When working with objects that have dynamic properties, the bundler seems to be making incorrect assumptions about which properties have been deoptimized.

### Reproduction

```js
const obj = {
  knownProp: 'value'
};

// Dynamically add properties
obj[computedKey] = 'dynamic';

// Access the property later
console.log(obj[computedKey]);
```

The bundler appears to be treating deoptimized properties incorrectly, leading to unexpected optimization behavior. Properties that should be flagged as having unknown deoptimization are being handled as if they don't have this flag set, or vice versa.

### Expected behavior

The bundler should correctly track which object properties have been deoptimized and handle them appropriately during the optimization phase. Dynamic property access should work consistently regardless of how properties are added to objects.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems like it might be a regression as it was working fine in earlier versions. The issue manifests when dealing with objects that have both static and dynamic properties.

---
Repository: /testbed
