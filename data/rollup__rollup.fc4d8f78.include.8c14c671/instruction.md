# Bug Report

### Describe the bug

I'm experiencing an issue with dynamic imports where the module seems to get included multiple times or the inclusion logic isn't working as expected. After some investigation, it appears that `import()` expressions with options are not being handled correctly during the tree-shaking/inclusion phase.

### Reproduction

```js
// module.js
export const data = { value: 42 };

// main.js
async function loadModule() {
  const module = await import('./module.js', {
    assert: { type: 'json' }
  });
  console.log(module.data);
}

loadModule();
```

When bundling this code, the dynamic import with options doesn't seem to be included properly. The behavior is inconsistent - sometimes the options are processed, sometimes they're not.

### Expected behavior

Dynamic import expressions should be included correctly regardless of whether they have options or not. The inclusion should happen once and the options (if present) should be processed appropriately.

### System Info
- Rollup version: latest
- Node version: 18.x

This might be related to the tree-shaking logic for dynamic imports. Has anyone else run into this?

---
Repository: /testbed
