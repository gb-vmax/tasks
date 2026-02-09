# Bug Report

### Describe the bug

I'm experiencing an issue with object parsing where the first property in an object literal is being treated incorrectly. When parsing objects, it seems like the first property is not being handled the same way as subsequent properties.

### Reproduction

```js
const obj = {
  first: 1,
  second: 2,
  third: 3
}
```

When parsing this object, the behavior differs for the first property compared to the others. The issue appears to be related to how properties are being added during the parsing phase.

### Expected behavior

All properties in an object literal should be parsed and handled consistently, regardless of their position in the object. The first property should behave the same as any other property.

### Additional context

This seems to affect object expressions and might also impact object patterns in destructuring assignments. The issue is subtle but can lead to unexpected behavior when working with object literals.

---
Repository: /testbed
