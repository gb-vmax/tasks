# Bug Report

### Describe the bug

The `jsonp()` method on Response objects is not working properly when parsing JSONP responses. The function appears to have issues with the extraction logic that's causing it to fail on valid JSONP formatted data.

### Reproduction

```js
const response = {
  body: 'callback({"data": "value"})',
  // ... other response properties
}

// Trying to parse JSONP response
const result = response.jsonp()
// Expected: { data: "value" }
// Actual: throws error or returns incorrect result
```

Also happens with different callback function names:

```js
const response = {
  body: 'myCallback({"status": "ok"})',
}

response.jsonp() // doesn't work as expected
```

### Expected behavior

The method should correctly extract and parse the JSON content from JSONP responses regardless of the callback function name used. It should handle common JSONP patterns like:
- `callback({"key": "value"})`
- `myFunc({"key": "value"});`
- `namespace.callback([1, 2, 3])`

### System Info
- insomnia-sdk version: latest
- The issue seems to be in the response.ts file

---
Repository: /testbed
