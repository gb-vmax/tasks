# Bug Report

### Describe the bug

I'm experiencing an issue where `import.meta` properties are being incorrectly tree-shaken from the bundle even when they have side effects. The code is being removed during optimization even though it should be preserved.

### Reproduction

```js
// This code gets removed from the bundle
if (import.meta.env.DEV) {
  console.log('Development mode');
}

// Also affected:
const url = import.meta.url;
someFunction(url); // The assignment gets removed
```

The above code is being completely eliminated from the final bundle, but it should be kept since accessing `import.meta` properties can have side effects in certain environments.

### Expected behavior

Code that accesses `import.meta` properties should not be tree-shaken away. The bundler should treat these accesses as having potential side effects and preserve them in the output.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
