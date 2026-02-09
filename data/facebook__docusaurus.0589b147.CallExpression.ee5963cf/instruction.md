# Bug Report

### Describe the bug

I'm experiencing an issue with the translation extraction where the `translate()` function seems to be using the wrong field when creating translation entries. When I provide both an `id` and a `message` in the translation object, the extracted translation key doesn't match what I expect.

### Reproduction

```js
translate({
  id: 'homepage.title',
  message: 'Welcome to our site'
})
```

When this gets extracted, the translation key being used appears to be based on the `message` field instead of the `id` field. This causes problems when trying to reference translations by their intended IDs.

### Expected behavior

The translation should be keyed by the `id` field when both `id` and `message` are provided. The `id` should take precedence as the key, with `message` being the actual translation text.

For example, the above code should create a translation entry with key `'homepage.title'`, not `'Welcome to our site'`.

### System Info
- Docusaurus version: latest
- Node version: 18.x

This is causing issues in our project where we use explicit IDs to organize our translations. Any help would be appreciated!

---
Repository: /testbed
