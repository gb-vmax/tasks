# Bug Report

### Describe the bug

I'm experiencing an issue with schema merging where properties from earlier schema definitions are being lost. When merging multiple schema definitions together, only the properties from the last definition are preserved in the final merged schema, while properties from earlier definitions disappear.

### Reproduction

```js
const schema1 = {
  property: { prop1: 'value1' },
  normal: { norm1: 'normalValue1' }
};

const schema2 = {
  property: { prop2: 'value2' },
  normal: { norm2: 'normalValue2' }
};

const schema3 = {
  property: { prop3: 'value3' },
  normal: { norm3: 'normalValue3' }
};

const merged = merge([schema1, schema2, schema3], 'html');

// Expected: merged.normal should contain norm1, norm2, and norm3
// Actual: merged.normal only contains norm3
console.log(merged.normal); // Only has properties from schema3
```

### Expected behavior

When merging multiple schema definitions, the resulting schema should contain all normal properties from all input schemas, similar to how the `property` field correctly accumulates all properties from all definitions.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
