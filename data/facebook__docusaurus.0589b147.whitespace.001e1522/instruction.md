# Bug Report

### Describe the bug

I'm experiencing an issue with whitespace detection in the hast-util-whitespace module. When passing different types of values to the `whitespace()` function, it's returning incorrect results - specifically, it seems to be inverting the logic for object vs non-object inputs.

### Reproduction

```js
// Case 1: Passing a text node object
const textNode = {
  type: 'text',
  value: '   \n\t  '
};
console.log(whitespace(textNode)); // Expected: true, but getting false

// Case 2: Passing a non-text node object
const elementNode = {
  type: 'element',
  tagName: 'div'
};
console.log(whitespace(elementNode)); // Expected: false, but behavior is wrong

// Case 3: Passing a string directly
const str = '   \n  ';
console.log(whitespace(str)); // Expected: true, but getting unexpected result
```

### Expected behavior

The function should correctly identify whitespace-only content:
- For text node objects with whitespace-only values, it should return `true`
- For non-text node objects, it should return `false`
- For string values containing only whitespace, it should return `true`

Currently, the logic appears to be backwards and is not properly distinguishing between object and non-object inputs.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
