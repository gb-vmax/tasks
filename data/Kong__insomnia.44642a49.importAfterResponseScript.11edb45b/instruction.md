# Bug Report

### Describe the bug

When importing Postman collections that contain disabled test scripts, the disabled scripts are still being imported and executed in Insomnia. According to Postman's specification, when an event has `disabled: true`, it should not be executed, but currently Insomnia is ignoring this flag during import.

### Reproduction

1. Create a Postman collection with a request that has a test script
2. Disable the test script in Postman (set `disabled: true` in the event object)
3. Export the collection from Postman
4. Import the collection into Insomnia
5. The disabled test script is still present and will execute

Example Postman collection structure:
```json
{
  "event": [
    {
      "listen": "test",
      "disabled": true,
      "script": {
        "exec": [
          "pm.test('This should not run', function() {",
          "  pm.response.to.have.status(200);",
          "});"
        ]
      }
    }
  ]
}
```

### Expected behavior

When a test script is marked as `disabled: true` in the Postman collection, it should not be imported or should be imported in a disabled/commented state. The script should not execute when the request is run.

### System Info
- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
