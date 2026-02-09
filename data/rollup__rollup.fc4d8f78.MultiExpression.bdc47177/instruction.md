# Bug Report

### Describe the bug

I'm experiencing an issue with how side effects are being detected in expressions. It seems like the logic for determining whether an expression has effects has been inverted - now it's reporting that expressions have effects when they shouldn't, or vice versa.

### Reproduction

```js
// Example with multiple expressions where some have effects and some don't
const multiExpr = new MultiExpression([
  expressionWithoutEffects,
  expressionWithEffects,
  anotherExpressionWithoutEffects
]);

// This now incorrectly reports that ALL expressions must have effects
// for the result to be true, instead of ANY expression having effects
const hasEffects = multiExpr.hasEffectsOnInteractionAtPath(path, interaction, context);
```

The behavior changed so that it only returns `true` if ALL expressions have effects, when it should return `true` if ANY expression has effects.

### Expected behavior

The method should return `true` if at least one expression in the collection has effects on the interaction at the given path. Currently it seems to require all expressions to have effects before returning `true`.

### Additional context

This is causing incorrect optimization decisions in the bundler, potentially leading to code being included or excluded incorrectly based on side effect analysis.

---
Repository: /testbed
