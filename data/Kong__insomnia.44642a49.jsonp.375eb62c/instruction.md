# Bug Report

### Describe the bug
The `jsonp()` method on Response objects is throwing an "unsupported" error instead of actually parsing JSONP responses. This makes it impossible to work with JSONP endpoints in scripts.

### Reproduction
```js
// Assuming you have a response from a JSONP endpoint
const response = pm.response;

// This throws "unsupported" error
const data = response.jsonp();
```

When calling `jsonp()` on a response object, it immediately throws an error saying the method is unsupported, even though JSONP is a common response format that should be parseable.

### Expected behavior
The `jsonp()` method should parse JSONP-formatted response bodies and return the JSON payload. For example, if the response body is:
```
callback({"key": "value"})
```

Then `response.jsonp()` should return `{"key": "value"}`.

It should also support common JSONP variations like:
- `callback({"data": "value"});`
- `/**/callback({"data": "value"})`
- Different callback function names

### System Info
- insomnia-sdk version: latest
- Using pre-request/test scripts

---
Repository: /testbed
