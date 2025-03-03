.PHONY: install train

# 安装 ultralytics 包
install:
	pdm add ultralytics

# 训练模型
train:
	pdm run python -c "from ultralytics import YOLO; YOLO('yolov8n.yaml').train(data='coco128.yaml', epochs=3)"


# 帮助信息
commit:
	git add .
	git commit -m "update"
	git push origin main

