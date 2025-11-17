# Agibot A2D Dual Arm IK Control Simulation

基于 Isaac Lab 的 Agibot A2D 双臂逆运动学控制仿真项目。

## 项目目标

- ✅ 在 Isaac Sim 中加载 Agibot A2D 机器人模型
- ✅ 实现基于 Pinocchio 的双臂逆运动学求解
- ✅ 给定末端执行器位姿，自动计算关节角度
- ✅ 通过 IK 控制机器人双臂运动
- ✅ 可视化仿真过程和控制结果

## 快速开始

### 环境配置

```bash
# 1. 克隆项目
git clone https://github.com/Ming-Start/agibot_a2d_ik_control.git
cd agibot_a2d_ik_control

# 2. 创建虚拟环境（推荐）
conda create -n env_isaac python==3.11.0
conda activate env_isaac

# 3. 安装依赖
pip install -r requirements.txt

# 4. 配置环境变量
cp .env.example .env
# 编辑 .env 文件，设置你的 Isaac Sim 路径
```

### 运行仿真

```bash
# 基本运行
python sim_a2d_main.py

# 指定参数
python sim_a2d_main.py --num-steps 2000 --headless

# 更多选项
python sim_a2d_main.py --help
```

## 项目结构

```
agibot_a2d_ik_control/
├── robots/              # 机器人配置
│   └── agibot_a2d.py
├── ik_solvers/          # IK 求解器
│   ├── dual_arm_ik.py
│   └── ik_utils.py
├── tasks/               # 仿真任务
│   └── a2d_tasks/
│       └── a2d_ik_task.py
├── tests/               # 单元测试
├── assets/              # 资源文件
│   └── robots/
│       └── a2d.usd
├── sim_a2d_main.py      # 主程序入口
└── requirements.txt
```

## 开发文档

- [安装指南](docs/installation.md)
- [快速开始](docs/quickstart.md)
- [API 文档](docs/api.md)

## 许可证

Apache License 2.0

## 贡献

欢迎提交 Issue 和 Pull Request！