"""Unit test suite for Info Panel."""

from hexabyte_extended_info.widgets.info_panel import InfoItem, InfoPanel


def test_info_panel_creation():
    """Test the creation of an info panel."""
    panel = InfoPanel(InfoItem("Test Item"), name="Test Panel")
    assert panel is not None
