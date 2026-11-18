# pairwise-audio-limiter

团战爆发时爆音、语音被技能音压住、安静时底噪被放大：限幅器用硬 clip；攻击/释放时间固定；阈值按峰值不按 RMS；多段总线各自限幅后叠加；侧链只压音乐不压 SFX；语音优先级按通道号；底噪门限固定；采样率不同 limiter 参数不同；5.1 下每声道独立限幅；暂停时 limiter 状态继续。audio/audio_limiter.py 是核心，tests/test_audio_limiter.py 15个红。要修的是：软拐点；自适应攻击释放；RMS 阈值；总线统一限幅；侧链分组；语音优先级；动态噪声门；采样率归一；多声道联动；暂停冻结。

## 运行

```bash
python -m pytest tests -q
```

初始状态：15 个用例失败。修复实现使全部用例通过，不要修改 `tests/` 下的测试。

子方向：音视频处理；任务类型：Bugfix；语言/框架：Python 3, pytest；环境可复现等级：无外部依赖。
