# Bug Report

### Describe the bug

When using JSX with `mode: 'preserve'` and specifying an `importSource`, the validation logic is incorrectly rejecting valid configurations. The error is thrown even when only a `fragment` is specified without a `factory`, which should be a valid combination.

### Reproduction

```js
// This configuration should be valid but throws an error
{
  jsx: {
    mode: 'preserve',
    importSource: 'react',
    fragment: 'Fragment'
    // No factory specified - should be fine
  }
}
```

The error message says:
```
when preserving JSX and specifying an importSource, you also need to specify a factory or fragment
```

But a fragment IS specified in this case.

### Expected behavior

The configuration should be accepted when either `factory` OR `fragment` is provided along with `importSource` in preserve mode. Currently it seems like the validation is checking the wrong condition.

### System Info
- Rollup version: latest
- Node: v18.x

---
Repository: /testbed
