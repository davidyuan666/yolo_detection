import os
import argparse
from ultralytics import YOLO

def parse_args():
    parser = argparse.ArgumentParser(description='Train YOLOv8 model for defect detection')
    parser.add_argument('--data', type=str, default='data.yaml', help='path to data.yaml')
    parser.add_argument('--model', type=str, default='yolov8n.pt', help='model to start training from')
    parser.add_argument('--epochs', type=int, default=100, help='number of epochs')
    parser.add_argument('--batch-size', type=int, default=16, help='batch size')
    parser.add_argument('--imgsz', type=int, default=640, help='image size')
    parser.add_argument('--device', type=str, default='0', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    parser.add_argument('--workers', type=int, default=8, help='number of worker threads')
    parser.add_argument('--project', type=str, default='runs/train', help='save to project/name')
    parser.add_argument('--name', type=str, default='exp', help='save to project/name')
    parser.add_argument('--patience', type=int, default=50, help='EarlyStopping patience (epochs without improvement)')
    return parser.parse_args()

def main():
    # 解析命令行参数
    args = parse_args()
    
    # 确保数据文件存在
    if not os.path.exists(args.data):
        raise FileNotFoundError(f"数据配置文件 {args.data} 不存在")
    
    print(f"开始训练模型，使用配置文件: {args.data}")
    print(f"训练参数: 模型={args.model}, 轮次={args.epochs}, 批次大小={args.batch_size}, 图像尺寸={args.imgsz}")
    
    # 加载模型
    if args.model.endswith('.yaml'):
        # 从YAML配置创建新模型
        model = YOLO(args.model)
    else:
        # 从预训练权重加载模型
        model = YOLO(args.model)
    
    # 开始训练
    results = model.train(
        data=args.data,
        epochs=args.epochs,
        batch=args.batch_size,
        imgsz=args.imgsz,
        device=args.device,
        workers=args.workers,
        project=args.project,
        name=args.name,
        patience=args.patience,
        verbose=True
    )
    
    # 保存训练好的模型
    model.export()
    
    print(f"训练完成！模型已保存到 {os.path.join(args.project, args.name)}")
    
    # 评估模型在验证集上的性能
    metrics = model.val()
    print(f"验证集评估结果: mAP50-95={metrics.box.map:.4f}, mAP50={metrics.box.map50:.4f}")

if __name__ == "__main__":
    main()