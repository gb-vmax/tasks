# Bug Report

### Describe the bug

I'm experiencing an issue with keyboard navigation in RTL (right-to-left) mode. When using arrow keys to navigate through elements, the navigation direction is reversed - pressing ArrowRight moves to the previous element and ArrowLeft moves to the next element, which is the opposite of what should happen in RTL layouts.

Additionally, the Home and End keys are behaving incorrectly - Home key jumps to the last element instead of the first, and End key jumps to the first element instead of the last.

### Reproduction

```jsx
// Set up a component with RTL direction
<div dir="rtl">
  <Button>Item 1</Button>
  <Button>Item 2</Button>
  <Button>Item 3</Button>
</div>

// Focus on Item 2
// Press ArrowRight - expects to move to Item 3, but moves to Item 1
// Press ArrowLeft - expects to move to Item 1, but moves to Item 3

// Press Home - expects to focus Item 1, but focuses Item 3
// Press End - expects to focus Item 3, but focuses Item 1
```

### Expected behavior

In RTL mode:
- ArrowRight should navigate to the next element (moving right in the visual order)
- ArrowLeft should navigate to the previous element (moving left in the visual order)
- Home key should focus the first element
- End key should focus the last element

### System Info

- @mantine/core version: latest
- Browser: Chrome/Firefox (affects both)
- Direction: RTL

---
Repository: /testbed
