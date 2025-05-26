from mcp.server.fastmcp import FastMCP, Context
import json

# 创建MCP服务器
mcp = FastMCP("MCP-构建指南")

# MCP核心概念资源
@mcp.resource("concepts://overview")
def get_overview() -> str:
    """提供MCP的概述信息"""
    return """
    MCP (Model Context Protocol) 是一个标准化协议，允许应用程序以标准化方式为LLM提供上下文，
    将提供上下文的关注点与实际LLM交互分离。Python SDK实现了完整的MCP规范。
    
    MCP核心功能:
    - 构建可以连接到任何MCP服务器的MCP客户端
    - 创建暴露资源、提示和工具的MCP服务器
    - 使用标准传输如stdio、SSE和Streamable HTTP
    - 处理所有MCP协议消息和生命周期事件
    """

@mcp.resource("concepts://server")
def get_server_concept() -> str:
    """MCP服务器概念说明"""
    return """
    FastMCP服务器是MCP协议的核心接口。它处理连接管理、协议合规性和消息路由。
    
    服务器功能:
    - 创建命名服务器
    - 指定部署和开发依赖
    - 管理应用程序生命周期
    - 支持类型安全的上下文
    
    基本服务器创建示例:
    ```python
    from mcp.server.fastmcp import FastMCP
    
    # 创建一个命名服务器
    mcp = FastMCP("My App")
    ```
    """

@mcp.resource("concepts://resources")
def get_resources_concept() -> str:
    """MCP资源概念说明"""
    return """
    资源是向LLM公开数据的方式。它们类似于REST API中的GET端点 - 它们提供数据，但不应执行重要计算或产生副作用。
    
    资源示例:
    ```python
    from mcp.server.fastmcp import FastMCP
    
    mcp = FastMCP("My App")
    
    @mcp.resource("config://app")
    def get_config() -> str:
        \"\"\"静态配置数据\"\"\"
        return "App configuration here"
    
    @mcp.resource("users://{user_id}/profile")
    def get_user_profile(user_id: str) -> str:
        \"\"\"动态用户数据\"\"\"
        return f"Profile data for user {user_id}"
    ```
    """

@mcp.resource("concepts://tools")
def get_tools_concept() -> str:
    """MCP工具概念说明"""
    return """
    工具允许LLM通过您的服务器执行操作。与资源不同，工具预期执行计算并产生副作用。
    
    工具示例:
    ```python
    import httpx
    from mcp.server.fastmcp import FastMCP
    
    mcp = FastMCP("My App")
    
    @mcp.tool()
    def calculate_bmi(weight_kg: float, height_m: float) -> float:
        \"\"\"计算BMI，使用kg为单位的体重和米为单位的身高\"\"\"
        return weight_kg / (height_m**2)
    
    @mcp.tool()
    async def fetch_weather(city: str) -> str:
        \"\"\"获取城市的当前天气\"\"\"
        async with httpx.AsyncClient() as client:
            response = await client.get(f"https://api.weather.com/{city}")
            return response.text
    ```
    """

@mcp.resource("concepts://prompts")
def get_prompts_concept() -> str:
    """MCP提示概念说明"""
    return """
    提示是可重用的模板，帮助LLM有效地与您的服务器交互。
    
    提示示例:
    ```python
    from mcp.server.fastmcp import FastMCP
    from mcp.server.fastmcp.prompts import base
    
    mcp = FastMCP("My App")
    
    @mcp.prompt()
    def review_code(code: str) -> str:
        return f"Please review this code:\\n\\n{code}"
    
    @mcp.prompt()
    def debug_error(error: str) -> list[base.Message]:
        return [
            base.UserMessage("I'm seeing this error:"),
            base.UserMessage(error),
            base.AssistantMessage("I'll help debug that. What have you tried so far?"),
        ]
    ```
    """

# 安装和运行指南
@mcp.resource("setup://installation")
def get_installation_info() -> str:
    """MCP安装指南"""
    return """
    安装MCP到你的Python项目:
    
    推荐使用uv管理Python项目：
    ```bash
    # 创建新的uv管理项目
    uv init mcp-server-demo
    cd mcp-server-demo
    
    # 添加MCP到项目依赖
    uv add "mcp[cli]"
    ```
    
    或者使用pip：
    ```bash
    pip install "mcp[cli]"
    ```
    
    运行独立MCP开发工具：
    ```bash
    uv run mcp
    ```
    """

@mcp.resource("setup://running")
def get_running_info() -> str:
    """MCP服务器运行指南"""
    return """
    运行MCP服务器有多种方式:
    
    1. 开发模式:
    ```bash
    mcp dev server.py
    
    # 添加依赖
    mcp dev server.py --with pandas --with numpy
    
    # 挂载本地代码
    mcp dev server.py --with-editable .
    ```
    
    2. Claude桌面集成:
    ```bash
    mcp install server.py
    
    # 自定义名称
    mcp install server.py --name "My Analytics Server"
    
    # 环境变量
    mcp install server.py -v API_KEY=abc123 -v DB_URL=postgres://...
    mcp install server.py -f .env
    ```
    
    3. 直接执行:
    ```python
    from mcp.server.fastmcp import FastMCP
    
    mcp = FastMCP("My App")
    
    if __name__ == "__main__":
        mcp.run()
    ```
    
    使用以下命令运行:
    ```bash
    python server.py
    # 或
    mcp run server.py
    ```
    """

# 示例代码
@mcp.resource("examples://echo_server")
def get_echo_server_example() -> str:
    """Echo服务器示例"""
    return """
    一个简单的服务器，展示资源、工具和提示:
    
    ```python
    from mcp.server.fastmcp import FastMCP
    
    mcp = FastMCP("Echo")
    
    
    @mcp.resource("echo://{message}")
    def echo_resource(message: str) -> str:
        \"\"\"Echo a message as a resource\"\"\"
        return f"Resource echo: {message}"
    
    
    @mcp.tool()
    def echo_tool(message: str) -> str:
        \"\"\"Echo a message as a tool\"\"\"
        return f"Tool echo: {message}"
    
    
    @mcp.prompt()
    def echo_prompt(message: str) -> str:
        \"\"\"Create an echo prompt\"\"\"
        return f"Please process this message: {message}"
    ```
    """

@mcp.resource("examples://sqlite_explorer")
def get_sqlite_explorer_example() -> str:
    """SQLite浏览器示例"""
    return """
    一个更复杂的示例，展示数据库集成:
    
    ```python
    import sqlite3
    
    from mcp.server.fastmcp import FastMCP
    
    mcp = FastMCP("SQLite Explorer")
    
    
    @mcp.resource("schema://main")
    def get_schema() -> str:
        \"\"\"Provide the database schema as a resource\"\"\"
        conn = sqlite3.connect("database.db")
        schema = conn.execute("SELECT sql FROM sqlite_master WHERE type='table'").fetchall()
        return "\\n".join(sql[0] for sql in schema if sql[0])
    
    
    @mcp.tool()
    def query_data(sql: str) -> str:
        \"\"\"Execute SQL queries safely\"\"\"
        conn = sqlite3.connect("database.db")
        try:
            result = conn.execute(sql).fetchall()
            return "\\n".join(str(row) for row in result)
        except Exception as e:
            return f"Error: {str(e)}"
    ```
    """

# 高级用法
@mcp.resource("advanced://low_level_server")
def get_low_level_server() -> str:
    """低级服务器实现"""
    return """
    对于更多控制，您可以直接使用低级服务器实现。这让您可以完全访问协议并自定义服务器的各个方面，包括通过lifespan API进行生命周期管理:
    
    ```python
    from contextlib import asynccontextmanager
    from collections.abc import AsyncIterator
    
    from fake_database import Database  # Replace with your actual DB type
    
    from mcp.server import Server
    
    
    @asynccontextmanager
    async def server_lifespan(server: Server) -> AsyncIterator[dict]:
        \"\"\"Manage server startup and shutdown lifecycle.\"\"\"
        # Initialize resources on startup
        db = await Database.connect()
        try:
            yield {"db": db}
        finally:
            # Clean up on shutdown
            await db.disconnect()
    
    
    # Pass lifespan to server
    server = Server("example-server", lifespan=server_lifespan)
    
    
    # Access lifespan context in handlers
    @server.call_tool()
    async def query_db(name: str, arguments: dict) -> list:
        ctx = server.get_context()
        db = ctx.lifespan_context["db"]
        return await db.query(arguments["query"])
    ```
    """

@mcp.resource("advanced://clients")
def get_client_info() -> str:
    """MCP客户端实现信息"""
    return """
    SDK提供了高级客户端接口，用于使用各种传输连接到MCP服务器:
    
    ```python
    from mcp import ClientSession, StdioServerParameters, types
    from mcp.client.stdio import stdio_client
    
    # 为stdio连接创建服务器参数
    server_params = StdioServerParameters(
        command="python",  # 可执行文件
        args=["example_server.py"],  # 可选命令行参数
        env=None,  # 可选环境变量
    )
    
    
    # 可选: 创建采样回调
    async def handle_sampling_message(
        message: types.CreateMessageRequestParams,
    ) -> types.CreateMessageResult:
        return types.CreateMessageResult(
            role="assistant",
            content=types.TextContent(
                type="text",
                text="Hello, world! from model",
            ),
            model="gpt-3.5-turbo",
            stopReason="endTurn",
        )
    
    
    async def run():
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(
                read, write, sampling_callback=handle_sampling_message
            ) as session:
                # 初始化连接
                await session.initialize()
    
                # 列出可用提示
                prompts = await session.list_prompts()
    
                # 获取提示
                prompt = await session.get_prompt(
                    "example-prompt", arguments={"arg1": "value"}
                )
    
                # 列出可用资源
                resources = await session.list_resources()
    
                # 列出可用工具
                tools = await session.list_tools()
    
                # 读取资源
                content, mime_type = await session.read_resource("file://some/path")
    
                # 调用工具
                result = await session.call_tool("tool-name", arguments={"arg1": "value"})
    
    
    if __name__ == "__main__":
        import asyncio
    
        asyncio.run(run())
    ```
    """

# 工具方法
@mcp.tool()
def get_concept_details(concept_name: str) -> str:
    """获取特定MCP概念的详细信息
    
    参数:
    concept_name: 概念名称，可选值: server, resources, tools, prompts
    """
    concept_map = {
        "server": "concepts://server",
        "resources": "concepts://resources",
        "tools": "concepts://tools",
        "prompts": "concepts://prompts",
        "overview": "concepts://overview"
    }
    
    if concept_name in concept_map:
        resource_path = concept_map[concept_name]
        concept_func = globals().get(f"get_{concept_name}_concept", None)
        if concept_func:
            return concept_func()
        else:
            return f"找不到关于 {concept_name} 的详细信息函数"
    else:
        return f"未知概念: {concept_name}。可用选项: {', '.join(concept_map.keys())}"

@mcp.tool()
def list_available_resources() -> str:
    """列出服务器上的所有可用资源路径"""
    resources = [
        "concepts://overview", 
        "concepts://server",
        "concepts://resources", 
        "concepts://tools",
        "concepts://prompts",
        "setup://installation",
        "setup://running",
        "examples://echo_server",
        "examples://sqlite_explorer",
        "advanced://low_level_server",
        "advanced://clients"
    ]
    
    categories = {
        "concepts": "MCP核心概念",
        "setup": "安装与运行指南",
        "examples": "示例代码",
        "advanced": "高级用法"
    }
    
    result = "可用资源:\n\n"
    
    for category, description in categories.items():
        result += f"## {description}\n"
        category_resources = [r for r in resources if r.startswith(f"{category}://")]
        for resource in category_resources:
            result += f"- {resource}\n"
        result += "\n"
        
    return result

@mcp.tool()
def get_example_code(example_name: str) -> str:
    """获取示例代码
    
    参数:
    example_name: 示例名称，可选值: echo_server, sqlite_explorer
    """
    example_map = {
        "echo_server": "examples://echo_server",
        "sqlite_explorer": "examples://sqlite_explorer"
    }
    
    if example_name in example_map:
        resource_path = example_map[example_name]
        example_func = globals().get(f"get_{example_name}_example", None)
        if example_func:
            return example_func()
        else:
            return f"找不到关于 {example_name} 的示例代码函数"
    else:
        return f"未知示例: {example_name}。可用选项: {', '.join(example_map.keys())}"

@mcp.prompt()
def mcp_guide_prompt() -> str:
    """创建MCP指南提示模板"""
    return """
    我是MCP构建指南。我可以帮助你了解如何构建MCP服务器和客户端。
    
    你可以通过以下几种方式与我互动：
    1. 询问特定MCP概念(server, resources, tools, prompts)的详细信息
    2. 查看安装和运行指南
    3. 获取示例代码
    4. 了解高级用法
    
    请告诉我你想了解什么？
    """

# 主程序
if __name__ == "__main__":
    mcp.run() 