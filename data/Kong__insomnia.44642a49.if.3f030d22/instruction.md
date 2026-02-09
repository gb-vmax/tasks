# Bug Report

### Describe the bug

I'm experiencing an issue where the blacklist path regex functionality is not working as expected in the render function. When I specify a blacklist regex pattern to exclude certain paths from rendering, those paths are still being processed and rendered instead of being skipped.

### Reproduction

```js
const template = {
  sensitiveData: '{{ _.secret }}',
  allowedData: '{{ _.normal }}',
  nested: {
    blocked: '{{ _.password }}'
  }
};

const context = {
  secret: 'should-not-render',
  normal: 'should-render',
  password: 'also-blocked'
};

// Set up blacklist regex to exclude paths containing "sensitive" or "blocked"
const blacklistRegex = /(sensitiveData|blocked)/;

const result = await render(template, context, null, blacklistRegex);

// Expected: sensitiveData and nested.blocked should remain as templates
// Actual: All fields are rendered, blacklist is ignored
console.log(result);
```

### Expected behavior

When a blacklist path regex is provided, any paths matching that regex should be skipped during rendering and remain as their original template strings. The blacklist should prevent sensitive or excluded fields from being processed.

### Actual behavior

The blacklist regex appears to have no effect - all paths are being rendered regardless of whether they match the blacklist pattern or not.

This is causing security concerns in our application where we need to prevent certain sensitive fields from being processed during the render phase.

---
Repository: /testbed
