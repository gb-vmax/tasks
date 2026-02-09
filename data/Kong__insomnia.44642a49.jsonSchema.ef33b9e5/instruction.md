# Bug Report

### Describe the bug

After a recent update, the `jsonSchema` validation in the Response object appears to be broken. When trying to validate response bodies against JSON schemas, the validation doesn't work as expected.

### Reproduction

```js
const response = pm.response;

// This no longer works correctly
pm.test("Response matches schema", function() {
    pm.expect(response).to.have.jsonSchema({
        type: "object",
        properties: {
            id: { type: "number" },
            name: { type: "string" }
        }
    });
});
```

The code seems to have some issues with the schema validation logic - it looks like there might be duplicate or malformed code in the response.ts file around the `jsonSchema` method definition.

### Expected behavior

The `jsonSchema` validation should work properly and validate response bodies against the provided schema without any issues.

### Additional context

This appears to be affecting the SDK's ability to validate JSON responses. The problem seems related to how the schema configuration is being parsed or how the validation is being set up.

---
Repository: /testbed
