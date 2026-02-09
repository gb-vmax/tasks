# Bug Report

### Describe the bug
When using plugins with the `reduceValueSync` hook, the first plugin in the sorted plugin list is being skipped and never executed. This causes the hook to miss processing from the initial plugin, which can lead to incorrect or incomplete transformations.

### Reproduction
```js
// Setup multiple plugins that should all be called
const plugins = [
  {
    name: 'plugin-a',
    transform(code) {
      return code + '// processed by A\n';
    }
  },
  {
    name: 'plugin-b',
    transform(code) {
      return code + '// processed by B\n';
    }
  },
  {
    name: 'plugin-c',
    transform(code) {
      return code + '// processed by C\n';
    }
  }
];

// After running through the plugin driver
// Expected: All three plugins should process the code
// Actual: Only plugin-b and plugin-c are called, plugin-a is skipped
```

### Expected behavior
All plugins in the sorted plugin list should be executed in order. The first plugin should not be skipped.

### Additional context
This appears to affect any hook that uses the reduce pattern where multiple plugins need to sequentially process a value. The first plugin's contribution is completely missing from the final result.

---
Repository: /testbed
