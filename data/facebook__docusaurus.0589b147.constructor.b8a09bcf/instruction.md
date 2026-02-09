# Bug Report

### Describe the bug

I'm encountering an issue where HTML attributes are not being set correctly when using MDX components. It appears that the `attribute` property is being assigned the wrong value, causing attributes to not match their expected names.

### Reproduction

```js
// When creating an Info object with property and attribute names
const info = new Info('className', 'class');

// Expected:
// info.property = 'className'
// info.attribute = 'class'

// Actual:
// info.property = undefined (or wrong value)
// info.attribute = 'className' (should be 'class')
```

This causes attributes to render incorrectly in the generated HTML. For example, when trying to set a `class` attribute, it might end up using the property name instead of the correct attribute name.

### Expected behavior

The `Info` constructor should correctly assign the `property` parameter to `this.property` and the `attribute` parameter to `this.attribute`. This way, the mapping between JavaScript property names and HTML attribute names works as intended.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
