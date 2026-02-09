# Bug Report

### Describe the bug

I'm experiencing an issue where HTML attributes and their corresponding properties are being swapped when creating Info objects. It looks like the `property` and `attribute` parameters are getting reversed during initialization.

### Reproduction

```js
const info = new Info('className', 'class');

// Expected:
// info.property = 'className'
// info.attribute = 'class'

// Actual:
// info.property = 'class'
// info.attribute = 'className'
```

When both parameters are provided, they appear to be assigned to the wrong fields. This is causing incorrect mappings between DOM properties and HTML attributes.

### Expected behavior

The Info constructor should assign the first parameter to `property` and the second parameter to `attribute`, maintaining the correct relationship between property names and attribute names.

### Additional context

This seems to affect any code that relies on the Info class for mapping between properties and attributes in the rehype-stringify vendor code. The swap is causing downstream issues when trying to serialize HTML elements correctly.

---
Repository: /testbed
