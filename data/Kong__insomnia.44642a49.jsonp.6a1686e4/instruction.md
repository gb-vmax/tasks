# Bug Report

### Describe the bug

The `jsonp()` method on the Response object is throwing an "unsupported" error instead of actually parsing JSONP responses. This makes it impossible to work with JSONP endpoints in the SDK.

### Reproduction

```js
const response = new Response({
  body: 'callback({"status": "success", "data": 123})'
});

// This throws an error instead of parsing
const data = response.jsonp();
```

Expected the method to extract and parse the JSON data from the JSONP callback wrapper, but instead it just throws an unsupported error.

### Expected behavior

The `jsonp()` method should:
1. Extract the JSON payload from the JSONP callback wrapper
2. Parse the JSON content
3. Return the parsed object

For example, given a response body like `myCallback({"foo": "bar"})`, calling `response.jsonp()` should return `{foo: "bar"}`.

### Additional context

This is blocking our ability to work with legacy APIs that only support JSONP format. The method exists in the API but is currently non-functional.

---
Repository: /testbed
