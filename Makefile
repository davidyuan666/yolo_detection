.PHONY: install train install-pdm install-python

# 检查并安装 Python
install-python:
	@echo "检查 Python 是否已安装..."
	@which python3 > /dev/null || (echo "正在安装 Python..." && \
	(apt-get update && apt-get install -y python3 python3-pip || \
	 yum install -y python3 python3-pip || \
	 brew install python3))

# 安装 pdm
install-pdm: install-python
	@echo "安装 pdm..."
	pip3 install pdm

# 安装 ultralytics 包
install: install-pdm
	pdm add ultralytics

# 训练模型
train:
	pdm run python -c "from ultralytics import YOLO; YOLO('yolov8n.yaml').train(data='coco128.yaml', epochs=3)"


# 帮助信息
commit:
	git add .
	git commit -m "update"
	git push origin main