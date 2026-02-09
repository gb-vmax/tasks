# Bug Report

### Describe the bug

The `jsonp()` method on the Response object is not working as expected when parsing JSONP responses. When I try to call `response.jsonp()` on a valid JSONP response, it throws an error about the response not matching JSONP format, even though the response body is correctly formatted.

### Reproduction

```js
// Example JSONP response body
const jsonpResponse = 'callback({ "status": "success", "data": 123 })';

// Trying to parse it
const result = response.jsonp();
// Error: jsonp: response does not match JSONP format
```

I've also noticed that responses with extra whitespace or trailing semicolons sometimes cause issues:

```js
// This also fails
const jsonpWithSemicolon = 'myCallback({"key": "value"});';
const result = response.jsonp();
```

### Expected behavior

The `jsonp()` method should successfully extract and parse the JSON content from valid JSONP responses. It should handle:
- Standard JSONP format: `callbackName({...})`
- Responses with trailing semicolons: `callbackName({...});`
- Responses with extra whitespace
- Nested callback names like `namespace.callback({...})`

The method should return the parsed JSON object, similar to how `response.json()` works for regular JSON responses.

### Additional context

This is blocking our ability to work with legacy APIs that only return JSONP format. The method currently just throws an "unsupported" error, but it would be really useful to have this functionality working properly.

---
Repository: /testbed
