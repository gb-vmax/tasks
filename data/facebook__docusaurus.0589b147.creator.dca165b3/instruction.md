# Bug Report

### CSS custom properties incorrectly removed when duplicate declarations exist

I'm encountering an issue with the CSS optimization where duplicate custom property declarations are being removed incorrectly. It seems like the wrong properties are being kept/removed when there are multiple declarations of the same CSS custom property.

### Reproduction

```css
:root {
  --primary-color: red;
  --primary-color: blue;
  --primary-color: green;
}
```

After processing, the first declaration (`red`) is kept instead of the last one (`green`). In CSS, later declarations should override earlier ones, so the expected behavior is that `green` should be the final value.

### Expected behavior

When multiple declarations of the same custom property exist (without `!important`), only the **last** declaration should be kept, and all previous ones should be removed during optimization. The cascade order matters in CSS.

### Additional context

This appears to affect the `remove-overridden-custom-properties` plugin. The issue manifests when you have duplicate custom property declarations in your CSS - the optimizer is keeping the wrong declaration.

---
Repository: /testbed
