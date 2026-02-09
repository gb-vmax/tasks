# Bug Report

### Describe the bug

I'm experiencing unexpected behavior with object property tracking after a recent update. It seems like the deoptimization logic for integer properties isn't working correctly anymore.

When accessing properties on objects that should be tracked, the bundler appears to be losing track of which properties have been deoptimized. This is causing incorrect tree-shaking behavior where code that should be retained is being removed.

### Reproduction

```js
const obj = {};
for (let i = 0; i < 10; i++) {
  obj[i] = someFunction();
}

// Access with integer key
console.log(obj[5]);
```

In this case, the bundler seems to be treating integer property access differently than expected. The deoptimization state appears to be checking the wrong flag internally.

### Expected behavior

Integer property access should properly track deoptimization state and preserve the necessary code during tree-shaking. The bundler should correctly identify when an object has unknown deoptimized integer properties.

### System Info
- Rollup version: latest
- Node version: 18.x

This might be related to how the internal flags are being checked for object entities. The behavior changed recently and is causing some of my builds to produce incorrect output.

---
Repository: /testbed
