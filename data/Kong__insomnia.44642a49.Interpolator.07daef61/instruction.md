# Bug Report

### Describe the bug

I'm experiencing an issue with template rendering when using the interpolator. When I have a template string that contains tags at the very beginning (position 0), they're not being processed correctly. The interpolator seems to be skipping tags that start at index 0.

### Reproduction

```js
const interpolator = new Interpolator();

// This doesn't work - tag at position 0 is ignored
const template1 = '{{$faker.name}}';
const result1 = interpolator.render(template1, {});
// Expected: generated faker name
// Actual: '{{$faker.name}}' (unchanged)

// This works fine - tag not at position 0
const template2 = 'Name: {{$faker.name}}';
const result2 = interpolator.render(template2, {});
// Works as expected
```

Also noticing that non-faker tags (regular interpolation tags) are getting malformed - they're only getting one closing brace instead of two.

### Expected behavior

- Tags at position 0 should be processed just like tags at any other position
- Regular interpolation tags should maintain their proper `}}` closing syntax

### System Info
- Package: insomnia-sdk
- Version: latest

---
Repository: /testbed
