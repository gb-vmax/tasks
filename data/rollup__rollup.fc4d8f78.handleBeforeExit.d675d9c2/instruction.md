# Bug Report

### Describe the bug

When plugins return unresolved Promises that cause Rollup to exit early, the error message only shows the first unfulfilled hook action instead of all of them. This makes it difficult to debug issues when multiple plugins have unfinished work.

### Reproduction

Create a build configuration with multiple plugins that have unresolved Promises:

```js
// rollup.config.js
export default {
  input: 'src/main.js',
  output: { file: 'dist/bundle.js', format: 'es' },
  plugins: [
    {
      name: 'plugin-a',
      buildStart() {
        return new Promise(() => {}); // Never resolves
      }
    },
    {
      name: 'plugin-b',
      buildStart() {
        return new Promise(() => {}); // Never resolves
      }
    },
    {
      name: 'plugin-c',
      buildStart() {
        return new Promise(() => {}); // Never resolves
      }
    }
  ]
}
```

Run the build and let it exit early. The error message will only mention one unfulfilled action instead of showing all three plugins that have unfinished work.

### Expected behavior

The error message should list all unfulfilled hook actions from all plugins, not just the first one. This would make it much easier to identify all problematic plugins at once rather than having to fix them one by one.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
