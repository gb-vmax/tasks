# Bug Report

### Describe the bug
When using `watch` mode with multiple configurations that have different `buildDelay` values, the watcher is using an incorrect delay. It seems like the delay calculation is not working as expected.

### Reproduction
```js
const rollup = require('rollup');

const watcher = rollup.watch([
  {
    input: 'src/main.js',
    output: { file: 'dist/bundle1.js', format: 'es' },
    watch: {
      buildDelay: 1000
    }
  },
  {
    input: 'src/main.js',
    output: { file: 'dist/bundle2.js', format: 'es' },
    watch: {
      buildDelay: 500
    }
  }
]);
```

### Expected behavior
The watcher should use the maximum `buildDelay` value from all configurations (1000ms in this case). Currently it appears to be using a much smaller or incorrect value.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
