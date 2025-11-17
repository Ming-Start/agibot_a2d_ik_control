# Copyright (c) 2025, Agibot IK Control. All Rights Reserved.
"""Setup script for agibot_a2d_ik_control project."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="agibot-a2d-ik-control",
    version="0.1.0",
    description="Agibot A2D Dual Arm IK Control Simulation based on Isaac Lab",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Ming-Start",
    url="https://github.com/Ming-Start/agibot_a2d_ik_control",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "isaaclab>=2.2.0",
        "torch==2.7.0",
        "numpy>=1.21.0",
        "pinocchio>=2.6.0",
        "gymnasium>=0.27.0",
        "scipy>=1.7.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Robotics Researchers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.11",
    ],
)