# Bug Report

### Describe the bug

I'm experiencing an issue with the `util.models.request.getById()` function in template tags. When calling this function, it's returning an empty object `{}` instead of `null` when a request doesn't exist or when there are errors.

This is causing problems in my templates because I can't properly check if a request was found or not. Previously, the function would return `null` for non-existent requests, which allowed me to use simple null checks.

### Reproduction

```js
const requestId = 'non-existent-id';
const request = await context.util.models.request.getById(requestId);

// Expected: request should be null
// Actual: request is an empty object {}

if (!request) {
  // This condition never executes because {} is truthy
  console.log('Request not found');
}
```

The same issue occurs when there's an error fetching the request - instead of returning `null`, it returns an empty object.

### Expected behavior

The function should return `null` when:
- The request ID doesn't exist
- There's an error fetching the request data
- The request data is invalid

This would match the function signature `Promise<Request | null>` and allow proper null checking in templates.

### Additional context

This seems to have changed recently. My existing templates that rely on null checks are now broken because they can't distinguish between a valid empty request object and a failed lookup.

---
Repository: /testbed
