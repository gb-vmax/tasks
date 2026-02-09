# Bug Report

### Describe the bug

When using `response.to.not.have.jsonSchema()` with an empty object `{}`, the assertion is not working as expected. The behavior seems to be inverted - it's now checking that the response *does* have the schema instead of checking that it doesn't.

### Reproduction

```js
pm.test("Response should not match empty schema", function () {
    pm.response.to.not.have.jsonSchema({});
});
```

When the response has a JSON body, this test fails even though we're explicitly checking for `not.have.jsonSchema` with an empty schema object.

### Expected behavior

The `to.not.have.jsonSchema({})` assertion should pass when we want to verify that the response doesn't match the given schema. The negation (`not`) should properly invert the schema validation behavior.

### System Info
- Package: insomnia-sdk
- Using the response assertion API

---
Repository: /testbed
