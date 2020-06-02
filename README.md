# nonlinear
Experimenting with non-linear transformations

## Theory
I was curious about what would happen if we transformed the coordinate system with a 2D transformation matrix which had entries that are functions of the points they are transforming (unlike linear algebra). This is the result, and it looks pretty cool.

## Code
I have implemented this both in Python and Processing. The Processing version runs in real-time, however, is often not as detailed as the Python version (Processing seems to omit the rendering of points if the `delta` value is too low).

The Python version can switch between rendering to disk or attempting to run real-time. Rendering in real-time seems to be laggier than the Processing version, however, can render at arbitrary `delta` values.

(The coordinate system is drawn parametrically. `Delta` is the step increment for the parameter. It can be interpreted as 'amount of detail', with values closer to 0 = more detailed).

They can both be found under `nonlinear/`
