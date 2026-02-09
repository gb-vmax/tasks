# Bug Report

### Describe the bug

I'm experiencing an issue with HTML tag validation in Docusaurus. When I try to add custom HTML tags to my site configuration, the validation logic seems to be inverted - it's rejecting valid HTML tag objects and potentially accepting invalid ones.

### Reproduction

```js
// In docusaurus.config.js
module.exports = {
  // ...
  headTags: [
    {
      tagName: 'meta',
      attributes: {
        name: 'description',
        content: 'My site description'
      }
    }
  ]
}
```

When running the build, this valid HTML tag object is being rejected with an error about invalid tagName, even though the tagName is clearly a string.

### Expected behavior

Valid HTML tag objects with proper `tagName` strings should be accepted by the validation logic. The validator should only throw errors when:
1. The value is not an object
2. The tagName property is missing or not a string

### System Info
- Docusaurus version: latest
- Node version: 18.x

This seems like the validation conditions might be checking the wrong thing. Has anyone else run into this?

---
Repository: /testbed
