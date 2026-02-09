# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with object property copying in the MDX bundler. It seems like properties that should be copied from one object to another are either not being copied at all, or the wrong properties are being selected.

### Reproduction

```js
const source = {
  prop1: 'value1',
  prop2: 'value2',
  prop3: 'value3'
};

const target = {};

// After the internal copy operation, target should have all properties from source
// but it's either empty or has unexpected properties
```

When processing MDX files that rely on object property enumeration and copying, the resulting objects don't contain the expected properties. This breaks the build process for certain MDX configurations.

### Expected behavior

Properties should be correctly copied from source objects to target objects during the bundling process. All enumerable own properties should be transferred unless explicitly excluded.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest LTS

---
Repository: /testbed
