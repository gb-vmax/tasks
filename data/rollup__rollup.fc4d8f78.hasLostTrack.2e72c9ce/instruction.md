# Bug Report

### Describe the bug

I'm experiencing an issue where object property tracking seems to be inverted or not working correctly. When I modify properties on objects, the bundler appears to be tracking them incorrectly, leading to unexpected behavior in the generated output.

### Reproduction

```js
const obj = {
  foo: {
    bar: 'value'
  }
}

// Modify a nested property
obj.foo.bar = 'new value'

// The tracking state appears inverted - properties that should be 
// tracked as modified are not being detected properly
```

### Expected behavior

The bundler should correctly track when object properties have been modified and maintain accurate state about whether tracking has been lost. Currently it seems like the tracking logic is reversed.

### System Info
- Rollup version: latest
- Node version: 18.x

This is causing issues with tree-shaking and dead code elimination in my project. Properties that should be considered "used" are being incorrectly flagged.

---
Repository: /testbed
