# Bug Report

### Describe the bug

I'm experiencing an issue with synthetic named exports where the namespace seems to be getting recalculated on every access instead of being cached properly. This is causing performance issues and potentially incorrect behavior in my bundled output.

### Reproduction

```js
// module.js
export const foo = 'bar';

// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'es'
  },
  plugins: [
    {
      name: 'synthetic-exports',
      resolveId(id) {
        if (id === 'module.js') return id;
      },
      load(id) {
        if (id === 'module.js') {
          return {
            code: 'export const foo = "bar";',
            syntheticNamedExports: true
          };
        }
      }
    }
  ]
};
```

When the synthetic namespace is accessed multiple times, it appears to be regenerated each time rather than using the cached value. The condition that checks whether the namespace has already been computed seems inverted - it only computes when the value is NOT null, which means it never gets initialized on the first call.

### Expected behavior

The synthetic namespace should be computed once on first access and then cached for subsequent accesses. The namespace variable should be set to `undefined` initially to indicate it's being computed, then set to the actual value, and subsequent calls should return the cached result.

### System Info

- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
