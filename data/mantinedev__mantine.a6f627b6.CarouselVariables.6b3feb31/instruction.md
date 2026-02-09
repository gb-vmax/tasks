# Bug Report

### Describe the bug

The Carousel component is rendering duplicate inline styles when `slideGap` and `slideSize` props are provided. The base values for these props are being applied to all breakpoints, and then the responsive values are being added on top, resulting in doubled style declarations.

### Reproduction

```jsx
import { Carousel } from '@mantine/carousel';

function Demo() {
  return (
    <Carousel
      slideSize="50%"
      slideGap="md"
      breakpoints={[
        { maxWidth: 'md', slideSize: '100%', slideGap: 'sm' }
      ]}
    >
      <Carousel.Slide>Slide 1</Carousel.Slide>
      <Carousel.Slide>Slide 2</Carousel.Slide>
    </Carousel>
  );
}
```

When inspecting the rendered output, you'll see that the carousel variables are defined twice - once with the base values and again with the breakpoint-specific values. This causes the styles to be duplicated in the DOM.

### Expected behavior

The carousel should only render the base `slideGap` and `slideSize` values once, followed by the responsive overrides for specific breakpoints. There shouldn't be duplicate style declarations.

### System Info

- @mantine/carousel version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
