# Bug Report

### Describe the bug

I'm experiencing an issue with plugin execution order in the build process. When multiple plugins are registered and use the same hook, it seems like some plugins are being skipped during execution. The behavior is inconsistent - sometimes only half of the plugins actually run their hooks.

### Reproduction

```js
import { rollup } from 'rollup';

const plugin1 = {
  name: 'plugin-1',
  transform(code) {
    console.log('Plugin 1 executed');
    return code + '// plugin1';
  }
};

const plugin2 = {
  name: 'plugin-2',
  transform(code) {
    console.log('Plugin 2 executed');
    return code + '// plugin2';
  }
};

const plugin3 = {
  name: 'plugin-3',
  transform(code) {
    console.log('Plugin 3 executed');
    return code + '// plugin3';
  }
};

const plugin4 = {
  name: 'plugin-4',
  transform(code) {
    console.log('Plugin 4 executed');
    return code + '// plugin4';
  }
};

await rollup({
  input: 'src/index.js',
  plugins: [plugin1, plugin2, plugin3, plugin4]
});

// Expected: All 4 plugins execute
// Actual: Only plugins 1 and 3 execute (every other plugin is skipped)
```

### Expected behavior

All registered plugins should execute their hooks in the order they were registered. Each plugin's transform hook should be called sequentially.

### Additional context

This seems to have started happening recently. When I have an even number of plugins, only half of them run. With an odd number of plugins, it's still skipping alternating ones. The final output is missing transformations from the skipped plugins.

---
Repository: /testbed
