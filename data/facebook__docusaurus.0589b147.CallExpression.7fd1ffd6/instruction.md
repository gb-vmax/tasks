# Bug Report

### Describe the bug

I'm experiencing an issue with the `translate()` function where the `id` and `message` fields appear to be swapped in the extracted translations. When I provide a translation object with both `id` and `message` properties, the extracted translation uses the `message` value as the key and the `id` value as the message content, which is the opposite of what I expect.

### Reproduction

```js
translate({
  id: "homepage.title",
  message: "Welcome to our site"
})
```

When translations are extracted, I would expect:
- Key: `homepage.title`
- Message: `Welcome to our site`

But instead I'm getting:
- Key: `Welcome to our site`
- Message: `homepage.title`

This makes the translation files very confusing and breaks the expected workflow where the `id` should be the stable identifier and `message` should be the translatable text.

### Expected behavior

The translation extraction should use the `id` field as the translation key and the `message` field as the actual message content. If only one is provided, it should fall back appropriately, but when both are present, `id` should take precedence as the key.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
