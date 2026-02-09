# Bug Report

### Describe the bug

I'm experiencing an issue with CSS custom property handling when some properties are marked as `!important` and others are not. It seems like the behavior for determining which properties should be removed has changed unexpectedly.

### Reproduction

```css
:root {
  --my-color: red;
  --my-color: blue !important;
  --my-color: green;
}
```

When processing this CSS, the plugin is not correctly identifying which properties should be kept vs removed. The logic for handling mixed `!important` and non-`!important` declarations of the same property appears to be treating them differently than before.

### Expected behavior

When there's a mix of `!important` and regular declarations for the same custom property:
- If at least one declaration is `!important`, only non-`!important` declarations should be candidates for removal
- The final (last) declaration should be kept unless it's overridden by an `!important` one

Currently, it seems like the check for whether properties have `!important` is too strict, which affects which declarations get removed.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
