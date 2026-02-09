# Bug Report

### Describe the bug

After a recent update, environment objects with `null` color values are causing issues. When an environment has `color: null`, it gets normalized to `null` which breaks the UI rendering of environment color indicators.

### Reproduction

```js
const environment = {
  _id: 'env_1',
  name: 'Test Environment',
  data: { apiKey: 'test' },
  color: null,
  isPrivate: false
};

// After migration, color remains null
// This causes the UI to fail when trying to render color indicators
```

### Expected behavior

When `color` is `null`, it should either:
1. Be left as `null` without normalization, OR
2. Be converted to a valid default color value

Currently the normalization function returns `null` for invalid colors, which breaks components expecting either a valid color string or undefined.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
