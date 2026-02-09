# Bug Report

### Describe the bug

I'm experiencing an issue with the `expect().to.not.have.jsonBody()` assertion in the Insomnia SDK. When I use this negated assertion, it's not working as expected and seems to be checking the wrong condition.

### Reproduction

```js
const response = insomnia.response;

// This assertion behaves incorrectly
expect(response).to.not.have.jsonBody({ key: 'value' });
```

When the response body does NOT contain the expected JSON, the assertion should pass, but instead it seems to be doing something unexpected. The negated form (`not.have.jsonBody`) doesn't appear to be properly inverting the check.

### Expected behavior

The `expect().to.not.have.jsonBody()` assertion should pass when the response body does NOT match the expected JSON object, and fail when it does match.

### Additional context

This seems to only affect the `jsonBody` assertion when used with the `.not` modifier. Other assertions like `status`, `header`, and `body` work correctly with negation.

---
Repository: /testbed
