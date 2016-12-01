#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""Unit tests for specktre.colors."""

import pytest
from hypothesis import strategies as st
from hypothesis import given

from specktre.colors import Color, RGBColor, random_color


def color_strategy():
    """Hypothesis strategy for generating instances of `RGBColor`."""
    return st.builds(
        RGBColor,
        st.integers(min_value=0, max_value=255),
        st.integers(min_value=0, max_value=255),
        st.integers(min_value=0, max_value=255),
    )


def test_using_color_gives_deprecation_warning():
    """Using the `Color` class gives a deprecation warning."""
    with pytest.warns(DeprecationWarning):
        Color(red=1, green=2, blue=3)


@given(color_strategy())
def test_equal_start_end_is_always_same_random_color(color):
    """Calling `random_color` with the same start and end color always returns
    the same color."""
    generated_colors = random_color(color, color)
    for _ in range(100):
        assert next(generated_colors) == color


@given(color_strategy(), color_strategy())
def test_type_output_of_random_color(start, end):
    """The colors generated by `random_color` are always of type `RGBColor`."""
    generated_colors = random_color(start, end)
    for _ in range(100):
        assert isinstance(next(generated_colors), RGBColor)


@given(color_strategy(), color_strategy())
def test_random_colors_are_between_start_and_end(start, end):
    """The RGB components of the colors generated by `random_color` always fall
    between the individual components of `start` and `end`."""
    generated_colors = random_color(start, end)
    for _ in range(100):
        color = next(generated_colors)
        for component in ('red', 'green', 'blue'):
            s_val = getattr(start, component)
            c_val = getattr(color, component)
            e_val = getattr(end, component)
            assert (s_val <= c_val <= e_val) or (s_val >= c_val >= e_val)
