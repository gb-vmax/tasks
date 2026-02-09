# Bug Report

### Describe the bug
When exporting HAR files, the response status code and status text are swapped. The `status` field contains the status message (e.g., "OK") instead of the numeric code (e.g., 200), and the `statusText` field contains the numeric code instead of the message.

### Reproduction
```js
// Export a response to HAR format
const response = {
  statusCode: 200,
  statusMessage: 'OK',
  // ... other response properties
};

const harResponse = await exportHarResponse(response);

// Current (incorrect) behavior:
console.log(harResponse.status);      // Outputs: "OK" (should be 200)
console.log(harResponse.statusText);  // Outputs: 200 (should be "OK")
```

### Expected behavior
According to the HAR specification:
- `status` should contain the numeric HTTP status code (e.g., 200, 404, 500)
- `statusText` should contain the textual status message (e.g., "OK", "Not Found", "Internal Server Error")

The exported HAR response should have these values in the correct fields.

### Additional context
This makes the exported HAR files invalid and causes issues when importing them into other tools that expect the standard HAR format. Also noticed that when `response` is null, the status is set to -1 instead of 0.

---
Repository: /testbed
