# Bug Report

### Describe the bug

I'm encountering an issue with array expressions that contain spread elements. When an array has multiple spread operators, the order of elements seems to be getting mixed up or properties are being processed in the wrong sequence.

### Reproduction

```js
const arr1 = [1, 2];
const arr2 = [3, 4];
const combined = [...arr1, ...arr2, 5];
```

When the above code is processed, the resulting array structure doesn't maintain the expected order. It appears that spread elements are being handled incorrectly when there are multiple spreads in a single array expression.

### Expected behavior

The array should maintain the correct order of elements:
- First spread: elements from arr1
- Second spread: elements from arr2  
- Regular element: 5

The final array should be `[1, 2, 3, 4, 5]` with all elements in their proper positions.

### Additional context

This seems to affect any array expression with more than one spread operator. Single spreads work fine, but as soon as you have multiple spreads or a mix of spread and regular elements, the ordering gets corrupted.

---
Repository: /testbed
