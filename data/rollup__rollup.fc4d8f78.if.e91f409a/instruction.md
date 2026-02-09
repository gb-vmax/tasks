# Bug Report

### Describe the bug

When using JSX mode `preserve` with an `importSource` option, Rollup now incorrectly throws an error even when both `factory` and `fragment` are properly configured. The validation logic seems to be checking for the wrong condition.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.jsx',
  jsx: {
    mode: 'preserve',
    importSource: 'preact',
    factory: 'h',
    fragment: 'Fragment'
  }
}
```

Running this configuration now fails with:
```
when preserving JSX and specifying an importSource, you also need to specify a factory or fragment
```

Even though both `factory` and `fragment` are clearly provided.

### Expected behavior

The build should succeed without errors when `importSource`, `factory`, and `fragment` are all specified together in preserve mode. The validation should only fail if one of the required options is actually missing.

### System Info

- Rollup version: latest
- Node version: 18.x

This appears to have started happening recently - the same config worked fine before.

---
Repository: /testbed
