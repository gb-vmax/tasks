# Bug Report

### Indicator positioning issue with middle and center placements

I'm experiencing an issue with the Indicator component where the positioning seems off when using `middle` or `center` placements.

### Reproduction

```jsx
// Middle position - indicator appears below the center instead of centered vertically
<Indicator position="middle-start">
  <Avatar src="avatar.png" />
</Indicator>

// Center placement - indicator appears offset to the right instead of centered horizontally
<Indicator position="top-center">
  <Avatar src="avatar.png" />
</Indicator>
```

### Expected behavior

- When using `position="middle-*"`, the indicator should be vertically centered on the target element
- When using `position="*-center"`, the indicator should be horizontally centered on the target element

### Current behavior

The indicator appears misaligned:
- With `middle` position, it's positioned incorrectly on the vertical axis
- With `center` placement, it's offset horizontally instead of being centered

This affects all position combinations that use `middle` or `center` (e.g., `middle-start`, `middle-end`, `top-center`, `bottom-center`, `middle-center`).

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
