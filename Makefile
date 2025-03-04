# 基础变量定义
VENV_DIR := .venv
PYTHON := python3
PDM := pdm

# 安装依赖
.PHONY: install
install:
	@echo "Installing dependencies..."
	@# 检查 Python 是否已安装
	@if ! command -v $(PYTHON) >/dev/null 2>&1; then \
		echo "Python not found. Please install Python 3.8 or higher"; \
		exit 1; \
	fi
	@# 检查 PDM 是否已安装
	@if ! command -v $(PDM) >/dev/null 2>&1; then \
		echo "PDM not found. Installing PDM..."; \
		$(PYTHON) -m pip install --user pdm; \
	fi
	@# 配置 PDM 使用镜像
	@echo "Configuring PDM to use mirror..."
	@$(PDM) config pypi.url https://pypi.tuna.tsinghua.edu.cn/simple
	@# 使用 PDM 创建虚拟环境并安装项目依赖
	@echo "Installing project dependencies with PDM..."
	@$(PDM) install --no-lock
	@echo "Installation completed successfully!"

commit:
	git add .
	git commit -m "update"
	git push origin main