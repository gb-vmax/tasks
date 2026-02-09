# Bug Report

### Describe the bug

I'm experiencing an issue with HTML attribute handling in the rehype-stringify module. When setting properties and attributes on elements, they seem to be swapped - the property value ends up in the attribute field and vice versa.

### Reproduction

```js
const info = new Info('propertyName', 'attributeName');

console.log(info.property); // Expected: 'propertyName', Got: 'attributeName'
console.log(info.attribute); // Expected: 'attributeName', Got: 'propertyName'
```

When creating an Info object with both property and attribute parameters, the values appear to be reversed. The property field contains what should be the attribute, and the attribute field contains what should be the property.

### Expected behavior

The Info constructor should assign the first parameter to `this.property` and the second parameter to `this.attribute`, not the other way around.

### Additional context

This is causing issues when processing HTML elements where the distinction between properties and attributes matters (e.g., `class` vs `className`, `for` vs `htmlFor`, etc.). The incorrect mapping leads to malformed HTML output.

---
Repository: /testbed
