#!/usr/bin/env python3
"""
测试 OpenRouter API 连接的脚本
在运行教程之前使用此脚本测试您的 OpenRouter API key 是否工作正常
"""

from openai import OpenAI
import os

def test_openrouter_connection():
    """测试 OpenRouter 连接"""
    
    # 从环境变量或直接设置 API key
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        api_key = input("请输入您的 OpenRouter API key: ")
    
    # 配置客户端
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    
    # 测试模型列表
    models_to_test = [
        "anthropic/claude-3-haiku",
        "anthropic/claude-3-sonnet", 
        "anthropic/claude-3-opus"
    ]
    
    print("🔧 开始测试 OpenRouter 连接...")
    print(f"🔑 使用 API key: {api_key[:10]}...")
    
    for model in models_to_test:
        print(f"\n📡 测试模型: {model}")
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": "Hello! Please respond with 'OpenRouter connection successful!'"}
                ],
                max_tokens=50,
                temperature=0.0,
            )
            
            response_text = response.choices[0].message.content
            print(f"✅ 成功! 响应: {response_text}")
            
        except Exception as e:
            print(f"❌ 失败: {str(e)}")
            if "insufficient_quota" in str(e).lower():
                print("   💰 可能是余额不足，请检查您的 OpenRouter 账户余额")
            elif "unauthorized" in str(e).lower():
                print("   🔐 API key 无效，请检查您的 OpenRouter API key")
    
    print("\n🎯 测试完成!")
    print("\n📋 接下来的步骤:")
    print("1. 如果测试成功，您可以在教程中使用相应的模型")
    print("2. 如果测试失败，请检查:")
    print("   - API key 是否正确")
    print("   - OpenRouter 账户是否有足够余额")
    print("   - 网络连接是否正常")
    print("\n💡 推荐使用 claude-3-haiku 进行教程学习，它速度快且成本低")

if __name__ == "__main__":
    test_openrouter_connection()