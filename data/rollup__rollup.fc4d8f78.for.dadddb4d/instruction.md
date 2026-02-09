# Bug Report

### Describe the bug
When using multiple plugins with reduce hooks, the first plugin in the sorted list is being skipped and its transformations are not applied. This causes the reduce hook chain to start from the second plugin instead of processing all plugins in order.

### Reproduction
```js
// Setup with 3 plugins that should all run
const plugin1 = {
  name: 'plugin1',
  transform(code) {
    return code + '// plugin1';
  }
};

const plugin2 = {
  name: 'plugin2',
  transform(code) {
    return code + '// plugin2';
  }
};

const plugin3 = {
  name: 'plugin3',
  transform(code) {
    return code + '// plugin3';
  }
};

// Use all three plugins
// Expected: all plugins should process the code
// Actual: first plugin is skipped
```

### Expected behavior
All plugins in the sorted plugin list should be executed when using reduce hooks. The transformation chain should include every plugin's modifications.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. The first plugin's hook is completely bypassed which breaks plugin chains that depend on all plugins being executed in order.

---
Repository: /testbed
