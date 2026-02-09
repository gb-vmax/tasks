# Bug Report

### Describe the bug

I'm experiencing an issue with HTML tag validation in Docusaurus. When I try to use valid HTML tags in my configuration, they're being rejected with an error message saying the tag is not valid. Conversely, when I use completely invalid/made-up tag names, they seem to pass validation without any issues.

### Reproduction

```js
// This throws an error even though 'div' is a valid HTML tag
const htmlTag = {
  tagName: 'div',
  attributes: {
    class: 'container'
  }
}

// But this doesn't throw an error (it should!)
const invalidTag = {
  tagName: 'notarealtag',
  attributes: {}
}
```

### Expected behavior

Valid HTML tags like `div`, `span`, `meta`, `link`, etc. should be accepted without errors. Invalid or custom tag names that aren't in the allowed list should throw validation errors.

Currently it seems like the validation logic is inverted - it's rejecting valid tags and accepting invalid ones.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
