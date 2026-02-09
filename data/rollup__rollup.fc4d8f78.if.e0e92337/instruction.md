# Bug Report

### Describe the bug

When passing multiple plugins via the `-p` CLI option separated by commas, the first plugin in the list is being skipped and not loaded. Only the plugins after the first comma are being registered.

### Reproduction

```bash
# Try loading multiple plugins with comma separation
rollup input.js -p node-resolve,commonjs,buble

# Expected: All three plugins (node-resolve, commonjs, buble) should be loaded
# Actual: Only commonjs and buble are loaded, node-resolve is skipped
```

The same issue occurs when using the API directly:

```js
const plugins = 'plugin-a,plugin-b,plugin-c';
// Only plugin-b and plugin-c get loaded, plugin-a is missing
```

### Expected behavior

All plugins specified in a comma-separated list should be loaded and registered, including the first one. The command `-p node-resolve,commonjs,buble` should load all three plugins in order.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: Linux

---
Repository: /testbed
