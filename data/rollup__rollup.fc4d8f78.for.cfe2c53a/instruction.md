# Bug Report

### Describe the bug

When a transform dependency changes, modules that depend on it are not being properly invalidated. The `originalCode` cache is not being cleared, causing stale transformed code to be used instead of re-transforming the module with the updated dependency.

### Reproduction

```js
// Setup a plugin with transform dependencies
const plugin = {
  name: 'test-plugin',
  transform(code, id) {
    this.addWatchFile('config.json'); // Add transform dependency
    const config = readFileSync('config.json', 'utf-8');
    return transformWithConfig(code, config);
  }
}

// Steps:
// 1. Build with initial config.json
// 2. Modify config.json
// 3. Observe that modules are not re-transformed with new config
```

### Expected behavior

When a transform dependency (like `config.json` in the example) is modified, all modules that added it as a watch file should have their transform cache invalidated and be re-transformed on the next build.

### Current behavior

The modules continue to use cached transformed code even though their transform dependency has changed. This means configuration changes or other external files watched via `addWatchFile` don't trigger proper re-transformation.

This seems like a regression - transform dependencies used to properly invalidate the cache before.

---
Repository: /testbed
