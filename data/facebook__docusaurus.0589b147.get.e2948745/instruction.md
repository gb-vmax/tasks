# Bug Report

### Describe the bug

I'm encountering an issue with property enumeration when using the mdast-util-to-string vendor module. It appears that properties are not being correctly marked as enumerable when copied between objects.

### Reproduction

```js
const sourceObj = {
  get someProperty() {
    return 'value';
  }
};

Object.defineProperty(sourceObj, 'someProperty', {
  enumerable: false
});

// When copying properties, the enumerable descriptor is not preserved correctly
// Properties that should be non-enumerable are showing up in enumeration
```

### Expected behavior

When copying properties between objects, the enumerable descriptor should be preserved from the source object. Non-enumerable properties should remain non-enumerable after the copy operation.

### System Info
- Jest vendor module: mdast-util-to-string@4.0.0
- Affects property descriptor copying logic

---
Repository: /testbed
