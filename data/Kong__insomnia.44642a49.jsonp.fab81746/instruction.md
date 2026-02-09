# Bug Report

### Describe the bug

The `jsonp()` method is not correctly parsing JSONP responses. When calling `response.jsonp()` on a valid JSONP response, it throws an error saying it failed to extract the JSONP payload, even though the response body contains a properly formatted JSONP callback.

### Reproduction

```js
// JSONP response body: "myCallback({\"status\": \"ok\", \"data\": 123})"
const response = ... // response object with JSONP body

try {
  const data = response.jsonp();
  console.log(data); // Should parse and return the JSON object
} catch (e) {
  console.error(e); // Throws: "jsonp: failed to extract JSONP payload from response body"
}
```

The method fails to extract the JSON payload from what appears to be a valid JSONP format. The callback name and JSON data are clearly present in the response body but the extraction logic doesn't seem to handle it correctly.

### Expected behavior

The `jsonp()` method should successfully parse JSONP responses in the format `callbackName({...json...})` and return the parsed JSON object. It should handle nested parentheses in the JSON payload and properly identify where the JSON content starts and ends.

### Additional context

This is blocking our ability to work with JSONP APIs. The response bodies are definitely in the correct JSONP format but the parser isn't extracting the data properly.

---
Repository: /testbed
