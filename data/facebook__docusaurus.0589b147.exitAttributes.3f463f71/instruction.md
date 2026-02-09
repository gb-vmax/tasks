# Bug Report

### Describe the bug
When using directives with multiple class attributes, the classes are being concatenated in the wrong order. The first class attribute is being ignored and only subsequent class attributes are being combined.

### Reproduction
```js
// Using a directive with multiple class attributes
:::directive{.first-class .second-class .third-class}
content
:::
```

The resulting output has the classes in an unexpected order, with the first class missing from the concatenated result.

### Expected behavior
All class attributes should be properly concatenated in the order they appear, with the first class included in the final output. For example, if three class attributes are provided (`.first-class`, `.second-class`, `.third-class`), the final `class` property should contain all three classes separated by spaces: `"first-class second-class third-class"`.

### System Info
- remark-directive version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
