/**
 * @param fn Predicate
 * @returns Predicate that return not of `fn`
 */
export const not =
  <T>(fn: (arg: T, ...args: any[]) => boolean) =>
  (value: T) =>
    !fn(value);
