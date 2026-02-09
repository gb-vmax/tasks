# Bug Report

### Describe the bug
When using template interpolation with tags at the very beginning of a string (position 0), the interpolator fails to recognize and process them correctly. This affects templates that start immediately with a tag without any preceding text.

### Reproduction
```js
const interpolator = new Interpolator();

// This doesn't work - tag at position 0 is ignored
const template1 = '{{$timestamp}}';
const result1 = interpolator.renderWithFaker(template1);
// Expected: processed faker function
// Actual: returns '{{$timestamp}}' unchanged

// This works fine - tag has text before it
const template2 = 'prefix {{$timestamp}}';
const result2 = interpolator.renderWithFaker(template2);
// Works as expected
```

### Expected behavior
Tags should be processed regardless of their position in the template string. A tag at the start of the template (position 0) should work the same as a tag that appears later in the string.

### Additional context
This also affects templates with only a single tag and no closing `}}` at the end, where the tag position check seems to be too strict.

---
Repository: /testbed
