# Bug Report

### Describe the bug

I'm experiencing an issue with the `translate()` function where the `id` and `message` properties appear to be swapped in the extracted translations. When I provide a translation object with both `id` and `message` fields, the resulting translation uses the wrong values for each field.

### Reproduction

```js
translate({
  id: "my.translation.id",
  message: "This is the display text"
})
```

After extraction, the translation entry has:
- The key set to the message text instead of the id
- The message field set to the id instead of the actual message

So instead of getting:
```json
{
  "my.translation.id": {
    "message": "This is the display text"
  }
}
```

I'm getting the values reversed.

### Expected behavior

When using `translate()` with an object containing both `id` and `message`:
- The translation key should be the `id` value
- The `message` field should contain the `message` value

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
