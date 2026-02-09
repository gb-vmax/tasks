# Bug Report

### Describe the bug

I'm experiencing an issue where object properties with side effects are not being properly detected during tree-shaking. It seems like the bundler is incorrectly removing code that should be preserved when object properties have side effects.

### Reproduction

```js
const obj = {
  [sideEffect()]: 'value',
  normalKey: 'value'
}
```

When the key has a side effect (like `sideEffect()` being called), the bundler should preserve this code. However, it appears that both the key AND value need to have side effects for the code to be retained, when it should be retained if EITHER has side effects.

### Expected behavior

The bundler should preserve object properties if either:
- The property key has side effects, OR
- The property value has side effects

Currently it seems to only preserve the property when both have side effects, causing valid side-effectful code to be incorrectly removed during tree-shaking.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
