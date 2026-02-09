# Bug Report

### Describe the bug

I'm experiencing an issue where spread elements in object/array literals are being incorrectly tree-shaken away even when they have side effects. The spread operation should be preserved when the argument has effects, but it seems like the bundler is removing it in some cases.

### Reproduction

```js
const obj = {
  get foo() {
    console.log('side effect');
    return 1;
  }
};

// This spread should trigger the getter and preserve the side effect
const result = { ...obj };
```

When bundling this code, the spread operation gets removed even though accessing `obj.foo` has a side effect (the console.log). The expected behavior is that the spread should be preserved to maintain the side effect.

### Expected behavior

The spread element should be included in the output when:
1. The argument itself has effects, OR
2. Property read side effects are enabled and the argument has effects on property access

Currently it seems like both conditions need to be true for the spread to be preserved, which causes valid side effects to be tree-shaken away.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
