# Bug Report

### Describe the bug

Template interpolation is failing when the template string starts with a tag at position 0. The interpolator appears to be skipping tags that are at the very beginning of the template string.

### Reproduction

```js
// This works fine - tag is not at the start
const result1 = interpolator.render('prefix {{$faker.name}}', context);

// This fails - tag is at position 0
const result2 = interpolator.render('{{$faker.name}}', context);
// Expected: Generated faker name
// Actual: Returns '{{$faker.name}}' unchanged
```

### Expected behavior

Tags should be processed correctly regardless of their position in the template string, including when they appear at the very beginning (position 0).

### Additional context

This seems to affect any template that starts with a tag. Templates with tags in the middle or end work as expected. Also noticed that non-faker tags (those not starting with `$`) are now being returned without the closing `}}` which seems odd.

---
Repository: /testbed
