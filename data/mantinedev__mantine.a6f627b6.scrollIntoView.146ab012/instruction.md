# Bug Report

### Describe the bug

I'm encountering an issue with `scrollIntoView()` when passing a boolean `false` argument. The element's display style is being set to 'none', which causes the element to become hidden instead of just scrolling it into view at the bottom of the viewport.

### Reproduction

```js
const element = document.getElementById('myElement');

// This hides the element instead of scrolling it into view
element.scrollIntoView(false);

// Expected: element scrolls to bottom of viewport
// Actual: element.style.display is set to 'none' and element disappears
```

### Expected behavior

According to the spec, calling `scrollIntoView(false)` should scroll the element so that it's aligned to the bottom of the visible area. It should NOT hide the element by setting its display property to 'none'.

The boolean parameter is supposed to control alignment:
- `true` (or no argument): align to the top
- `false`: align to the bottom

### Additional context

This seems to be affecting any code that relies on the standard `scrollIntoView()` behavior with the boolean parameter. The element becomes invisible which breaks the expected scroll functionality.

---
Repository: /testbed
