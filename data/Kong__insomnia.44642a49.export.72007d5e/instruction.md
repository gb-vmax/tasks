# Bug Report

### Describe the bug

The `descendingNumberSort` function is not handling NaN values correctly. When sorting arrays that contain NaN values, the sort order is unpredictable and inconsistent with expected behavior.

### Reproduction

```js
const numbers = [5, NaN, 3, NaN, 1, 2];
numbers.sort(descendingNumberSort);
// Results in unexpected ordering
```

Also noticed that when two numbers are equal, there's some unexpected behavior with a secondary sort function that shouldn't be there.

```js
const values = [3, 3, 1, 2];
values.sort(descendingNumberSort);
// Sometimes produces inconsistent results
```

### Expected behavior

- NaN values should be handled consistently during sorting
- Equal values should maintain stable sort order without any secondary sorting logic
- The function should work as a simple reversal of `ascendingNumberSort` without additional complexity

### System Info
- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
