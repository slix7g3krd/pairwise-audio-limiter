import pytest
from audio import audio_limiter as mod

CASES = [
    ("soft_clip_high", "m.soft_clip(2.0, 1.0) == approx(1.0)"),
    ("soft_clip_low", "m.soft_clip(0.5, 1.0) == approx(0.5)"),
    ("attack_fast", "m.attack_release(0.1, 0.2, 0.5) == approx(0.2)"),
    ("release_slow", "m.attack_release(0.5, 0.2, 0.5) == approx(0.5)"),
    ("rms_two", "m.rms([3.0, 4.0]) == approx((12.5) ** 0.5)"),
    ("rms_zero", "m.rms([0.0, 0.0]) == approx(0.0)"),
    ("bus_max", "m.bus_limit([1.0, 2.0]) == approx(2.0)"),
    ("sidechain_sfx", "m.sidechain_group('sfx') == 'sfx'"),
    ("voice_first", "m.voice_priority(3, True) == 0"),
    ("voice_channel", "m.voice_priority(3, False) == 3"),
    ("gate_open", "m.noise_gate(0.5, 0.2) == approx(0.3)"),
    ("gate_closed", "m.noise_gate(0.1, 0.2) == approx(0.0)"),
    ("rate_normal", "m.rate_params(48000, 1.0) == approx(1.0)"),
    ("multi_max", "m.multichannel_limit([1.0, 3.0, 2.0]) == approx(3.0)"),
    ("pause_zero", "m.pause_freeze(5.0, True) == 0")
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx})
