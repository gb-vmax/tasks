# Bug Report

### Describe the bug

The CLI is only building the first configuration when multiple configurations are provided. After the first build completes, the process exits without processing the remaining configurations.

### Reproduction

Create a rollup config file that exports an array of multiple configurations:

```js
// rollup.config.js
export default [
  {
    input: 'src/main.js',
    output: {
      file: 'dist/bundle1.js',
      format: 'es'
    }
  },
  {
    input: 'src/secondary.js',
    output: {
      file: 'dist/bundle2.js',
      format: 'cjs'
    }
  },
  {
    input: 'src/third.js',
    output: {
      file: 'dist/bundle3.js',
      format: 'iife'
    }
  }
]
```

Run the build command:
```bash
rollup -c
```

### Expected behavior

All three bundles should be generated:
- `dist/bundle1.js`
- `dist/bundle2.js`
- `dist/bundle3.js`

### Actual behavior

Only `dist/bundle1.js` is created. The other two configurations are ignored and never built.

This is a regression from the previous version where all configurations were processed correctly.

---
Repository: /testbed
