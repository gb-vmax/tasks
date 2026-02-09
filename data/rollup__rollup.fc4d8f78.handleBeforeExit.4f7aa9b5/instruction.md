# Bug Report

### Describe the bug

I'm experiencing an issue where plugin promises that fail to resolve are not being properly caught and reported during process exit. It seems like the first plugin driver in the list is being silently skipped when checking for unfinished hook actions.

### Reproduction

```js
// Setup multiple plugins with async hooks
const plugins = [
  {
    name: 'plugin-one',
    buildStart() {
      return new Promise(() => {
        // This promise never resolves
      });
    }
  },
  {
    name: 'plugin-two',
    buildStart() {
      return new Promise(resolve => resolve());
    }
  }
];

// Run the build
// Expected: Error about unfinished hook action in plugin-one
// Actual: No error is thrown, the unfinished action is not reported
```

### Expected behavior

When a plugin returns a Promise that never resolves, the build process should detect this and throw an error listing the unfinished hook actions for ALL plugins, including the first one registered.

Currently it appears that only plugins after the first one are being checked for unfinished actions.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
