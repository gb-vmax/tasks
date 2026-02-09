# Bug Report

### Describe the bug

I'm experiencing an issue with template interpolation when using tags at the beginning of a string. When a template tag appears at position 0 (the very start of the string), it's not being processed correctly and gets skipped.

### Reproduction

```js
// This doesn't work - tag at the start of the string
const result = interpolator.replaceIn('{{$someFunction}}');
// Expected: function output
// Actual: '{{$someFunction}}' (unchanged)

// This works fine - tag not at the start
const result2 = interpolator.replaceIn('prefix {{$someFunction}}');
// Works as expected
```

The interpolation only seems to work when there's at least one character before the opening `{{` tags. If the tag starts at position 0, it's completely ignored.

### Expected behavior

Template tags should be interpolated regardless of their position in the string. A tag at the beginning of a string should be processed the same way as a tag in the middle or end.

### Additional context

This seems to affect any template that starts immediately with a tag, which is a common use case when you want the entire value to be dynamically generated.

---
Repository: /testbed
