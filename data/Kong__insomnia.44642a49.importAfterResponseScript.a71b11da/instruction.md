# Bug Report

### Describe the bug

When importing Postman collections that contain multiple test events (events with `listen: 'test'`), only the first test script is being imported. If a collection has multiple test event listeners defined, the subsequent ones are being ignored and not included in the imported request.

### Reproduction

Create a Postman collection with multiple test events:

```json
{
  "event": [
    {
      "listen": "test",
      "script": {
        "exec": ["pm.test('First test', function() {", "  // test logic", "});"]
      }
    },
    {
      "listen": "test", 
      "script": {
        "exec": ["pm.test('Second test', function() {", "  // more test logic", "});"]
      }
    }
  ]
}
```

When importing this collection, only the first test script gets imported. The second test event is completely lost.

### Expected behavior

All test events should be imported and combined into a single after-response script. Both test scripts should be present in the imported request so that all test logic is preserved.

### System Info

- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
