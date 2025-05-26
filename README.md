# MCP构建指南服务器

这是一个使用Model Context Protocol (MCP)创建的服务器，旨在为客户端提供关于如何搭建和使用MCP的全面信息。

## 功能特点

该服务器提供多种资源和工具，帮助你了解MCP：

- MCP核心概念解释（服务器、资源、工具、提示等）
- 安装和运行指南
- 代码示例
- 高级用法说明

## 安装

1. 确保已安装Python 3.8+
2. 安装MCP SDK:
```bash
pip install "mcp[cli]"
```

## 运行服务器

### 直接运行
```bash
python mcp_server.py
```

### 使用MCP CLI工具运行
```bash
mcp run mcp_server.py
```

### 在开发模式下运行（带调试器）
```bash
mcp dev mcp_server.py
```

## 在Claude桌面版中使用

你可以将此服务器安装到Claude桌面版应用中：

```bash
mcp install mcp_server.py --name "MCP构建指南"
```

## 可用资源

服务器提供以下资源类别：

### MCP核心概念
- concepts://overview - MCP概述
- concepts://server - 服务器概念
- concepts://resources - 资源概念
- concepts://tools - 工具概念
- concepts://prompts - 提示概念

### 安装与运行指南
- setup://installation - 安装指南
- setup://running - 运行指南

### 示例代码
- examples://echo_server - Echo服务器示例
- examples://sqlite_explorer - SQLite浏览器示例

### 高级用法
- advanced://low_level_server - 低级服务器实现
- advanced://clients - 客户端实现

## 可用工具

服务器提供以下工具：

- `get_concept_details(concept_name)` - 获取特定MCP概念的详细信息
- `list_available_resources()` - 列出服务器上的所有可用资源路径
- `get_example_code(example_name)` - 获取示例代码

## 可用提示

- `mcp_guide_prompt` - MCP指南提示模板 