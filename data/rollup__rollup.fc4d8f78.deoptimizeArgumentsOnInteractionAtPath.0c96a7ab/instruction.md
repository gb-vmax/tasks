# Bug Report

### Describe the bug

I'm experiencing issues with tree-shaking when using deeply nested object property access. It appears that certain code paths that should be tree-shaken are being incorrectly retained in the bundle, leading to larger than expected output sizes.

### Reproduction

```js
// input.js
const config = {
  settings: {
    advanced: {
      feature: {
        enabled: true
      }
    }
  }
};

function checkFeature() {
  return config.settings.advanced.feature.enabled;
}

// This should be tree-shaken but isn't
if (checkFeature()) {
  console.log('feature enabled');
}
```

When bundling this code, the dead code elimination doesn't work as expected for deeply nested property paths. The code that should be removed is still present in the final bundle.

### Expected behavior

Dead code that depends on deeply nested property access should be properly eliminated when those properties can be statically analyzed. The bundle size should be optimized correctly.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. Previously, the same code would be optimized correctly.

---
Repository: /testbed
