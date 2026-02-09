# Bug Report

### Describe the bug

When using `syntheticNamedExports` in my rollup config, I'm noticing that regular exports are no longer being included in the bundle. It seems like only the synthetic named export itself is being processed, while all other exports from the module are being ignored.

### Reproduction

```js
// input.js
export const foo = 'foo';
export const bar = 'bar';
export const baz = 'baz';

// rollup.config.js
export default {
  input: 'input.js',
  output: {
    file: 'bundle.js',
    format: 'es'
  },
  plugins: [
    {
      name: 'test-plugin',
      resolveId(id) {
        if (id === 'input.js') return id;
      },
      load(id) {
        if (id === 'input.js') {
          return {
            code: `export const foo = 'foo'; export const bar = 'bar';`,
            syntheticNamedExports: '__synthetic'
          };
        }
      }
    }
  ]
}
```

### Expected behavior

All regular exports (`foo`, `bar`, etc.) should be included in the bundle along with the synthetic named export. The `syntheticNamedExports` option should add additional functionality without excluding the normal exports.

### Actual behavior

Only the synthetic named export is being processed and included. All other exports from the module are missing from the final bundle.

This seems like a regression - it was working fine before. The logic appears to be inverted somehow.

---
Repository: /testbed
