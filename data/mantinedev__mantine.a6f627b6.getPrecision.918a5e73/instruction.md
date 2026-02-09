# Bug Report

### Slider precision calculation broken with decimal step values

I'm experiencing an issue with the Slider component where decimal step values are not being handled correctly. The slider seems to be ignoring the precision of the step value.

### Reproduction
```jsx
<Slider
  min={0}
  max={10}
  step={0.01}
  defaultValue={5}
/>
```

When using a step value like `0.01`, the slider doesn't respect the decimal precision. It seems like the precision calculation is completely off - dragging the slider results in values that don't match the expected step increments.

### Expected behavior
The slider should respect the decimal precision of the step value. For example:
- `step={0.1}` should allow values like 1.0, 1.1, 1.2, etc.
- `step={0.01}` should allow values like 1.00, 1.01, 1.02, etc.
- `step={0.001}` should allow values like 1.000, 1.001, 1.002, etc.

### System Info
- @mantine/core version: latest
- Browser: Chrome

This is affecting our application where we need precise decimal control for measurement inputs. Any help would be appreciated!

---
Repository: /testbed
