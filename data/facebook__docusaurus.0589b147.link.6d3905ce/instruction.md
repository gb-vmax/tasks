# Bug Report

### Describe the bug

I'm encountering an issue with link rendering where the `href` and `title` attributes are not being applied correctly to anchor tags. It seems like the properties object is being spread in a way that doesn't preserve the expected structure.

### Reproduction

```js
const node = {
  type: 'link',
  url: 'https://example.com',
  title: 'Example Link',
  children: [{ type: 'text', value: 'Click here' }]
};

// After processing, the resulting element doesn't have href/title as properties
// Instead they appear to be at the wrong level in the object structure
```

When I process markdown links, the resulting HTML elements don't have the `href` and `title` attributes properly set. The link text renders but the actual link properties are missing or incorrectly placed.

### Expected behavior

The anchor tag should have `href` and `title` as properties in the properties object, with children being a separate field. Something like:

```js
{
  type: "element",
  tagName: "a",
  properties: {
    href: "https://example.com",
    title: "Example Link"
  },
  children: [...]
}
```

### System Info
- remark-rehype version: 11.0.0
- Node version: 18.x

---
Repository: /testbed
