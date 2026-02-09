# Bug Report

### Describe the bug

I'm encountering an issue with attribute name normalization in the schema lookup. When looking up properties using normalized attribute names, the wrong key is being used to access the property mapping.

### Reproduction

```js
const schema = {
  normal: {
    'classname': 'className'
  },
  property: {
    'className': { /* property info */ }
  }
};

// Trying to find property info for 'className'
const value = 'className';
const normal = value.toLowerCase(); // 'classname'

// The lookup fails because it uses the original value instead of the normalized key
const result = schema.property[schema.normal[value]]; // undefined
// Should be: schema.property[schema.normal[normal]]
```

The function is using the original `value` parameter to index into `schema.normal` instead of using the `normal` variable that was already computed. This causes property lookups to fail when the attribute name casing doesn't match exactly.

### Expected behavior

The schema lookup should correctly use the normalized attribute name to find the corresponding property in the schema, regardless of the casing of the input value.

### System Info
- rehype-stringify version: 10.0.0

---
Repository: /testbed
