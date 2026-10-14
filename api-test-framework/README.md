# 接口自动化测试框架

## 技术栈
Python + requests + pytest + YAML + pytest-html

## 项目结构
...

## 如何运行
pip install -r requirements.txt
pytest

## 测试对象
JSONPlaceholder 公开 API

## 测试内容
- GET /posts 列表
- GET /posts/{id} 单个
- POST /posts 创建
- PUT /posts/{id} 更新
- DELETE /posts/{id} 删除

## 报告
运行后生成 report.html