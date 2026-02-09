# Bug Report

### Describe the bug

The interpolator is not correctly handling template strings that contain multiple Faker function calls. When using multiple `{{$faker}}` tags in a single template, the output gets malformed - the closing braces `}}` are being inserted incorrectly between segments.

### Reproduction

```js
const interpolator = new Interpolator();
const template = "Hello {{$firstName}} {{$lastName}}!";
const result = interpolator.render(template, {});

// Expected: "Hello John Doe!"
// Actual: "Hello John}}Doe!"
```

Another example with mixed content:

```js
const template = "User: {{$username}}, Email: {{$email}}";
const result = interpolator.render(template, {});

// The closing braces appear in wrong places between the generated values
```

### Expected behavior

When a template contains multiple Faker function calls, each should be properly replaced with generated values without extra `}}` appearing in the output. The template delimiters should only appear where they're actually written in the template string.

### Additional context

This seems to affect any template with more than one Faker tag. Single Faker tags work fine, but as soon as you have multiple tags in the same template string, the joining logic adds unwanted closing braces between the segments.

---
Repository: /testbed
