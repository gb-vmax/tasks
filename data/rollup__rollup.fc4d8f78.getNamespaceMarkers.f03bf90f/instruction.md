# Bug Report

### Describe the bug

When generating CommonJS output without named exports, the `Symbol.toStringTag` property is not being added to the exports object even when `output.esModule` is set to `false` and namespace markers are expected.

### Reproduction

```js
// rollup.config.js
export default {
  input: 'src/index.js',
  output: {
    file: 'dist/bundle.js',
    format: 'cjs',
    esModule: false,
    exports: 'default'
  }
};

// src/index.js
export default function() {
  return 'test';
}
```

After bundling, the output should include `Symbol.toStringTag` definition but it's missing from the exports object. The namespace marker that should be present in the generated code is not there.

### Expected behavior

When there are no named exports and `esModule` is disabled, the `Symbol.toStringTag` property should still be defined on the exports object to properly mark it as a module namespace.

The generated output should include:
```js
Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
```

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
