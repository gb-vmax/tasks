# Bug Report

### Describe the bug
When sending multipart form data requests, the first parameter in the array is being skipped and not included in the request body. Only parameters starting from the second element onwards are being processed.

### Reproduction
```js
const params = [
  { name: 'field1', value: 'value1' },
  { name: 'field2', value: 'value2' },
  { name: 'field3', value: 'value3' }
];

await buildMultipart(params);
// Only field2 and field3 are included in the multipart body
// field1 is missing
```

### Expected behavior
All parameters in the array should be included in the multipart request body, including the first one. The request should contain field1, field2, and field3.

### Additional context
This seems to have started happening recently. When I inspect the actual request being sent, the first form field is consistently missing from the body. This breaks requests that rely on having all fields present.

---
Repository: /testbed
