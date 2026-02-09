# Bug Report

### Describe the bug

I'm experiencing an issue with schema property normalization where normal and property attributes appear to be swapped. When working with schema definitions, the normal properties are being assigned to the property object and vice versa.

### Reproduction

```js
const schema = merge([
  {
    property: { className: 'class' },
    normal: { class: 'className' }
  }
], 'html');

// Expected: schema.property should contain { className: 'class' }
// Actual: schema.property contains { class: 'className' }

// Expected: schema.normal should contain { class: 'className' }  
// Actual: schema.normal contains { className: 'class' }
```

### Expected behavior

The `merge` function should correctly assign:
- `property` attributes from definitions to the resulting schema's `property` object
- `normal` attributes from definitions to the resulting schema's `normal` object

Instead, they appear to be reversed - normal values are going into property and property values are going into normal.

### System Info
- Version: @mdx-js/mdx@3.0.0
- Node: v18.x

---
Repository: /testbed
