# Bug Report

### Describe the bug

I'm getting a stack overflow error when using a custom `assetFileNames` function that accesses the `name` property. The deprecation warning mentions that accessing `"names"` is deprecated and to use `"name"` instead, but that's backwards - I'm trying to access `name` and the warning is telling me the wrong thing.

### Reproduction

```js
export default {
  output: {
    assetFileNames: (assetInfo) => {
      // Trying to access the name property
      console.log(assetInfo.name);
      return `assets/[name]-[hash][extname]`;
    }
  }
}
```

When this runs, I get:
1. A deprecation warning that says `Accessing the "names" property... Use the "name" property instead` (even though I'm accessing `name`, not `names`)
2. A stack overflow error because it seems to be recursively calling itself

### Expected behavior

- The deprecation warning should correctly state that accessing `"name"` is deprecated and suggest using `"names"` instead
- Accessing the `name` property should return the actual name value, not cause infinite recursion

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
