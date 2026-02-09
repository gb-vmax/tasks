# Bug Report

### Describe the bug

I'm experiencing an issue with the render function where blacklisted paths are not being properly excluded from rendering. It seems like the blacklist regex is now working in reverse - paths that should be blacklisted are being rendered, and paths that should be rendered are being skipped.

### Reproduction

```js
const obj = {
  normalField: '{{ someVar }}',
  secretField: '{{ secretVar }}'
};

const blacklistPathRegex = /secretField/;

const result = await render(obj, context, blacklistPathRegex);

// Expected: secretField should remain as '{{ secretVar }}' (not rendered)
// Actual: secretField gets rendered while normalField doesn't
```

### Expected behavior

When a `blacklistPathRegex` is provided, paths matching that regex should be skipped during rendering and left as-is. All other paths should be rendered normally with their template variables replaced.

### Additional context

This appears to be a logic issue where the blacklist condition is inverted. Fields that match the blacklist pattern are being processed when they should be ignored, and vice versa.

---
Repository: /testbed
