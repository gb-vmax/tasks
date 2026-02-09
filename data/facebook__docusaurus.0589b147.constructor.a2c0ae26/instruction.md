# Bug Report

### Describe the bug
After a recent update, there's an issue with property/attribute mapping in the MDX vendor code. When creating Info objects, the property and attribute values are getting swapped - the property field is being set to the attribute value and vice versa.

### Reproduction
```js
const info = new Info('myProperty', 'my-attribute');

console.log(info.property); // Expected: 'myProperty', Actual: 'my-attribute'
console.log(info.attribute); // Expected: 'my-attribute', Actual: 'my-attribute'
```

### Expected behavior
The Info constructor should correctly assign:
- The first parameter to `this.property`
- The second parameter to `this.attribute`

Instead, both fields end up with the same value (the attribute parameter).

### System Info
- Package: @mdx-js/mdx@3.0.0
- Affects property/attribute handling in the Info class

This is causing issues with any code that relies on the correct mapping between properties and attributes in the MDX processing pipeline.

---
Repository: /testbed
