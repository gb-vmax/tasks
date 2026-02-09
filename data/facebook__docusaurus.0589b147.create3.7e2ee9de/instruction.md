# Bug Report

### Describe the bug

I'm experiencing an issue with property normalization in the schema creation logic. When working with properties that have both a property name and an attribute name, the normalization mapping appears to be inconsistent.

### Reproduction

```js
const schema = create3({
  space: 'html',
  properties: {
    someProperty: 'some-attribute'
  },
  mustUseProperty: ['some-attribute']
});

// Trying to look up the normalized property
const result = schema.normal[normalize('someProperty')];
// Expected: 'someProperty'
// Actual: 'some-attribute'
```

When I normalize a property name and try to look it up, I'm getting back the attribute name instead of the property name. This breaks the expected behavior where normalizing a property should consistently map back to the original property identifier.

### Expected behavior

The normalization should create a bidirectional mapping where:
- Normalizing the property name returns the property name
- Normalizing the attribute name returns the property name

This way, both the property and attribute forms can be used interchangeably and always resolve to the correct property.

### System Info
- Package: @mdx-js/mdx@3.0.0
- Node version: 18.x

---
Repository: /testbed
