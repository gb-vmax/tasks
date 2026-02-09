# Bug Report

### Describe the bug

When exporting HAR responses, the status code and status message are being swapped. The `status` field contains the status message (string) and the `statusText` field contains the status code (number), which is the opposite of what it should be according to the HAR specification.

Additionally, responses are only being exported when they exist, but the logic seems inverted - when a response is null/undefined, it should return the empty response object, but currently it's doing the opposite.

### Reproduction

```js
const response = {
  statusCode: 200,
  statusMessage: 'OK',
  // ... other response fields
}

const harResponse = await exportHarResponse(response);

console.log(harResponse.status); // Expected: 200, Actual: 'OK'
console.log(harResponse.statusText); // Expected: 'OK', Actual: 200
```

Also, when calling with a null response:
```js
const harResponse = await exportHarResponse(null);
// Expected: returns empty response object
// Actual: attempts to access properties on null response
```

### Expected behavior

- `harResponse.status` should contain the numeric status code (e.g., 200, 404, 500)
- `harResponse.statusText` should contain the string status message (e.g., 'OK', 'Not Found', 'Internal Server Error')
- When response is null, should return the empty response object without attempting to process it

### System Info
- Insomnia version: latest

---
Repository: /testbed
