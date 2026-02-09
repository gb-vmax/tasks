# Bug Report

### Describe the bug

I'm experiencing an issue with HAR export where the `headersSize` and `bodySize` fields are being calculated incorrectly. The exported HAR files now contain values that don't match the actual HTTP response sizes.

### Reproduction

When exporting a response to HAR format:

```js
const response = {
  statusCode: 200,
  statusMessage: 'OK',
  headers: [
    { name: 'Content-Type', value: 'application/json' },
    { name: 'Content-Length', value: '42' }
  ],
  // ... other response data
};

const harResponse = await exportHarResponse(response);
console.log(harResponse.headersSize); // Expected: -1, Getting: calculated value
console.log(harResponse.bodySize);    // Expected: -1, Getting: calculated value
```

The `headersSize` and `bodySize` fields are now being populated with calculated values instead of the expected `-1` values that were returned before. This is causing issues with HAR file validation and compatibility with other tools that expect these fields to be `-1` when the actual size is unknown.

### Expected behavior

The HAR export should maintain the previous behavior where `headersSize` and `bodySize` are set to `-1` (indicating unknown size) rather than attempting to calculate these values. The calculated sizes don't accurately reflect the actual wire transfer sizes and break compatibility.

### Additional context

This appears to have changed recently. The HAR specification allows `-1` for these fields when the actual size cannot be determined, which was the previous behavior.

---
Repository: /testbed
