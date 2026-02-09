# Bug Report

### Describe the bug

I'm experiencing an issue where modules with side effects are being included in the bundle even when they shouldn't be. It seems like the dependency tree traversal is not correctly filtering out modules based on their `moduleSideEffects` configuration.

### Reproduction

```js
// entry.js
import './moduleA.js';

// moduleA.js (has moduleSideEffects: false)
import './moduleB.js';
console.log('Module A side effect');

// moduleB.js (has moduleSideEffects: true)
console.log('Module B side effect');
```

With the following configuration:
```js
{
  treeshake: {
    moduleSideEffects: (id) => {
      if (id.includes('moduleA')) return false;
      return true;
    }
  }
}
```

### Expected behavior

Only `moduleB.js` should be included in the bundle since `moduleA.js` is marked as having no side effects. However, both modules are being included.

### System Info

- Rollup version: latest
- Node version: 18.x

The dependency resolution seems to be treating all modules as if they have side effects regardless of the configuration. This is causing unnecessary code to be included in the final bundle.

---
Repository: /testbed
