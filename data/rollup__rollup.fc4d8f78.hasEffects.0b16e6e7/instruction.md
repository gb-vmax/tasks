# Bug Report

### Describe the bug

Arrow functions are being incorrectly treated as having side effects, causing them to be retained in the bundle even when they're not used. This results in unnecessary code being included in the final output.

### Reproduction

```js
// input.js
const unusedArrowFn = () => {
  return 42;
};

export const used = 'test';
```

When bundling this code, the unused arrow function declaration should be tree-shaken since it has no side effects and is never called or exported. However, it's currently being kept in the output bundle.

### Expected behavior

Unused arrow function expressions without side effects should be removed during tree-shaking. The bundled output should only contain:

```js
export const used = 'test';
```

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
