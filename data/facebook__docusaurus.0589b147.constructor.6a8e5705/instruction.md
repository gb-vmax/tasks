# Bug Report

### Describe the bug

I'm encountering an issue where HTML attributes and their corresponding JavaScript properties are being swapped/reversed. When working with DOM elements, the property names and attribute names seem to be mixed up.

### Reproduction

```js
// When creating an Info object with property and attribute names
const info = new Info('className', 'class');

// Expected:
// info.property should be 'className'
// info.attribute should be 'class'

// Actual behavior:
// info.property is 'class' (should be 'className')
// info.attribute is 'className' (should be 'class')
```

This causes issues when trying to map between JavaScript property names and HTML attribute names. For example, when dealing with `className` property vs `class` attribute, they get reversed.

### Expected behavior

The `Info` constructor should correctly assign:
- The first parameter to `this.property`
- The second parameter to `this.attribute`

Instead, it appears they're being assigned in reverse order.

### System Info
- rehype-stringify version: 10.0.0

---
Repository: /testbed
