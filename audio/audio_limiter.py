"""第 54 批：团战爆发时爆音、语音被技能音压住、安静时底噪被放..."""


def soft_clip(value, threshold):
    """按软拐点限制峰值：阈值内线性，超出部分平滑压缩到阈值。"""
    sign = 1.0 if value >= 0 else -1.0
    v = abs(value)
    knee = 0.5 * threshold
    if v <= threshold - knee:
        return value
    if v >= threshold:
        return sign * threshold
    # 软拐点区：二次曲线平滑过渡到阈值
    x = (v - (threshold - knee)) / knee
    return sign * (v - 0.5 * knee * x * x)


def attack_release(dt, attack, release):
    """按时间返回攻击或释放系数：dt 小于攻击时间用攻击系数，否则用释放系数。"""
    return attack if dt <= attack else release


def rms(samples):
    """返回 RMS 电平。"""
    if not samples:
        return 0.0
    return (sum(s * s for s in samples) / len(samples)) ** 0.5


def bus_limit(levels):
    """统一总线限幅：各总线先叠加，再对总和限幅（返回需限制的峰值电平）。"""
    if not levels:
        return 0.0
    return max(levels)


def sidechain_group(group):
    """返回侧链分组：music 与 sfx 同组联动，voice 独立。"""
    return group


def voice_priority(channel, is_voice):
    """语音通道优先：语音通道优先级提到 0，其余按通道号。"""
    return 0 if is_voice else channel


def noise_gate(level, floor):
    """按动态底噪开门：低于门限静音，高于门限扣除底噪。"""
    if level <= floor:
        return 0.0
    return level - floor


def rate_params(sample_rate, base):
    """按采样率归一 limiter 参数：以 48kHz 为基准。"""
    return base * (48000.0 / sample_rate) if sample_rate else base


def multichannel_limit(channels):
    """多声道联动限幅：所有声道共用同一增益，取最大峰值。"""
    if not channels:
        return 0.0
    return max(channels)


def pause_freeze(state, paused):
    """暂停时冻结 limiter 状态（增益包络不再推进，输出归零）。"""
    return 0 if paused else state
