# Bug Report

### Describe the bug

Dynamic imports are being incorrectly tree-shaken from the bundle even when they have side effects. Import expressions should always be preserved in the output since they can have side effects (like loading external modules), but they're being removed during the tree-shaking process.

### Reproduction

```js
// input.js
async function loadModule() {
  const module = await import('./external-module.js');
  return module.default;
}

// After bundling, the import() call is completely removed
// even though it should be preserved
```

Another example:

```js
// This dynamic import has side effects but gets tree-shaken out
if (condition) {
  import('./side-effect-module.js');
}
```

### Expected behavior

Dynamic import expressions should always be included in the bundle output since they can have side effects. The bundler should treat `import()` as having side effects and preserve them during tree-shaking, similar to how static imports with side effects are handled.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
