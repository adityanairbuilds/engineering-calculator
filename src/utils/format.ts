/** Rounds to a sane number of significant digits and trims floating-point noise. */
export function formatResult(value: number): string {
  if (Number.isInteger(value)) return value.toString();
  const rounded = Number(value.toPrecision(10));
  return rounded.toString();
}
