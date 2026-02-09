# Bug Report

### Describe the bug

I'm experiencing an issue with the `response.to.not.have.jsonSchema()` assertion in the Insomnia SDK. When I try to use the negative assertion to verify that a response does NOT match a JSON schema, it's giving me incorrect results - it seems to be doing the opposite of what I expect.

### Reproduction

```js
pm.test("Response should not match schema", function () {
    const schema = {
        type: "object",
        properties: {
            name: { type: "string" }
        }
    };
    
    // This should pass when response doesn't match the schema
    // but it's behaving incorrectly
    pm.response.to.not.have.jsonSchema(schema);
});
```

### Expected behavior

When using `pm.response.to.not.have.jsonSchema(schema)`, the assertion should pass if the response body does NOT conform to the provided schema, and fail if it does conform. Currently it seems to be doing the inverse.

### System Info
- Insomnia SDK version: latest
- The positive assertion `pm.response.to.have.jsonSchema()` works fine, only the negative version is affected

---
Repository: /testbed
