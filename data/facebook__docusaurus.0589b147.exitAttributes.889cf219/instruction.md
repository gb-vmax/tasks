# Bug Report

### Describe the bug

I'm experiencing an issue with directive attributes where the order of class names appears to be reversed when multiple class attributes are merged. The classes are being concatenated in the wrong order, which is affecting CSS specificity and styling behavior.

### Reproduction

When using directives with multiple class attributes, the resulting merged class string has the classes in reverse order compared to what I would expect:

```js
// Given directive attributes like:
// [['class', 'first'], ['class', 'second'], ['class', 'third']]

// Expected output: class="first second third"
// Actual output: class="third second first"
```

The first class attribute defined is ending up last in the final merged string, which breaks CSS specificity rules where order matters.

### Expected behavior

When multiple class attributes are merged, they should maintain their original order. The first class attribute encountered should appear first in the merged result, not last.

### System Info
- remark-directive version: 3.0.0

This is causing issues in my project where certain styles aren't being applied correctly due to the reversed class order. Any help would be appreciated!

---
Repository: /testbed
