#!/usr/bin/env python
# -*- coding: utf-8 -*-

import openai
from utils.yaml_control import read_config, mask_system, mask_user

# 设置你的 OpenAI API 密钥
openai.api_key = read_config("OPENAI_API_KEY")  # 获取config中配置的OPENAI_API_KEY
# openai.api_key = os.getenv("OPENAI_API_KEY")  # 获取你系统变量中配置的OPENAI_API_KEY

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-16k",  # 选择使用的 GPT-3.5 引擎
    messages=[
        {"role": "system", "content": mask_system},
        {"role": "user", "content": mask_user},
    ],
    max_tokens=1000  # 生成文本的最大长度
)


generated_function_name = response.choices[0].message.content
print(generated_function_name)
