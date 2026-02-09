# Bug Report

### Describe the bug

The `jsonp()` method on the Response object isn't working properly. When I try to parse a JSONP response, I'm getting errors about the payload extraction failing even though the response looks valid.

### Reproduction

```js
const response = new Response({
  body: 'callback({"data": "test"})',
  // ... other response properties
});

// This throws an error about invalid JSONP format
const data = response.jsonp();
```

I'm also seeing issues when the JSONP response has extra whitespace or semicolons at the end. Sometimes it works, sometimes it doesn't - seems inconsistent.

Another case that's failing:
```js
const response = new Response({
  body: '({"wrapped": "object"});',
  // ... other response properties
});

// Should parse the wrapped object but throws error
const data = response.jsonp();
```

### Expected behavior

The `jsonp()` method should correctly extract and parse JSON payloads from JSONP responses in various formats:
- Standard callback format: `callbackName({...})`
- Wrapped objects: `({...})`
- Plain JSON as fallback

It should handle extra whitespace, trailing semicolons, and both object and array payloads.

### Additional context

This used to throw an "unsupported" error before, but now it's implemented and I'm running into these parsing issues. The strict mode parameter also doesn't seem to be working as expected.

---
Repository: /testbed
